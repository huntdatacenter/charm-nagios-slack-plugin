# nagios-slack plugin

![GitHub Action CI badge](https://github.com/huntdatacenter/charm-nagios-slack-plugin/workflows/ci/badge.svg)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

This subordinate charm enables [Nagios][nagios] to send notifications to [Slack][slack].
The charm is intended to be used with the [`nagios`][nagios-charm] charm.

## Usage

The charm creates a new Nagios contact definition called `slack`.
This contact should be added to the default Nagios contact group.
Here is an example to get going:

```
juju deploy cs:~huntdatacenter/nagios-slack-plugin
juju deploy nagios
juju add-relation nagios:juju-info nagios-slack-plugin:juju-info
juju config nagios contactgroup-members="root,slack"
```

## Development

Here are some helpful commands to get started with development and testing:

```
$ make help
lint                 Run linter
build                Build charm
deploy               Deploy charm
upgrade              Upgrade charm
force-upgrade        Force upgrade charm
test-xenial-bundle   Test Xenial bundle
test-bionic-bundle   Test Bionic bundle
push                 Push charm to stable channel
clean                Clean .tox and build
help                 Show this help
```

## Further information

### Links

- [Nagios charm][nagios-charm]
- [Nagios Standard Macros documentation][nagios-macros]

### Attribution

This project is based on modifications of the following projects:

- [Nagios2Slack][nagios2slack]
- [Nagios-Slack-Notifications][nagios-slack-notifications]

### License

Copyright (C) 2017 Runlevel Consulting Ltd.

Copyright (C) 2018-2019 Øystein Baarnes

Copyright (C) 2020 Norges teknisk-naturvitenskapelige universitet

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

[nagios]: https://www.nagios.com
[nagios-macros]: https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/3/en/macrolist.html
[nagios2slack]: https://github.com/obaarne/Nagios2Slack
[nagios-slack-notifications]: https://github.com/RunlevelConsulting/Nagios-Slack-Notifications
[slack]: https://slack.com
[nagios-charm]: https://jaas.ai/nagios
