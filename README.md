# Load Envs for Python v.1.1.0

### Description

The variables loaded from the .env file are always in form of string, so anyone who wants to load a boolean, or a list,
should parse it.
This is a simple function that parse .env files for strings, booleans and lists and returns a dict with the passed list of env names as keys
and the parsed vars as python valid types. If *raise_no_exists* option is set it will raise an exception, otherwise
the value will be skipped.
> Please note that any value assigned as pure int or float will be parsed as number (you can not have a
number in the form of a string).


### Usage
Install the package via git:
> pip install git+https://github.com/LucioPg/load_envs_py.git

Import in your script:
> from load_envs_py import Envs

Create a list of variables names that you need:
> envs_names = (
    'SECRET_KEY',
    'INIT_ADMIN_USERNAME',
    'INIT_ADMIN_EMAIL',
    'INIT_ADMIN_PASSWORD',
    'DEBUG',
    'ALLOWED_HOSTS',
    'CORS_ORIGIN_ALLOW_ALL',
    'LOAD_CORS_SETTINGS',
    'CORS_ALLOWED_ORIGINS',
    'CSRF_TRUSTED_ORIGINS',
    'CORS_ALLOW_CREDENTIALS',
    'SESSION_COOKIE_SECURE',
    'SECURE_SSL_REDIRECT',
)

Use double quotes to separate the elements in a list:
>MYLIST = ["http://localhost:8000", "http://192.168.1.5"]

Fire the load_env script and store the parsed result in a constant, specifying the .env path if it is necessary:
>env_path = 'your_env_path'
> ENVS = Envs(envs_names, env_path)

get the variable that you need with the dotted notation:
>SECRET_KEY = ENVS.SECRET_KEY

### Options
The script needs the list of string indicating the variable that need to be parsed as first argument.
The other two args are optionals (but **recommend**):
1. *env_path* sets the path of the .env file 
2. *raise_no_exists* raise an exception if a name not represents any variable in the .env.

### Dependencies
The script depends only on dotenv==1.0.0 package.

bye bye
