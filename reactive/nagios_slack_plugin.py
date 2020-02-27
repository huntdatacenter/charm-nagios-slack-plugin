#!/usr/bin/env python

from charmhelpers.contrib.ansible import apply_playbook
from charmhelpers.core.hookenv import status_set
from charms.reactive.decorators import hook
from charms.reactive.decorators import when
from charms.reactive.decorators import when_not
from charms.reactive.flags import clear_flag
from charms.reactive.flags import register_trigger
from charms.reactive.flags import set_flag

register_trigger(when='config.changed',
                 clear_flag='plugin.configured')


@when_not('config.set.slack_webhook_url')
def require_webhook():
    status_set('blocked', 'slack_webhook_url must be set')


@when('config.set.slack_webhook_url')
@when_not('plugin.configured')
def configure_plugin():
    status_set('maintenance', 'configuring nagios-slack plugin')
    apply_playbook(playbook='ansible/playbook.yaml')
    status_set('active', 'ready')
    set_flag('plugin.configured')


# Hooks
@hook('stop')
def cleanup():
    apply_playbook(playbook='ansible/playbook.yaml', tags=['uninstall'])


@hook('upgrade-charm')
def upgrade_charm():
    clear_flag('plugin.configured')
