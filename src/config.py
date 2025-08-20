
class _Logger:
    debug = True
    file = 'D:/%USERNAME%/Py-Projects/CalcHelper/logs.ph'
    pass


_values = {
    'add_sub': {
        'levels': {
            'min': 0,
            'max': 99,
            'default': {
                'level': 15,
                'min': 30,
                'max': 50
            }
        },
        'learn': {
            'timing': 2,  # sec
            'qty': 10
        },
        'check': {
            'timing': 6,  # sec
            'qty': 20
        },
        'repeat': {
            'timing': 9,  # sec
            'qty': 25
        }
    },
    'mul_div': {
        'levels': {
            'min': 0,
            'max': 9,
            'default': {
                'level': 7,
                'min': 6,
                'max': 9
            }
        },
        'learn': {
            'timing': 2,  # sec
            'qty': 10
        },
        'check': {
            'timing': 6,  # sec
            'qty': 20
        },
        'repeat': {
            'timing': 9,  # sec
            'qty': 30
        }
    }
}


class _Config:
    logger = _Logger
    values = _values
    pass


config = _Config
