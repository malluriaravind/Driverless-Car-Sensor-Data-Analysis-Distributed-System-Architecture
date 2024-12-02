# Driverless Car Sensor Data Analysis

## Project Overview
This project analyzes sensor data from a driverless car to calculate total data generation and technical requirements.

### Route Specifications
- Distance: 100 miles
- Duration: 90 minutes
- Number of Stops: 3
- Fixed Passengers: 2

### Sensor Configuration

| Sensor Type    | Frequency      | Bytes | Count | Double Calibration | Data Type | Unit                  |
|---------------|---------------|-------|-------|-------------------|-----------|----------------------|
| Temperature   | per second    | 8     | 100   | No                | Double    | Percentage           |
| Humidity      | per second    | 8     | 25    | No                | Double    | Percentage           |
| Tire Pressure | per second    | 8     | 8     | Yes               | Double    | Force per area       |
| Vibrations    | per millisec  | 4     | 100   | Yes               | Integer   | Velocity             |
| Torque        | per millisec  | 4     | 100   | Yes               | Integer   | Force per area       |
| Proximity     | per millisec  | 4     | 20    | Yes               | Integer   | Proximity            |
| GPS           | per second    | 8     | 3     | No                | Double    | Latitude, Longitude  |
| Bluetooth     | per second    | 4     | 2     | No                | Integer   | Number of Devices    |
| Brake Sensors | per second    | 8     | 6     | Yes               | Double    | Break device rotations|

## Project Structure
riverless_car_analysis/
│
├── src/
│ ├── init.py
│ ├── sensor_config.py
│ ├── data_calculator.py
│ └── report_generator.py
│
├── output/
│ └── reports/
│
├── main.py
└── requirements.txt

## Installation & Setup

1. Create project directory structure:

bash
mkdir -p driverless_car_analysis/src driverless_car_analysis/output/reports
cd driverless_car_analysis

2. Copy source files to their respective locations
3. No additional dependencies required

## Usage

Run the analysis:

```bash
python main.py
```

## Output

The script generates a detailed report in `output/reports` containing:

1. Route Information
   - Distance, duration, stops, passengers

2. Sensor Configuration Details
   - Number of sensors
   - Data units
   - Calibration requirements
   - Frequency
   - Data size per reading

3. Data Analysis
   - 10-minute period analysis
   - Full route analysis (90 minutes)
   - Per-sensor data generation
   - Total data volume

4. Technical Requirements
   - Latency requirements
   - Throughput calculations
   - Network speed recommendations

## Calculations

### Data Generation Formula

```python
total_bytes = readings_per_second * duration_in_seconds * bytes_per_reading * number_of_sensors * calibration_factor
```
where:
- readings_per_second: 1000 for millisecond sensors, 1 for second sensors
- calibration_factor: 2 for double calibration, 1 for single calibration

### Unit Conversions
- 1 MB = 1,048,576 bytes
- 1 GB = 1,073,741,824 bytes


