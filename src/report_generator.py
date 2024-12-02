import os
from datetime import datetime
from .sensor_config import ROUTE_CONFIG, SENSORS

class ReportGenerator:
    def __init__(self, output_dir='output/reports'):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def generate_report(self, ten_min_data, full_route_data, ten_min_total, route_total):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'sensor_analysis_report_{timestamp}.txt'
        filepath = os.path.join(self.output_dir, filename)

        with open(filepath, 'w') as f:
            f.write("DRIVERLESS CAR SENSOR DATA ANALYSIS REPORT\n")
            f.write("=" * 50 + "\n\n")
            
            # Route Information
            f.write("ROUTE INFORMATION:\n")
            f.write("-" * 30 + "\n")
            f.write(f"Distance: {ROUTE_CONFIG['distance']} miles\n")
            f.write(f"Duration: {ROUTE_CONFIG['duration']} minutes\n")
            f.write(f"Number of Stops: {ROUTE_CONFIG['num_stops']}\n")
            f.write(f"Fixed Passengers: {ROUTE_CONFIG['passengers']}\n\n")

            # Sensor Configuration
            f.write("SENSOR CONFIGURATION:\n")
            f.write("-" * 30 + "\n")
            for sensor, config in SENSORS.items():
                f.write(f"{sensor}:\n")
                f.write(f"  - Number of Sensors: {config['count']}\n")
                f.write(f"  - Data Unit: {config['unit']}\n")
                f.write(f"  - Double Calibration: {config['double_calibration']}\n")
                f.write(f"  - Frequency: {config['frequency']}\n")
                f.write(f"  - Bytes per reading: {config['bytes']}\n\n")

            # 10-minute analysis
            f.write("10-MINUTE PERIOD ANALYSIS:\n")
            f.write("-" * 30 + "\n")
            for sensor, data in ten_min_data.items():
                f.write(f"{sensor} ({data['sensor_count']} sensors):\n")
                f.write(f"  - Data: {data['mb']:.2f} MB\n")
                f.write(f"  - Unit: {data['unit']}\n")
            f.write(f"\nTotal 10-minute data: {ten_min_total/1024/1024:.2f} MB\n\n")

            # Full route analysis
            f.write("FULL ROUTE ANALYSIS (90 minutes):\n")
            f.write("-" * 30 + "\n")
            for sensor, data in full_route_data.items():
                f.write(f"{sensor} ({data['sensor_count']} sensors):\n")
                f.write(f"  - Data: {data['mb']:.2f} MB ({data['gb']:.2f} GB)\n")
                f.write(f"  - Unit: {data['unit']}\n")
            f.write(f"\nTotal route data: {route_total/1024/1024/1024:.2f} GB\n\n")

            # Technical Requirements
            f.write("TECHNICAL REQUIREMENTS:\n")
            f.write("-" * 30 + "\n")
            throughput_per_second = route_total / (ROUTE_CONFIG['duration'] * 60)
            
            f.write("Latency Requirements:\n")
            f.write("- Millisecond sensors: <1ms processing time\n")
            f.write("- Second-frequency sensors: <1s processing time\n")
            f.write("- Double calibration overhead considered\n\n")
            
            f.write("Throughput Requirements:\n")
            f.write(f"- Raw data rate: {throughput_per_second/1024:.2f} KB/second\n")
            f.write(f"- With overhead: {(throughput_per_second*1.5)/1024:.2f} KB/second\n")
            f.write(f"- Network speed: {(throughput_per_second*8/1024/1024)*10:.2f} Mbps\n")

        return filepath 