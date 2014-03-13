## Ansibles - hostname [![Build Status](https://travis-ci.org/Ansibles/hostname.png)](https://travis-ci.org/Ansibles/hostname)

Ansible role that sets the hostname and FQDN of the node.


#### Variables

This completely depends on your host inventory. Add the hosts to your inventory with their fqdn (e.g. foo.bar.com), and the role will take care of setting your hostname accordingly (hostname: foo, fqdn: foo.bar.com). If you just name it with the hostname in the inventory, it will similarly work (hostname set, but no fqdn attached to it).


#### License

Licensed under the MIT License. See the LICENSE file for details.


#### Feedback, bug-reports, requests, ...

Are [welcome](https://github.com/ansibles/hostname/issues)!
