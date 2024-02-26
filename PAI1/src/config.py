import os
import configparser

# /home/carolcintra24/Desktop/SSII/testPAI1
config = configparser.ConfigParser()


def writeDefaultConfig():
    config['hids'] = {
        'directories_to_scan': 'filesystem',
        'hash_function': 'sha256',
        'email_to_notify': '',
        'scan_interval': 3,
        'log_interval': 3
    }
    
    config['instruciones'] = {
        'directories_to_scan': 'por defecto: filesystem, directorios para ser protegidos',
        'hash_function': 'por defecto: md5, indica: md5 | sha1 | sha256',
        'email_to_notify': 'correos para ser notificado, puede indicar varias correos separados por una coma ","',
        'scan_interval': 'por defecto: diario, indica: 1=3min, 2=1h, 3=24h',
        'log_interval': 'por defecto: mensual, indica: 1=10min, 2=24h, 3=30dias'
    }

    with open(os.getcwd() + '/src/hids.config', 'w') as configfile:
        config.write(configfile)
    return config
    

def readConfig():
    config.read(os.getcwd() + '/src/hids.config')
    
    directory = config['hids']['directories_to_scan']
    function = config['hids']['hash_function']
    email = config['hids']['email_to_notify']
    scan = config['hids']['scan_interval']
    log = config['hids']['log_interval']

    dict = {

    }
    
    #return (directory, function, email, scan, log)
    return config


def editConfig(dir, function, email, scan, log):
    config['hids'] = {
    'directories_to_scan': dir,
    'hash_function': function,
    'email_to_notify': email,
    'scan_interval': scan,
    'log_interval': log
    }
    
    with open(os.getcwd() + '/src/hids.config', 'w') as configfile:
        config.write(configfile)