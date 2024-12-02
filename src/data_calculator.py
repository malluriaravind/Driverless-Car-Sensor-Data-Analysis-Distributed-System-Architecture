from .sensor_config import SENSORS, CONSTANTS

class DataCalculator:
    def __init__(self):
        self.sensors = SENSORS
        self.constants = CONSTANTS

    def calculate_sensor_data(self, duration_minutes, sensor_config):
        readings_per_second = 1000 if sensor_config['frequency'] == 'millisecond' else 1
        total_seconds = duration_minutes * self.constants['SECONDS_IN_MINUTE']
        total_readings = total_seconds * readings_per_second
        
        # Calculate total bytes considering number of sensors and double calibration
        total_bytes = (total_readings * sensor_config['bytes'] * sensor_config['count'])
        if sensor_config['double_calibration']:
            total_bytes *= 2
            
        return total_bytes

    def calculate_period_data(self, duration_minutes):
        results = {}
        total_bytes = 0
        
        for sensor, config in self.sensors.items():
            bytes_generated = self.calculate_sensor_data(duration_minutes, config)
            mb_generated = bytes_generated / self.constants['BYTES_TO_MB']
            gb_generated = bytes_generated / self.constants['BYTES_TO_GB']
            
            results[sensor] = {
                'bytes': bytes_generated,
                'mb': mb_generated,
                'gb': gb_generated,
                'sensor_count': config['count'],
                'unit': config['unit'],
                'double_calibration': config['double_calibration']
            }
            total_bytes += bytes_generated
            
        return results, total_bytes 