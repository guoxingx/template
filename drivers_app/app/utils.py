
CONFIG = {}


def populate_config(config):
    global CONFIG
    for key in dir(config):
        if key.isupper():
            CONFIG[key] = getattr(config, key)


def config_value(key):
    global CONFIG
    return CONFIG.get(key)
