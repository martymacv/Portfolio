class SynapseService:
    def __init__(self, synapse_config=None):
        self.__synapse_config = synapse_config

    def get_test_config(self, config='1'):
        return self.__synapse_config[config]

    def get_user_name(self):
        return self.__synapse_config['user_name']

    def get_server_role(self, config='1'):
        return [role for role in self.__synapse_config[config]]

    def get_service_to_update(self, config='1', server='A'):
        return [service for service in self.__synapse_config[config][server]]

    def get_deb_packet_name(self, config='1', server='A', service='server'):
        path = self.__synapse_config[config][server][service]
        return path[path.rfind('/') + 1:]

    def get_path_to_deb_packet(self, config='1', server='A', service='server'):
        return self.__synapse_config[config][server][service]

    def set_path_to_deb(self, config='1', server='A', service='server', path='https://'):
        self.__synapse_config[config][server][service] = path
        print(self.__synapse_config)





    # def enter_path(self, path):
    #     self.__path = path
    #     self.__deb_name = path[path.rfind('/') + 1:]
    #     self.__component = self.__deb_name[self.__deb_name.find('-') + 1:self.__deb_name.find('_')]
    #     return self.__path, self.__deb_name
    #
    # def enter_user_name(self, user_name):
    #     self.__user_name = user_name
    #     return self.__user_name,
    #
    # def __download(self):
    #     return subprocess.run(['wget', '{}'.format(self.__path), '/home/{}'.format(self.__user_name)])
    #
    # def __install_deb(self):
    #     return subprocess.run(['dpkg', '-i', '/home/{}/{}'.format(self.__user_name, self.__deb_name)])
    #
    # def install(self, mode):
    #     self.__download()
    #     self.__install_deb()
    #
    # def licencing(self, mode):
    #     if self.__component == 'server':
    #         subprocess.run(['cp', '/etc/qatools/ipmportant_files/synapse_license/licence.info', '/usr/share/synapse/server/'])
    #         subprocess.run(['cp', '/etc/qatools/ipmportant_files/synapse_license/liblicense.so', '/usr/share/synapse/server/'])
