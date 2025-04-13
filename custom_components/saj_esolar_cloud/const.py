"""Constants for the SAJ eSolar Cloud integration."""
from typing import Final

DOMAIN: Final = "saj_esolar_cloud"
MANUFACTURER: Final = "SAJ"
MODEL: Final = "H1"

# Base URL for the SAJ eSolar API
# China portal
# BASE_URL: Final = "https://op.saj-electric.com/saj"
# European Portal
# BASE_URL: Final = "https://fop.saj-electric.com/saj"
# International Portal
BASE_URL: Final = "https://intoop.saj-electric.com/saj"

# Update interval
UPDATE_INTERVAL: Final = 300  # 5 minutes

# Device info
DEVICE_INFO = {
    "identifiers": {(DOMAIN, "h1")},
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
        "name": "Today Generation",
        "icon": "mdi:solar-power",
        "device_class": "energy",
        "state_class": "total_increasing",
        "unit": "kWh",
    },
    "monthElectricity": {
        "name": "Current Month Generation",
        "icon": "mdi:solar-power",
        "device_class": "energy",
        "state_class": "total_increasing",
        "unit": "kWh",
    },
    "yearElectricity": {
        "name": "Current Year Generation",
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
        "unit": "t",
    },
    "dailyConsumption": {
        "name": "Today Consumption",
        "icon": "mdi:home-lightning-bolt",
        "device_class": "energy",
        "state_class": "total_increasing",
        "unit": "kWh",
    },
    "dailyGridImport": {
        "name": "Today Grid Import",
        "icon": "mdi:transmission-tower-import",
        "device_class": "energy",
        "state_class": "total_increasing",
        "unit": "kWh",
    },
    "dailyGridExport": {
        "name": "Today Grid Export",
        "icon": "mdi:transmission-tower-export",
        "device_class": "energy",
        "state_class": "total_increasing",
        "unit": "kWh",
    },
    "dailyBatteryCharge": {
        "name": "Today Battery Charge",
        "icon": "mdi:battery-charging",
        "device_class": "energy",
        "state_class": "total_increasing",
        "unit": "kWh",
    },
    "dailyBatteryDischarge": {
        "name": "Today Battery Discharge",
        "icon": "mdi:battery-minus",
        "device_class": "energy",
        "state_class": "total_increasing",
        "unit": "kWh",
    },
    "dailyTreesPlanted": {
        "name": "Today Trees Planted",
        "icon": "mdi:tree",
        "device_class": None,
        "state_class": "total",
        "unit": None,
    },
    "dailyReduceCo2": {
        "name": "Today CO2 Reduction",
        "icon": "mdi:molecule-co2",
        "device_class": None,
        "state_class": "total",
        "unit": "t",
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
        "description": "Positive when importing, negative when exporting",
    },
    "gridPowerAbsolute": {
        "name": "Grid Power Absolute",
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
        "description": "Positive when discharging, negative when charging",
    },
    "batteryPowerAbsolute": {
        "name": "Battery Power Absolute",
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
    "batVoltage": {
        "name": "Battery Voltage",
        "icon": "mdi:lightning-bolt",
        "device_class": "voltage",
        "state_class": "measurement",
        "unit": "V",
    },
    "batTemperature": {
        "name": "Battery Temperature",
        "icon": "mdi:thermometer",
        "device_class": "temperature",
        "state_class": "measurement",
        "unit": "°C",
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

# Battery states mapping
BATTERY_STATES = {
    -1: "Charging",
    0: "Idle",
    1: "Discharging"
}

# API endpoints
ENDPOINTS = {
    "login": "/login",
    "plant_list": "/monitor/site/getUserPlantList",
    "plant_detail": "/monitor/site/getPlantDetailInfo",
    "device_power": "/monitor/site/getStoreOrAcDevicePowerInfo",
    "plant_chart": "/monitor/site/getPlantDetailChart2",
    "battery_info": "/cloudMonitor/deviceInfo/findBatteryRealTimeList"
}
