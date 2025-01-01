"""Constants for the SAJ eSolar integration."""
from typing import Final

DOMAIN: Final = "saj_esolar"
MANUFACTURER: Final = "SAJ"
MODEL: Final = "H1"

# Base URL for the SAJ eSolar API
BASE_URL: Final = "https://fop.saj-electric.com/saj"

# Update interval
UPDATE_INTERVAL: Final = 300  # 5 minutes

# Device info
DEVICE_INFO = {
    "identifiers": {("saj_esolar", "h1")},
    "name": "SAJ H1 Solar Inverter",
    "manufacturer": MANUFACTURER,
    "model": MODEL,
}

# Sensor definitions for H1 device
H1_SENSORS = {
    "nowPower": {
        "name": "Current Power",
        "icon": "mdi:solar-power",
        "device_class": "power",
        "state_class": "measurement",
        "unit": "W",
    },
    "todayElectricity": {
        "name": "Today's Generation",
        "icon": "mdi:solar-power",
        "device_class": "energy",
        "state_class": "total_increasing",
        "unit": "kWh",
    },
    "totalElectricity": {
        "name": "Total Generation",
        "icon": "mdi:solar-power",
        "device_class": "energy",
        "state_class": "total_increasing",
        "unit": "kWh",
    },
    "batEnergyPercent": {
        "name": "Battery Level",
        "icon": "mdi:battery",
        "device_class": "battery",
        "state_class": "measurement",
        "unit": "%",
    },
    "batteryPower": {
        "name": "Battery Power",
        "icon": "mdi:battery-charging",
        "device_class": "power",
        "state_class": "measurement",
        "unit": "W",
    },
    "gridPower": {
        "name": "Grid Power",
        "icon": "mdi:transmission-tower",
        "device_class": "power",
        "state_class": "measurement",
        "unit": "W",
    },
    "totalBuyElec": {
        "name": "Total Grid Import",
        "icon": "mdi:transmission-tower-import",
        "device_class": "energy",
        "state_class": "total_increasing",
        "unit": "kWh",
    },
    "totalSellElec": {
        "name": "Total Grid Export",
        "icon": "mdi:transmission-tower-export",
        "device_class": "energy",
        "state_class": "total_increasing",
        "unit": "kWh",
    },
    "chargeElec": {
        "name": "Total Battery Charge",
        "icon": "mdi:battery-plus",
        "device_class": "energy",
        "state_class": "total_increasing",
        "unit": "kWh",
    },
    "dischargeElec": {
        "name": "Total Battery Discharge",
        "icon": "mdi:battery-minus",
        "device_class": "energy",
        "state_class": "total_increasing",
        "unit": "kWh",
    },
    "h1Online": {
        "name": "Device Online",
        "icon": "mdi:power-plug",
        "device_class": None,
        "state_class": None,
        "unit": None,
    },
    "totalPlantTreeNum": {
        "name": "Trees Planted",
        "icon": "mdi:tree",
        "device_class": None,
        "state_class": "total",
        "unit": None,
    },
    "totalReduceCo2": {
        "name": "CO₂ Reduction",
        "icon": "mdi:molecule-co2",
        "device_class": None,
        "state_class": "total",
        "unit": "kg",
    }
}

# API endpoints
ENDPOINTS = {
    "login": "/login",
    "plant_list": "/monitor/site/getUserPlantList",
    "plant_detail": "/monitor/site/getPlantDetailInfo",
    "device_power": "/monitor/site/getStoreOrAcDevicePowerInfo",
    "plant_chart": "/monitor/site/getPlantDetailChart2"
}
