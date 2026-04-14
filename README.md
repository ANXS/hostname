## [ANXS](https://github.com/ANXS) - hostname

[![CI Status](https://img.shields.io/github/actions/workflow/status/anxs/hostname/ci.yml)](https://github.com/ANXS/hostname/actions/workflows/ci.yml)
[![Maintenance](https://img.shields.io/maintenance/yes/2026.svg)](https://github.com/ANXS/hostname)
[![Ansible Role](https://img.shields.io/ansible/role/d/anxs/hostname)](https://galaxy.ansible.com/ui/standalone/roles/ANXS/hostname/)
[![License](https://img.shields.io/github/license/ANXS/hostname)](https://github.com/ANXS/hostname/blob/master/LICENSE)

Ansible role that sets the hostname and FQDN of a node based on its inventory name, keeping `/etc/hostname` and `/etc/hosts` in sync for IPv4 and IPv6.

## Requirements & Dependencies

* Ansible 2.12 or higher.
* Ubuntu 20.04+ or Debian 12+.
* Depends on `ANXS.apt` (installed via Galaxy).

## Usage

Add hosts to your inventory with their FQDN (e.g. `foo.bar.com`), and the role will set the short hostname and FQDN accordingly (hostname: `foo`, FQDN: `foo.bar.com`). A bare short name in inventory works too — hostname is set without an attached FQDN.

## Variables

Some commonly adjusted variables. See [`defaults/main.yml`](https://github.com/ANXS/hostname/blob/master/defaults/main.yml) for the full set.

* `hostname_avahi` (default `false`) installs `avahi-daemon` and `libnss-mdns` for mDNS-based name resolution. Useful for Vagrant and LAN discovery.

## Testing

Tests use [Molecule](https://github.com/ansible/molecule) with Docker and [Testinfra](https://testinfra.readthedocs.io/). Run the full suite with `make test`, or target a specific platform (e.g. `make test-ubuntu2404`).

The test suite verifies hostname and `/etc/hostname` are set from inventory, `/etc/hosts` carries correct IPv4 and IPv6 entries, and the legacy `127.0.1.1` Raspberry Pi override is removed when present. Tests run across Ubuntu 20.04/22.04/24.04 and Debian 12.

## Note on AI Usage

This project has been developed with AI assistance. Contributions making use of AI generated content are welcome, however they _must_ be human reviewed prior to submission as pull requests, or issues. All contributors must be able to fully explain and defend any AI generated code, documentation, issues, or tests they submit. Contributions making use of AI must have this explicitly declared in the pull request or issue. This also applies to utilization of AI for reviewing of pull requests.

## Feedback, bug-reports, requests, ...

Are [welcome](https://github.com/ANXS/hostname/issues)!
