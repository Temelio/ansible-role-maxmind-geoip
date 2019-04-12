"""
Role tests
"""

import os
import pytest

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_packages(host):
    """
    Check if packages are installed
    """

    packages = [
            'libmaxminddb0',
            'mmdb-bin',
            'geoipupdate',
            ]

    for package in packages:
        assert host.package(package).is_installed


def test_databases_download(host):
    """
    Check if databases downloaded files exists
    """

    if host.system_info.distribution != 'debian':
        pytest.skip('Not apply to %s' % host.system_info.distribution)

    databases_folder_path = '/usr/share/GeoIP'

    databases_files = [
        '{}/GeoLite2-City.mmdb'.format(databases_folder_path),
        '{}/GeoLite2-Country.mmdb'.format(databases_folder_path),
    ]

    for database_file in databases_files:
        assert host.file(database_file).exists
        assert host.file(database_file).user == 'root'
        assert host.file(database_file).group == 'root'
        assert host.file(database_file).mode == 0o777
        assert host.file(host.file(database_file).linked_to).user == 'root'
        assert host.file(host.file(database_file).linked_to).group == 'root'
        assert host.file(host.file(database_file).linked_to).mode == 0o440


def test_geoipupdate_configuration(host):
    """
    Check if geoipupdate configuration file exists
    """

    if host.system_info.distribution != 'ubuntu':
        pytest.skip('Not apply to %s' % host.system_info.distribution)

    config_file = '/etc/geoip/geoipupdate.conf'

    assert host.file(config_file).exists
    assert host.file(config_file).is_file
    assert host.file(config_file).user == 'root'
    assert host.file(config_file).group == 'root'
    assert host.file(config_file).mode == 0o640


def test_geoipupdate_databases(host):
    """
    Check if geoipupdate databases exists
    """

    if host.system_info.distribution != 'ubuntu':
        pytest.skip('Not apply to %s' % host.system_info.distribution)

    databases_folder_path = '/usr/share/GeoIP'
    databases_files = [
        '{}/GeoLite2-Country.mmdb'.format(databases_folder_path),
        '{}/GeoLite2-City.mmdb'.format(databases_folder_path),
    ]

    for database_file in databases_files:
        assert host.file(database_file).exists
        assert host.file(database_file).is_file
        assert host.file(database_file).user == 'root'
        assert host.file(database_file).group == 'root'
        assert host.file(database_file).mode == 0o644
