import boto3
import json
import os
from botocore.exceptions import ClientError
import subprocess


def deploy_stack(stack_name, template_file):
    with open(template_file, 'r') as template:
        template_body = template.read()

        parameters = [
            {
                'ParameterKey': 'SecurityGroup',
                'ParameterValue': 'sg-04b25b88d0a3ba979',
            }
        ]

    cloudformation = boto3.client('cloudformation')

    try:
        # Check if the stack exists
        cloudformation.describe_stacks(StackName=stack_name)
        stack_exists = True
    except ClientError as e:
        if 'does not exist' in str(e):
            stack_exists = False
        else:
            raise e

    if stack_exists:
        # Update the stack
        try:
            response = cloudformation.update_stack(
                StackName=stack_name,
                TemplateBody=template_body,
                Parameters=parameters,
                Capabilities=['CAPABILITY_NAMED_IAM']
            )
            print(f"Updating stack {stack_name} initiated.")
        except ClientError as e:
            if 'No updates are to be performed' in str(e):
                print("No updates are to be performed.")
                return None
            else:
                raise e
    else:
        # Create the stack
        response = cloudformation.create_stack(
            StackName=stack_name,
            TemplateBody=template_body,
            Parameters=parameters,
            Capabilities=['CAPABILITY_NAMED_IAM',
                          'CAPABILITY_NAMED_IAM', 'CAPABILITY_AUTO_EXPAND']
        )
        print(f"Creating stack {stack_name} initiated.")

    # Wait for the stack to be created/updated
    waiter = cloudformation.get_waiter(
        'stack_create_complete' if not stack_exists else 'stack_update_complete')
    waiter.wait(StackName=stack_name)
    print(f"Stack {stack_name} deployment complete")

    return response


def update_inventory(ip_address):
    inventory_content = f"[mysql_servers]\n{ip_address}\n"
    with open('../../ansible-ideahub/inventory/hosts.ini', 'w') as inventory_file:
        inventory_file.write(inventory_content)


if __name__ == "__main__":
    # Adjust paths to be relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_file = os.path.join(script_dir, '../templates/ideahub-api.yml')

    stack_name = "ideahub-api-stack"
    deploy_stack(stack_name, template_file)