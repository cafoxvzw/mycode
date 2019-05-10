#!/usr/bin/python3

ANSIBLE_METADATA = {
        'metadata_version': '1.1',
        'status': ['preview'],
        'supportedby': 'community'
        }

DOCUMENTATION = '''
---
module: my_net_test_module

'''

RETURN = '''
original_message:
    description: The original name that was passed in
    type: str
message:
    description: The output message that the sample module generates
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
            name=dict(type='str', required=True),
            new=dict(type='bool', required=False, default=False)
    )

    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        return result

    result['original_message'] = module.params['name']
    result['message'] = "Welcome to class, " + module.params['name']

    if module.params['new']:
        result['changed'] = True

    if module.params['name'] == 'fail me':
        module.fail_json(msg='You requested this to fail', **result) # the ** breaks results list into values

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()


