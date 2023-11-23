import qatools
import update_deb
import argparse
import json

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str)
    parser.add_argument('--mode', type=str)
    parser.add_argument('--flow', type=str)
    args = parser.parse_args()

    with open('/etc/qatools/python-scripts/SynapseQAtools/config/configurations.json') as json_file:
        j_data = json.load(json_file)

    # with open('../config/configurations.json') as json_file:
    #     j_data = json.load(json_file)

    synapse_service = qatools.SynapseService(j_data)
    user_name = synapse_service.get_user_name()
    full_update_flow = {'download': update_deb.download, 'install': update_deb.install}
    install_flow = {'install': update_deb.install}
    download_flow = {'download': update_deb.download}
    flow = {'full': full_update_flow, 'install': install_flow, 'download': download_flow}
    for role in synapse_service.get_server_role(config=args.config):
        services = synapse_service.get_service_to_update(config=args.config, server=role)
        for service in services:
            path = synapse_service.get_path_to_deb_packet(config=args.config, server=role, service=service)
            deb_name = synapse_service.get_deb_packet_name(config=args.config, server=role, service=service)

            config_to_update = {'user_name': user_name, 'path': path, 'deb_name': deb_name, 'service': service}
            update_deb.run(config_to_update, flow[args.flow])

