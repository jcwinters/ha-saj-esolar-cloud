# SAJ eSolar Cloud Integration for Home Assistant

A Home Assistant integration for SAJ eSolar cloud service, focused on H1 inverters with battery storage.

This integration is a complete rewrite focused on H1 inverters with battery storage, using the cloud API. The "Cloud" suffix denotes its cloud-based nature and distinguishes it from other SAJ eSolar integrations.

## Features

- Configuration through Home Assistant UI
- Comprehensive monitoring of:
  - Solar generation (current, daily, monthly, yearly, total)
  - Battery status (level, power, current, capacity)
  - Grid interaction (import/export)
  - Power flow directions
  - Environmental impact (CO₂ reduction, trees planted equivalent)
- All sensors properly organized under a single device entity
- Automatic data updates every 5 minutes

## Installation

### HACS (Recommended)

1. Open HACS in your Home Assistant instance
2. Go to "Integrations"
3. Click the three dots menu in the top right corner
4. Select "Custom repositories"
5. Add this repository URL: `https://github.com/elboletaire/ha-saj-esolar-cloud`
6. Select category: "Integration"
7. Click "Add"
8. Find "SAJ eSolar Cloud" in the integrations list and install it
9. Restart Home Assistant

### Manual Installation

1. Copy the `custom_components/saj_esolar_cloud` directory to your Home Assistant's `custom_components` directory
2. Restart Home Assistant

## Configuration

1. Go to Home Assistant's Configuration > Integrations
2. Click the "+ Add Integration" button
3. Search for "SAJ eSolar Cloud"
4. Enter your eSolar Portal credentials:
   - Username
   - Password

The integration will automatically discover your H1 inverter and set up all available sensors.

## Available Sensors

### Energy Metrics
- Current Power (W)
- Today's Generation (kWh)
- Month's Generation (kWh)
- Year's Generation (kWh)
- Total Generation (kWh)
- Total Consumption (kWh)
- Total Grid Import (kWh)
- Total Grid Export (kWh)
- Self-Use Rate (%)

### Battery Information
- Battery Level (%)
- Battery Power (W)
- Battery Current (A)
- Battery Capacity (Ah)
- Battery Direction (Charging/Discharging/Standby)

### Power Flow
- PV Power (W)
- Grid Power (W)
- Output Power (W)
- Total Load Power (W)
- PV Direction (Importing/Exporting/Standby)
- Grid Direction (Importing/Exporting/Standby)
- Output Direction (Importing/Exporting/Standby)

### Environmental Impact
- Trees Planted
- CO₂ Reduction (kg)

### System Status
- Device Online (Yes/No)
- Last Update (timestamp)

## Support

For bugs [open an issue on GitHub](https://github.com/elboletaire/ha-saj-esolar-cloud/issues).

Please, abstain from questions and feature requests, since this is a personal project and I don't have the time to provide support for it.

## Credits

Created by Òscar Casajuana ([@elboletaire](https://github.com/elboletaire))

## License

This project is licensed under the MIT License - see the LICENSE file for details.
