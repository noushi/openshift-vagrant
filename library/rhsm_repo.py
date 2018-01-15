#!/usr/bin/python

#import json
#import pprint
#import jsonpath_rw_ext
import yaml

log = []
#module = None

def debug(msg, *args):
    if module._verbosity >= 3:
        log.append(msg % args)

#def trace(msg, *args):
#    module._verbosity >= 4:
#        log.append(msg % args)

def main():
    global module
    module = AnsibleModule(
        argument_spec=dict(
            state = dict(default='present', choices=['present', 'absent']),
            repos = dict(type='list'),
        ),
        supports_check_mode=True
    )

    state = module.params['state']
    repos = module.params['repos']

    enable = state == 'present'
    if enable:
        action = '--enable='
    else:
        action = '--disable='

    with open("/var/lib/rhsm/cache/content_overrides.json", 'r') as file:
      content_overrides = yaml.load(file)
      enabled_repos = {repo.get('contentLabel', None) for repo in content_overrides if repo.get('contentLabel', None) in repos and repo.get('name', None) == 'enabled'}

    debug(str(enabled_repos))
    args = []
    for repo in repos:
        if enable != (repo in enabled_repos):
            args.append(action + repo)

    debug(' '.join(args))
    #(rc, stdout, stderr) = module.run_command('oc get project ' + name)

    #if (rc == 0) == (state == 'present'):
    #  module.exit_json(changed=False)

    #if state == 'present':
    #  cmd = 'oc new-project --skip-config-write'
    #else:
    #  cmd = 'oc delete-project'

    #args = cmd + ' ' + name
    cmd = []
    if args:
        cmd = ['subscription-manager', 'repos'] + args
        if not module.check_mode:
            module.run_command(cmd, check_rc=True)

    module.exit_json(changed=args, msg=cmd, debug=log)


from ansible.module_utils.basic import *
if __name__ == "__main__":
    main()
