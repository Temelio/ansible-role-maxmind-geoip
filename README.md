# maxmind-geoip

[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/travis/Temelio/ansible-role-maxmind-geoip/master.svg?label=travis_master)](https://travis-ci.org/Temelio/ansible-role-maxmind-geoip)
[![Build Status](https://img.shields.io/travis/Temelio/ansible-role-maxmind-geoip/develop.svg?label=travis_develop)](https://travis-ci.org/Temelio/ansible-role-maxmind-geoip)
[![Updates](https://pyup.io/repos/github/Temelio/ansible-role-maxmind-geoip/shield.svg)](https://pyup.io/repos/github/Temelio/ansible-role-maxmind-geoip/)
[![Python 3](https://pyup.io/repos/github/Temelio/ansible-role-maxmind-geoip/python-3-shield.svg)](https://pyup.io/repos/github/Temelio/ansible-role-maxmind-geoip/)
[![Ansible Role](https://img.shields.io/ansible/role/17662.svg)](https://galaxy.ansible.com/Temelio/maxmind-geoip/)
[![GitHub tag](https://img.shields.io/github/tag/temelio/ansible-role-maxmind-geoip.svg)](https://github.com/Temelio/ansible-role-maxmind-geoip/tags)

Install maxmind-geoip2 package.

## Requirements

This role requires Ansible 2.4 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- Debian Stretch
- Ubuntu Trusty
- Ubuntu Xenial
- Ubuntu Bionic

and use:
- Ansible 2.4.x
- Ansible 2.5.x
- Ansible 2.6.x
- Ansible 2.7.x

### Running tests

#### Using Docker driver

```
$ tox
```

## Role Variables

### Default role variables

> If you use this role with geoipupdate < 2.5, set **maxmind_geoip_geoipupdate_legacy_version** to True
> If you download legacy databases (not managed by geoipupdate since 2018 April 1st), set **maxmind_geoip_databases.legacy** to True.

``` yaml
# Defaults vars file for maxmind-geoip role
#------------------------------------------------------------------------------

# Packages management
maxmind_geoip_packages: "{{ _maxmind_geoip_packages }}"
maxmind_geoip_package_cache_valid_time: 3600
maxmind_geoip_repositories: "{{ _maxmind_geoip_repositories | default([]) }}"
maxmind_geoip_system_prerequisites: "{{ _maxmind_geoip_system_prerequisites | default([]) }}"

# Files management
maxmind_geoip_files_owner: 'root'
maxmind_geoip_files_group: 'root'
maxmind_geoip_files_mode: 'u-w,g-w,o-rwx'


# Databases updates management
#------------------------------------------------------------------------------

# General
maxmind_geoip_databases_folder: "{{ _maxmind_geoip_databases_folder | default('/usr/share/GeoIP') }}"
maxmind_geoip_update_databases: True
maxmind_geoip_update_databases_with_geoipupdate: True

# Without geoipupdate
maxmind_geoip_archives:
  base_url: 'http://geolite.maxmind.com/download/geoip/database/'
  download_folder_path: '/tmp/'
  files_names:
    - 'GeoLite2-ASN.tar.gz'
    - 'GeoLite2-City.tar.gz'
    - 'GeoLite2-Country.tar.gz'
  force_unarchive: False
  timeout: 30
maxmind_geoip_databases:
  dest_folder_path: "{{ maxmind_geoip_databases_folder }}"
  extension: '.mmdb'
  legacy: False

# With geoipupdate
maxmind_geoip_geoipupdate_legacy_version: False
maxmind_geoip_geoipupdate_managed: "{{ _maxmind_geoip_geoipupdate_managed }}"
maxmind_geoip_geoipupdate_changed_when: omit
maxmind_geoip_geoipupdate_host: 'updates.maxmind.com'
maxmind_geoip_geoipupdate_protocol: 'https'
maxmind_geoip_geoipupdate_proxy: ''
maxmind_geoip_geoipupdate_proxy_user_password: ''
maxmind_geoip_geoipupdate_skip_peer_verification: 0
maxmind_geoip_geoipupdate_skip_hostname_verification: 0
maxmind_geoip_geoipupdate_user_id: 999999
maxmind_geoip_geoipupdate_license_key: '000000000000'
maxmind_geoip_geoipupdate_product_ids:
  - 'GeoLite2-City'
  - 'GeoLite2-Country'
  - 'GeoLite-Legacy-IPv6-City'
  - 'GeoLite-Legacy-IPv6-Country'
  - 506
  - 517
  - 533
maxmind_geoip_configuration_folder_path: "{{ _maxmind_geoip_configuration_folder_path }}"
```

### Specific Debian OS family variables

``` yaml
# Debian family variables
#------------------------------------------------------------------------------

_maxmind_geoip_system_prerequisites:
  - name: 'ca-certificates'

_maxmind_geoip_databases_folder: '/usr/share/GeoIP/'
_maxmind_geoip_configuration_folder_path: '/etc/geoip/'
```

### Specific Debian distributions variables

``` yaml
# Debian OS variables
#------------------------------------------------------------------------------

_maxmind_geoip_geoipupdate_managed: True

_maxmind_geoip_packages:
  - name: 'geoip-database'
  - name: 'geoip-bin'
```

### Specific Ubuntu distributions variables

``` yaml
# Ubuntu distributions variables
#------------------------------------------------------------------------------

_maxmind_geoip_geoipupdate_managed: True

_maxmind_geoip_packages:
  - name: 'geoip-database'
  - name: 'geoip-bin'
  - name: 'geoipupdate'

_maxmind_geoip_repositories:
  - repo: 'ppa:maxmind/ppa'
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: Temelio.maxmind-geoip }
```

## License

MIT

## Author Information

Alexandre Chaussier, Lise Machetel (for Temelio company)
- http://www.temelio.com
