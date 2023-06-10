"""
author: https://www.github.com/LucioPg

"""

from dotenv import load_dotenv
import os
import json


class Envs:
    """Simple class that parse .env files. The passed list of env names will be set as attrs with the related values.
     If raise_no_exists is set it will raise an exception, otherwise the value will be skipped.
    Please note that any value assigned as pure int or float will be parsed as number (you can not have a
    number as a string ).
    :param env_names: tuple of name of vars that should be set
    :param env_path: str an existing path to the .env
    :param raise_no_exists: bool default False for to raise an exception when a requested var is not present into the env"""

    def __init__(self, env_names: tuple, env_path: str = 'blue', raise_no_exists=False):
        self.env_path = env_path
        self.env_names = env_names
        self.raise_no_exists = raise_no_exists

        self.load()

    def load(self):
        self._set_properties(self._load_envs())

    def _set_properties(self, props_dict):
        for attr, value in props_dict.items():
            setattr(self, attr, value)

    def _load_envs(self):
        if self.env_path:
            load_dotenv(self.env_path)
        else:
            load_dotenv()
        true_vars = ('True', 'true', '1')
        false_vars = ('False', 'false', '0')
        none_vars = ('None', 'none', 'Null', 'null')
        envs = {}
        for env_name in self.env_names:
            # check if the name is present in the .env
            # if not it will raise a KeyError and the name will not be added
            try:
                var = os.environ[env_name]
                # test the bools
                # if it is a bool should be in true_vars or in false_vars
                if var in true_vars or var in false_vars:
                    envs[env_name] = var in true_vars
                elif var in none_vars:
                    envs[env_name] = None
                else:
                    # test if it is a string or a list
                    try:
                        list_var = json.loads(var)
                        envs[env_name] = list_var
                    except json.decoder.JSONDecodeError:
                        # in this case should be a string or number
                        envs[env_name] = var
            except KeyError:
                if self.raise_no_exists:
                    raise Exception(f'No variable named "{env_name}" is present in the .env file ')
                else:
                    pass
        return envs
