import requests
import yaml


class TestEnvironment:
    "Этот класс создает объекты типа тестовое окружение для Синапса и описывает его состав"
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
        "Загружаем страницу и делаем выборку элементов страницы со ссылками на скачивание"
        url = 'https://digispot.gitlab.com/{}'.format(service)
        req = requests.get(url)
        text = req.text
        # или
        data = req.json()
        self.__synapse_config[config][server][service] = data['name']['link_to_download']
        return self.__synapse_config[config][server][service]

    def set_path_to_deb(self, config='1', server='A', service='server', path='https://'):
        self.__synapse_config[config][server][service] = path
        print(self.__synapse_config)


class NetworkConfig:
    "Этот класс создает объекты типа Сетевые настройки"
    def __int__(self, network_config=None):
        self.__network_config = network_config

    def read_local_netplan(self):
        with open('/etc/netplan/00.yaml', 'r') as file:
            netplan = yaml.safe_load(file)
        self.__network_config['networks']['ip_addresess']['server_A1'], \
            self.__network_config['networks']['ip_addresess']['server_A2'] = \
            netplan['network']['esp0s9']['addresses']

    def set_ip_addresses(self, role='A', general_ip='localhost', reserve_ip='localhost'):
        self.__network_config['networks']['ip_addresess'][f'server_{role.upper()}1'] = general_ip
        self.__network_config['networks']['ip_addresess'][f'server_{role.upper()}2'] = reserve_ip


class ServerModeConfig:
    "Этот класс создает объекты типа режима работы сервера (с резервированием или без)"
    def __init__(self, mode_config=None):
        self.__mode_config = mode_config

    def set_server_mode(self, standalone=True, trunk=True, sip=True):
        self.__mode_config['standalone'] = standalone
        self.__mode_config['redundancy'] = ~standalone
        self.__mode_config['trunk'] = trunk
        self.__mode_config['sip'] = sip