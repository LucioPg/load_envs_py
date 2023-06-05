"""
author: https://www.github.com/LucioPg

"""

from dotenv import load_dotenv
import os
import json


def load_envs(env_names: tuple, env_path: str = '', raise_no_exists: bool = False) -> dict:
    """Simple function that parse .env files and returns a dict with the passed list of env names as keys
    and the parsed vars as python values. If raise_no_exists is set it will raise an exception, otherwise
    the value will be skipped.
    Please note that any value assigned as pure int or float will be parsed as number (you can not have a
    number as a string ).
    :param env_names: tuple of name of vars that should be set
    :param env_path: str an existing path to the .env
    :param raise_no_exists: bool default False for to raise an exception
     when a requested var is not present into the env
    :returns dict
    """
    if env_path:
        load_dotenv(env_path)
    else:
        load_dotenv()
    true_vars = ('True', 'true', '1')
    false_vars = ('False', 'false', '0')
    none_vars = ('None', 'none', 'Null', 'null')
    envs = {}
    for env_name in env_names:
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
            if raise_no_exists:
                raise Exception(f'No variable named "{env_name}" is present in the .env file ')
            else:
                pass
    return envs
