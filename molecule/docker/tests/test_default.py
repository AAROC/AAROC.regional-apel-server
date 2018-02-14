import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_config_files(host):
    apel_config_dir = host.file('/etc/apel')
    
    # Various apel config files
    apel_auth_config_file = host.file('/etc/apel/auth.cfg')
    apel_db_config_file   = host.file('/etc/apel/db.cfg')
    apel_receiver_file    = host.file('/etc/apel/receiver.cfg')
    
    assert apel_auth_config_file.exists
    assert apel_db_config_file.exists
    assert apel_receiver_file.exists