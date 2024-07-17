import boto3
import os

def validate_template(template_file):
    with open(template_file, 'r') as template:
        template_body = template.read()

    cloudformation = boto3.client('cloudformation')

    try:
        response = cloudformation.validate_template(
            TemplateBody=template_body
        )
        print("Template is valid.")
        print("Template Description:", response.get('Description', 'No description available'))
    except Exception as e:
        print("Template validation failed:")
        print(e)

if __name__ == "__main__":
    # Adjust path to be relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_file = os.path.join(script_dir, '../templates/codepipeline-role.yml')

    validate_template(template_file)
