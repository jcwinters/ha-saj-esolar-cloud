"""SAJ eSolar sensor platform."""
from __future__ import annotations

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

from .const import DEVICE_INFO, DIRECTION_STATES, DOMAIN, H1_SENSORS
from .coordinator import SAJeSolarDataUpdateCoordinator

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

        # Set up sensor properties based on device class
        if sensor_config["device_class"] == "power":
            self._attr_device_class = SensorDeviceClass.POWER
            self._attr_native_unit_of_measurement = UnitOfPower.WATT
        elif sensor_config["device_class"] == "energy":
            self._attr_device_class = SensorDeviceClass.ENERGY
            self._attr_native_unit_of_measurement = UnitOfEnergy.KILO_WATT_HOUR
        elif sensor_config["device_class"] == "battery":
            self._attr_device_class = SensorDeviceClass.BATTERY
            self._attr_native_unit_of_measurement = PERCENTAGE
        elif sensor_config["device_class"] == "timestamp":
            self._attr_device_class = SensorDeviceClass.TIMESTAMP
        elif sensor_config["unit"]:
            self._attr_native_unit_of_measurement = sensor_config["unit"]

        # Set up state class
        if sensor_config["state_class"] == "measurement":
            self._attr_state_class = SensorStateClass.MEASUREMENT
        elif sensor_config["state_class"] == "total_increasing":
            self._attr_state_class = SensorStateClass.TOTAL_INCREASING
        elif sensor_config["state_class"] == "total":
            self._attr_state_class = SensorStateClass.TOTAL

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
                "totalReduceCo2", "lastUploadTime"
            ]:
                value = data["plant_details"]["plantDetail"][self._sensor_key]
                if self._sensor_key == "selfUseRate":
                    # Remove % symbol and convert to float
                    return float(value.rstrip("%"))
                return value

            # Device Power Sensors
            elif self._sensor_key in [
                "pvPower", "gridPower", "batteryPower", "outPower",
                "totalLoadPower", "batCurr", "batEnergyPercent",
                "batCapcity"
            ]:
                return float(data["device_power"]["storeDevicePower"][self._sensor_key])

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
