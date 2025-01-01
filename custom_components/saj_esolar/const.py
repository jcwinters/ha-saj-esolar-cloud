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
    # Plant Detail Sensors
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
    "monthElectricity": {
        "name": "Month's Generation",
        "icon": "mdi:solar-power",
        "device_class": "energy",
        "state_class": "total_increasing",
        "unit": "kWh",
    },
    "yearElectricity": {
        "name": "Year's Generation",
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
    "totalConsumpElec": {
        "name": "Total Consumption",
        "icon": "mdi:home-lightning-bolt",
        "device_class": "energy",
        "state_class": "total_increasing",
        "unit": "kWh",
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
    "selfUseRate": {
        "name": "Self-Use Rate",
        "icon": "mdi:home-percent",
        "device_class": None,
        "state_class": "measurement",
        "unit": "%",
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
    },
    "lastUploadTime": {
        "name": "Last Update",
        "icon": "mdi:clock",
        "device_class": "timestamp",
        "state_class": None,
        "unit": None,
    },

    # Device Power Sensors
    "pvPower": {
        "name": "PV Power",
        "icon": "mdi:solar-power",
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
    "batteryPower": {
        "name": "Battery Power",
        "icon": "mdi:battery-charging",
        "device_class": "power",
        "state_class": "measurement",
        "unit": "W",
    },
    "outPower": {
        "name": "Output Power",
        "icon": "mdi:power-plug",
        "device_class": "power",
        "state_class": "measurement",
        "unit": "W",
    },
    "totalLoadPower": {
        "name": "Total Load Power",
        "icon": "mdi:home-lightning-bolt",
        "device_class": "power",
        "state_class": "measurement",
        "unit": "W",
    },
    "batCurr": {
        "name": "Battery Current",
        "icon": "mdi:current-dc",
        "device_class": None,
        "state_class": "measurement",
        "unit": "A",
    },
    "batEnergyPercent": {
        "name": "Battery Level",
        "icon": "mdi:battery",
        "device_class": "battery",
        "state_class": "measurement",
        "unit": "%",
    },
    "batCapcity": {
        "name": "Battery Capacity",
        "icon": "mdi:battery-charging-100",
        "device_class": None,
        "state_class": None,
        "unit": "Ah",
    },
    "pvDirection": {
        "name": "PV Direction",
        "icon": "mdi:solar-power",
        "device_class": None,
        "state_class": None,
        "unit": None,
    },
    "gridDirection": {
        "name": "Grid Direction",
        "icon": "mdi:transmission-tower",
        "device_class": None,
        "state_class": None,
        "unit": None,
    },
    "batteryDirection": {
        "name": "Battery Direction",
        "icon": "mdi:battery",
        "device_class": None,
        "state_class": None,
        "unit": None,
    },
    "outPutDirection": {
        "name": "Output Direction",
        "icon": "mdi:power-plug",
        "device_class": None,
        "state_class": None,
        "unit": None,
    },
    "isOnline": {
        "name": "Device Online",
        "icon": "mdi:power-plug",
        "device_class": None,
        "state_class": None,
        "unit": None,
    }
}

# Direction states mapping
DIRECTION_STATES = {
    -1: "Importing",
    0: "Standby",
    1: "Exporting"
}

# API endpoints
ENDPOINTS = {
    "login": "/login",
    "plant_list": "/monitor/site/getUserPlantList",
    "plant_detail": "/monitor/site/getPlantDetailInfo",
    "device_power": "/monitor/site/getStoreOrAcDevicePowerInfo",
    "plant_chart": "/monitor/site/getPlantDetailChart2"
}
