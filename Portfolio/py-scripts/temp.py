import subprocess

import paramiko
from paramiko import SSHClient

REDUNDANCY = 'Redundancy'
STANDALONE = 'Standalone'


class SynapseService:
    def __init__(self, synapse_config):
        self.__deb_name = None
        self.__user_name = None
        self.__path = None
        self.__component = None
        self.__synapse_config = synapse_config

    def enter_path(self, path):
        self.__path = path
        self.__deb_name = path[path.rfind('/') + 1:]
        self.__component = self.__deb_name[self.__deb_name.find('-') + 1:self.__deb_name.find('_')]
        return self.__path, self.__deb_name

    def enter_user_name(self, user_name):
        self.__user_name = user_name
        return self.__user_name,

    def __download(self):
        return subprocess.run(['wget', '{}'.format(self.__path), '/home/{}'.format(self.__user_name)])

    def __download_to_remote_host(self):
        ssh = SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh.connect(self.__synapse_config['ip_addresses']['server_B1'], username='ubuntu', password='1q2w3e4r')
            stdin, stdout, stderr = ssh.exec_command('wget {} /home/{}'.format(self.__path, self.__user_name))
            for line in stdout.readlines():
                print(line.decode('utf-8'))
        finally:
            stdin.close()
            stdout.close()
            stderr.close()
            ssh.close()

    def __install_deb(self):
        return subprocess.run(['dpkg', '-i', '/home/{}/{}'.format(self.__user_name, self.__deb_name)])

    def __install_deb_to_remote_host(self):
        ssh = SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh.connect(self.__synapse_config['ip_addresses']['server_B1'], username='ubuntu', password='1q2w3e4r')
            stdin, stdout, stderr = ssh.exec_command('dpkg -i /home/{}/{}'.format(self.__user_name, self.__deb_name))
            for line in stdout.readlines():
                print(line.decode('utf-8'))
        finally:
            stdin.close()
            stdout.close()
            stderr.close()
            ssh.close()

    def install(self, mode):
        self.__download()
        self.__install_deb()
        if mode == 'Redundancy':
            self.__download_to_remote_host()
            self.__install_deb_to_remote_host()

    def licencing(self, mode):
        if self.__component == 'server':
            subprocess.run(['cp', '/etc/qatools/ipmportant_files/synapse_license/licence.info', '/usr/share/synapse/server/'])
            subprocess.run(['cp', '/etc/qatools/ipmportant_files/synapse_license/liblicense.so', '/usr/share/synapse/server/'])
        if mode == 'Redundancy' and self.__component == 'server':
            ssh = SSHClient()
            ssh.load_system_host_keys()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            try:
                ssh.connect(self.__synapse_config['ip_addresses']['server_B1'], username='ubuntu', password='1q2w3e4r')
                stdin, stdout, stderr = ssh.exec_command(
                    'cp /etc/qatools/ipmportant_files/synapse_license/licence.info /usr/share/synapse/server/')
                for line in stdout.readlines():
                    print(line.decode('utf-8'))
                stdin, stdout, stderr = ssh.exec_command(
                    'cp /etc/qatools/ipmportant_files/synapse_license/liblicense.so /usr/share/synapse/server/')
                for line in stdout.readlines():
                    print(line.decode('utf-8'))
            finally:
                stdin.close()
                stdout.close()
                stderr.close()
                ssh.close()

