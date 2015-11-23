import os


def update_environ_from_env_config_file():
    '''
    You can create an .env.yml file to override/specify environment variables
    that are used in settings.py.
    '''
    try:
        for line in open('.env'):
            line = line.strip()

            if not line:
                continue

            if line.startswith('#'):
                continue

            k, v = line.split('=', 1)

            os.environ[k] = v
    except FileNotFoundError:
        pass


def env_get_bool(name, default):
    '''
    Helper to cast to bool when the value could be a string or bool
    '''
    return str(os.environ.get(name, default)).lower()[0] == 't'
