# maxmind-geoip

[![Build Status](https://travis-ci.org/Temelio/ansible-role-maxmind-geoip.svg?branch=master)](https://travis-ci.org/Temelio/ansible-role-maxmind-geoip)

Install maxmind-geoip package.

## Requirements

This role requires Ansible 2.0 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Locally, you can run tests on Docker (default driver) or Vagrant.
Travis run tests using Docker driver only.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Trusty
- Ubuntu Xenial

and use:
- Ansible 2.0.x
- Ansible 2.1.x
- Ansible 2.2.x
- Ansible 2.3.x

### Running tests

#### Using Docker driver

```
$ tox
```

#### Using Vagrant driver

```
$ MOLECULE_DRIVER=vagrant tox
```

## Role Variables

### Default role variables

``` yaml
# Defaults vars file for maxmind-geoip role
#------------------------------------------------------------------------------

# Packages management
maxmind_geoip_packages: "{{ _maxmind_geoip_packages }}"
maxmind_geoip_package_cache_valid_time: 3600

# Files management
maxmind_geoip_files_owner: 'root'
maxmind_geoip_files_group: 'root'
maxmind_geoip_files_mode: 'u-w,g-w,o-rwx'


# Databases updates management
#------------------------------------------------------------------------------

# General
maxmind_geoip_update_databases_without_geoipupdate: True

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
  dest_folder_path: "{{ _maxmind_geoip_databases_folder }}"
  extension: '.mmdb'
```

## Dependencies

None

## Example Playbook

    - hosts: servers
      roles:
         - { role: Temelio.maxmind-geoip }

## License

MIT

## Author Information

Alexandre Chaussier (for Temelio company)
- http://www.temelio.com
- alexandre.chaussier [at] temelio.com

