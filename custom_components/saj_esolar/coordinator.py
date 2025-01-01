"""DataUpdateCoordinator for SAJ eSolar integration."""
from datetime import datetime, timedelta
import logging
from typing import Any

import aiohttp
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.exceptions import ConfigEntryAuthFailed

from .const import BASE_URL, DOMAIN, ENDPOINTS, UPDATE_INTERVAL

_LOGGER = logging.getLogger(__name__)

class SAJeSolarDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching data from the SAJ eSolar API."""

    def __init__(
        self,
        hass: HomeAssistant,
        session: aiohttp.ClientSession,
        username: str,
        password: str,
    ) -> None:
        """Initialize."""
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=UPDATE_INTERVAL),
        )
        self.session = session
        self.username = username
        self.password = password
        self._plant_id = None

    async def _async_update_data(self) -> dict[str, Any]:
        """Update data via API."""
        try:
            # Login
            login_data = {
                "lang": "en",
                "username": self.username,
                "password": self.password,
                "rememberMe": "true",
            }
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded",
            }

            async with self.session.post(
                f"{BASE_URL}{ENDPOINTS['login']}",
                data=login_data,
                headers=headers,
            ) as resp:
                if resp.status == 401:
                    raise ConfigEntryAuthFailed("Invalid authentication")
                if resp.status != 200:
                    raise UpdateFailed(f"Login failed with status {resp.status}")

            # Get plant list
            client_date = datetime.now().strftime("%Y-%m-%d")
            plant_list_data = f"pageNo=&pageSize=&orderByIndex=&officeId=&clientDate={client_date}&runningState=&selectInputType=1&plantName=&deviceSn=&type=&countryCode=&isRename=&isTimeError=&systemPowerLeast=&systemPowerMost="

            async with self.session.post(
                f"{BASE_URL}{ENDPOINTS['plant_list']}",
                data=plant_list_data,
                headers=headers,
            ) as resp:
                if resp.status != 200:
                    raise UpdateFailed(f"Failed to get plant list: {resp.status}")
                plant_info = await resp.json()

                if not plant_info.get("plantList"):
                    raise UpdateFailed("No plants found")

                # Use the first plant if plant_id is not set
                if self._plant_id is None:
                    self._plant_id = 0

                plant = plant_info["plantList"][self._plant_id]
                plant_uid = plant["plantuid"]

            # Get plant details
            plant_detail_data = f"plantuid={plant_uid}&clientDate={client_date}"
            async with self.session.post(
                f"{BASE_URL}{ENDPOINTS['plant_detail']}",
                data=plant_detail_data,
                headers=headers,
            ) as resp:
                if resp.status != 200:
                    raise UpdateFailed(f"Failed to get plant details: {resp.status}")
                plant_details = await resp.json()

            # Get device power info (specific to H1)
            device_sn = plant_details["plantDetail"]["snList"][0]
            epoch_ms = int(datetime.now().timestamp() * 1000)

            async with self.session.post(
                f"{BASE_URL}{ENDPOINTS['device_power']}?plantuid=&devicesn={device_sn}&_={epoch_ms}",
                headers=headers,
            ) as resp:
                if resp.status != 200:
                    raise UpdateFailed(f"Failed to get device power info: {resp.status}")
                device_power = await resp.json()

            # Combine all data
            data = {
                "plant_info": plant_info,
                "plant_details": plant_details,
                "device_power": device_power,
            }

            # Logout and clear session
            await self.session.post(f"{BASE_URL}/logout", headers=headers)
            return data

        except aiohttp.ClientError as err:
            raise UpdateFailed(f"Error communicating with API: {err}")
        except Exception as err:
            raise UpdateFailed(f"Error fetching data: {err}")
