
CONFIG = {}


def populate_config(config):
    global CONFIG
    for key in dir(config):
        if key.isupper():
            CONFIG[key] = getattr(config, key)
