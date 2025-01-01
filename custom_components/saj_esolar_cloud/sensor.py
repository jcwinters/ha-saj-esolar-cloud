"""SAJ eSolar sensor platform."""
from __future__ import annotations
from datetime import datetime
import zoneinfo

from typing import Any, cast

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    PERCENTAGE,
    UnitOfEnergy,
    UnitOfPower,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import StateType
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
)
from homeassistant.util import dt as dt_util

from .const import DEVICE_INFO, DIRECTION_STATES, DOMAIN, H1_SENSORS
from .coordinator import SAJeSolarDataUpdateCoordinator

# Device class mapping
DEVICE_CLASS_MAP = {
    "power": SensorDeviceClass.POWER,
    "energy": SensorDeviceClass.ENERGY,
    "battery": SensorDeviceClass.BATTERY,
    "timestamp": SensorDeviceClass.TIMESTAMP,
    "temperature": SensorDeviceClass.TEMPERATURE,
    "voltage": SensorDeviceClass.VOLTAGE,
}

# State class mapping
STATE_CLASS_MAP = {
    "measurement": SensorStateClass.MEASUREMENT,
    "total_increasing": SensorStateClass.TOTAL_INCREASING,
    "total": SensorStateClass.TOTAL,
}

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up SAJ eSolar sensors based on a config entry."""
    coordinator = hass.data[DOMAIN][entry.entry_id]

    # Wait for first update to ensure we have plant data
    await coordinator.async_config_entry_first_refresh()

    entities = []

    # Create sensor entities for each defined H1 sensor
    for sensor_key, sensor_config in H1_SENSORS.items():
        entities.append(
            SAJeSolarSensor(
                coordinator=coordinator,
                sensor_key=sensor_key,
                sensor_config=sensor_config,
            )
        )

    async_add_entities(entities)

class SAJeSolarSensor(CoordinatorEntity[SAJeSolarDataUpdateCoordinator], SensorEntity):
    """Representation of a SAJ eSolar sensor."""

    def __init__(
        self,
        coordinator: SAJeSolarDataUpdateCoordinator,
        sensor_key: str,
        sensor_config: dict[str, Any],
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)

        self._sensor_key = sensor_key
        self._config = sensor_config

        # Set up entity properties
        self._attr_name = f"SAJ {sensor_config['name']}"
        self._attr_unique_id = f"{DOMAIN}_{sensor_key}"
        self._attr_icon = sensor_config["icon"]
        self._attr_device_info = DEVICE_INFO

        # Set device class from mapping
        if sensor_config["device_class"]:
            self._attr_device_class = DEVICE_CLASS_MAP.get(sensor_config["device_class"])

        # Set state class from mapping
        if sensor_config["state_class"]:
            self._attr_state_class = STATE_CLASS_MAP.get(sensor_config["state_class"])

        # Set unit of measurement
        if sensor_config["unit"]:
            self._attr_native_unit_of_measurement = sensor_config["unit"]

    @property
    def native_value(self) -> StateType:
        """Return the sensor value."""
        try:
            data = self.coordinator.data

            # Plant Detail Sensors
            if self._sensor_key in [
                "nowPower", "todayElectricity", "monthElectricity",
                "yearElectricity", "totalElectricity", "totalConsumpElec",
                "totalBuyElec", "totalSellElec", "totalPlantTreeNum",
                "totalReduceCo2"
            ]:
                return float(data["plant_details"]["plantDetail"][self._sensor_key])
            elif self._sensor_key == "lastUploadTime":
                # Parse the timestamp string to datetime object with timezone
                timestamp = data["plant_details"]["plantDetail"]["lastUploadTime"]
                naive_dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                return dt_util.as_utc(naive_dt)
            elif self._sensor_key == "selfUseRate":
                # Remove % symbol and convert to float
                value = data["plant_details"]["plantDetail"]["selfUseRate"]
                return float(value.rstrip("%"))

            # Device Power Sensors
            elif self._sensor_key in [
                "pvPower", "gridPower", "batteryPower", "outPower",
                "totalLoadPower", "batCurr", "batEnergyPercent",
                "batCapcity"
            ]:
                return float(data["device_power"]["storeDevicePower"][self._sensor_key])

            # Battery Info Sensors
            elif self._sensor_key in ["batVoltage", "batTemperature"]:
                return float(data["battery_info"][self._sensor_key])

            # Direction Sensors
            elif self._sensor_key in [
                "pvDirection", "gridDirection", "batteryDirection",
                "outPutDirection"
            ]:
                value = int(data["device_power"]["storeDevicePower"][self._sensor_key])
                return DIRECTION_STATES.get(value, f"Unknown ({value})")

            # Online Status
            elif self._sensor_key == "isOnline":
                value = int(data["device_power"]["storeDevicePower"]["isOnline"])
                return "Yes" if value else "No"

            return None
        except (KeyError, TypeError, ValueError):
            return None

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        if self.coordinator.data is None:
            return False

        try:
            # Check if device is online
            online = self.coordinator.data["device_power"]["storeDevicePower"]["isOnline"]
            return bool(int(online))
        except (KeyError, TypeError, ValueError):
            return False
