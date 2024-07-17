import boto3
import sys
import os

def delete_stack(stack_name):
    cloudformation = boto3.client('cloudformation')

    response = cloudformation.delete_stack(
        StackName=stack_name
    )

    print(f"Stack {stack_name} deletion initiated.")
    return response

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python delete.py <stack_name>")
        sys.exit(1)

    stack_name = sys.argv[1]
    delete_stack(stack_name)
