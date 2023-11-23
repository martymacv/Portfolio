import subprocess


def run(config, functions):
    "Загружаем в config аргументы для функций, которые загружаются в **kwargs"
    for function in functions:
        print('\n', "Qatools log:", *functions[function](config), '\n')


def download(args):
    log = [subprocess.run(['wget', '{}'.format(args['path']), '/home/{}'.format(args['user_name'])])]
    return log


def install(args):
    log = [subprocess.run(['dpkg', '-i', '/home/{}/{}'.format(args['user_name'], args['deb_name'])])]
    if args['service'] == 'server':
        log.append(subprocess.run(['cp', '/etc/qatools/ipmportant_files/synapse_license/licence.info',
                                   '/usr/share/synapse/server/']))
        log.append(subprocess.run(['cp', '/etc/qatools/ipmportant_files/synapse_license/liblicense.so',
                                   '/usr/share/synapse/server/']))
    return log
