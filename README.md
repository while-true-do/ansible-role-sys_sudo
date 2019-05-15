<!--
name: README.md
description: This file contains important information for the repository.
author: while-true-do.io
contact: hello@while-true-do.io
license: BSD-3-Clause
-->

<!-- github shields -->
[![Github (tag)](https://img.shields.io/github/tag/while-true-do/ansible-role-sys_sudo.svg)](https://github.com/while-true-do/ansible-role-sys_sudo/tags)
[![Github (license)](https://img.shields.io/github/license/while-true-do/ansible-role-sys_sudo.svg)](https://github.com/while-true-do/ansible-role-sys_sudo/blob/master/LICENSE)
[![Github (issues)](https://img.shields.io/github/issues/while-true-do/ansible-role-sys_sudo.svg)](https://github.com/while-true-do/ansible-role-sys_sudo/issues)
[![Github (pull requests)](https://img.shields.io/github/issues-pr/while-true-do/ansible-role-sys_sudo.svg)](https://github.com/while-true-do/ansible-role-sys_sudo/pulls)
<!-- travis shields -->
[![Travis (com)](https://img.shields.io/travis/com/while-true-do/ansible-role-sys_sudo.svg)](https://travis-ci.com/while-true-do/ansible-role-sys_sudo)
<!-- ansible shields -->
[![Ansible (min. version)](https://img.shields.io/badge/dynamic/yaml.svg?label=Min.%20Ansible%20Version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-sys_sudo%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.min_ansible_version&colorB=black)](https://galaxy.ansible.com/while_true_do/sys_sudo)
[![Ansible (platforms)](https://img.shields.io/badge/dynamic/yaml.svg?label=Supported%20OS&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-sys_sudo%2Fmaster%2Fmeta%2Fmain.yml&query=galaxy_info.platforms%5B*%5D.name&colorB=black)](https://galaxy.ansible.com/while_true_do/sys_sudo)
[![Ansible (tags)](https://img.shields.io/badge/dynamic/yaml.svg?label=Galaxy%20Tags&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-sys_sudo%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.galaxy_tags%5B*%5D&colorB=black)](https://galaxy.ansible.com/while_true_do/sys_sudo)

# Ansible Role: sys_sudo

An Ansible Role to configure sudo and sudoers files.

## Motivation

[sudo](https://www.sudo.ws) is the most common used command in Linux. Having a
proper configuration is mandatory for most Linux Systems.

## Description

This role will configure sudo properly.

-   configure /etc/sudoers
-   configure /etc/sudoers.d/*

## Requirements

Used Modules:

-   [Ansible Module Package](https://docs.ansible.com/ansible/latest/modules/package_module.html)
-   [Ansible Module Template](https://docs.ansible.com/ansible/latest/modules/template_module.html)

## Installation

Install from [Ansible Galaxy](https://galaxy.ansible.com/while_true_do/sys_sudo)
```
ansible-galaxy install while_true_do.sys_sudo
```

Install from [Github](https://github.com/while-true-do/ansible-role-sys_sudo)
```
git clone https://github.com/while-true-do/ansible-role-sys_sudo.git while_true_do.sys_sudo
```

## Usage

### Role Variables

```
---
# defaults file for while_true_do.sys_sudo

wtd_sys_sudo_package: "sudo"
# State can be present|latest|absent
wtd_sys_sudo_package_state: "present"

# Configure the sudo defaults
wtd_sys_sudo_defaults:
  # Reset environment and use env_keep
  env_reset: true
  # Show asterisks, when typing a password
  pwfeedback: false
  # optional: lecture can be once|always|never
  # lecture: "once"
  # optional: define another lecture message from a file
  # lecture_file: "/path/to/file"

# Configure the wheel group
wtd_sys_sudo_wheel:
  enable: true
  host: "ALL"
  runas: "ALL"
  cmnd: "ALL"
  # optional: use tag PASSWD|NOPASSWD
  # tag: ""

# Configure the root user
wtd_sys_sudo_root:
  host: "ALL"
  runas: "ALL"
  cmnd: "ALL"
  # optional: use tag PASSWD|NOPASSWD
  # tag: ""

# Provide additional sudoers, the way you want them.
#
# All users|groups will be configured in /etc/sudoers.d/
#
# You can use user|group|netgroup, but not all at once.
#
# The result will be a lign like:
# user = (runas) tag: command
#
# Please carefully read the usage section in README.md.
#
# wtd_sys_sudo_sudoers:
#   - name: "myname"
#     user: "myuser"
#     group: "mygroup"
#     netgroup: "mynetgroup"
#     host: "HOST_SPEC"
#     runas: "RUNAS_SPEC"
#     cmnd: "COMMAND"
#     tag: "NOPASSWD|PASSWD"
```

### Example Playbook

Running Ansible
[Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)
can be done in a
[playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html).

#### Simple

Without any parameter given, `/etc/sudoers` will be configured, the way `%wheel`
and `root` are allowed to use the `sudo` command. This is standard in most
Linux Distributions.

```
---
- hosts: all
  roles:
    - role: while_true_do.sys_sudo
```

#### Advanced

Configure wheel, without a password.

```
- hosts: all
  roles:
    - role: while_true_do.sys_sudo
      wtd_sys_sudo_wheel:
        enable: true
        host: "ALL"
        runas: "ALL"
        cmnd: "ALL"
        tag: "NOPASSWD"
```

Configure a web admin group to sudo for specific commands.

```
- hosts: all
  roles:
    - role: while_true_do.sys_sudo
      wtd_sys_sudo_sudoers:
        - name: "webadmin"
          group: "webadmin"
          host: "ALL"
          runas: "ALL"
          cmnd: "/usr/sbin/service httpd *"
```

Configure multiple groups and users.

```
- hosts: all
  roles:
    - role: while_true_do.sys_sudo
      wtd_sys_sudo_sudoers:
        - name: "webadmin"
          group: "webadmin"
          host: "ALL"
          runas: "ALL"
          cmnd: "/usr/sbin/service httpd *"
        - name: "developer"
          user: "developer"
          host: "ALL"
          runas: "ALL"
          cmnd: "cat /var/log/messages"
```

## Known Issues

1.  RedHat Testing is currently not possible in public, due to limitations
    in subscriptions.
2.  Some services and features cannot be tested properly, due to limitations
    in docker.

## Testing

Most of the "generic" tests are located in the
[Test Library](https://github.com/while-true-do/test-library).

Ansible specific testing is done with
[Molecule](https://molecule.readthedocs.io/en/stable/).

Infrastructure testing is done with
[testinfra](https://testinfra.readthedocs.io/en/stable/).

Automated testing is done with [Travis CI](https://travis-ci.com/while-true-do).

## Contribute

Thank you so much for considering to contribute. We are very happy, when somebody
is joining the hard work. Please fell free to open
[Bugs, Feature Requests](https://github.com/while-true-do/ansible-role-sys_sudo/issues)
or [Pull Requests](https://github.com/while-true-do/ansible-role-sys_sudo/pulls) after
reading the [Contribution Guideline](https://github.com/while-true-do/doc-library/blob/master/docs/CONTRIBUTING.md).

See who has contributed already in the [kudos.txt](./kudos.txt).

## License

This work is licensed under a [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

## Contact

-   Site <https://while-true-do.io>
-   Twitter <https://twitter.com/wtd_news>
-   Code <https://github.com/while-true-do>
-   Mail [hello@while-true-do.io](mailto:hello@while-true-do.io)
-   IRC [freenode, #while-true-do](https://webchat.freenode.net/?channels=while-true-do)
-   Telegram <https://t.me/while_true_do>
