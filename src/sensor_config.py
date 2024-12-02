SENSORS = {
    'Temperature': {
        'frequency': 'second',
        'bytes': 8,
        'count': 100,
        'double_calibration': False,
        'data_type': 'Temperature',
        'unit': 'Percentage'
    },
    'Humidity': {
        'frequency': 'second',
        'bytes': 8,
        'count': 25,
        'double_calibration': False,
        'data_type': 'Temperature',
        'unit': 'Percentage'
    },
    'Tire Pressure': {
        'frequency': 'second',
        'bytes': 8,
        'count': 8,
        'double_calibration': True,
        'data_type': 'Force',
        'unit': 'Force per area'
    },
    'Vibrations': {
        'frequency': 'millisecond',
        'bytes': 4,
        'count': 100,
        'double_calibration': True,
        'data_type': 'Integer',
        'unit': 'Velocity'
    },
    'Torque': {
        'frequency': 'millisecond',
        'bytes': 4,
        'count': 100,
        'double_calibration': True,
        'data_type': 'Integer',
        'unit': 'Force per area'
    },
    'Proximity': {
        'frequency': 'millisecond',
        'bytes': 4,
        'count': 20,
        'double_calibration': True,
        'data_type': 'Integer',
        'unit': 'Proximity'
    },
    'GPS': {
        'frequency': 'second',
        'bytes': 8,
        'count': 3,
        'double_calibration': False,
        'data_type': 'Double',
        'unit': 'Latitude, Longitude'
    },
    'Bluetooth': {
        'frequency': 'second',
        'bytes': 4,
        'count': 2,
        'double_calibration': False,
        'data_type': 'Integer',
        'unit': 'Number of Devices'
    },
    'Brake Sensors': {
        'frequency': 'second',
        'bytes': 8,
        'count': 6,
        'double_calibration': True,
        'data_type': 'Double',
        'unit': 'Break devices rotations'
    }
}

ROUTE_CONFIG = {
    'distance': 100,  # miles
    'duration': 90,   # minutes
    'num_stops': 3,
    'passengers': 2
}

CONSTANTS = {
    'SECONDS_IN_MINUTE': 60,
    'BYTES_TO_MB': 1024 * 1024,
    'BYTES_TO_GB': 1024 * 1024 * 1024
}