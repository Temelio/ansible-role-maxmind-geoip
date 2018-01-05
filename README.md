# maxmind-geoip

[![Build Status](https://travis-ci.org/Temelio/ansible-role-maxmind-geoip.svg?branch=master)](https://travis-ci.org/Temelio/ansible-role-maxmind-geoip)

Install maxmind-geoip package.

> "geoipupdate" is managed only for Ubuntu via ppa today

## Requirements

This role requires Ansible 2.2 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Trusty
- Ubuntu Xenial

and use:
- Ansible 2.2.x
- Ansible 2.3.x
- Ansible 2.4.x

### Running tests

#### Using Docker driver

```
$ tox
```

## Role Variables

### Default role variables

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

# With geoipupdate
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

_maxmind_geoip_geoipupdate_managed: False

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

Alexandre Chaussier (for Temelio company)
- http://www.temelio.com
- alexandre.chaussier [at] temelio.com
