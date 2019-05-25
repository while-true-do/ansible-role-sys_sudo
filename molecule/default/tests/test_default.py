import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_sudoers_package(host):
    pkg = host.package('sudo')

    assert pkg.is_installed


def test_sudoers_file(host):
    file = host.file('/etc/sudoers')

    assert file.exists
