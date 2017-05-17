"""
Role tests
"""

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_packages(host):
    """
    Check if packages are installed
    """

    packages = []

    if host.system_info.distribution == 'debian':
        packages = [
            'geoip-database',
            'geoip-bin',
        ]
    elif host.system_info.distribution == 'ubuntu':
        packages = [
            'geoip-database',
            'geoip-bin',
            'geoipupdate',
        ]

    for package in packages:
        assert host.package(package).is_installed


def test_databases_download(host):
    """
    Check if databases downloaded files exists
    """

    databases_folder_path = ''

    if host.system_info.distribution in ('debian', 'ubuntu'):
        databases_folder_path = '/usr/share/GeoIP'

    databases_files = [
        '{}/GeoLite2-ASN.mmdb'.format(databases_folder_path),
        '{}/GeoLite2-City.mmdb'.format(databases_folder_path),
        '{}/GeoLite2-Country.mmdb'.format(databases_folder_path),
    ]

    for database_file in databases_files:
        assert host.file(database_file).exists
        assert host.file(database_file).is_symlink
        assert host.file(database_file).user == 'root'
        assert host.file(database_file).group == 'root'
        assert host.file(database_file).mode == 0o777
        assert host.file(host.file(database_file).linked_to).user == 'root'
        assert host.file(host.file(database_file).linked_to).group == 'root'
        assert host.file(host.file(database_file).linked_to).mode == 0o440
