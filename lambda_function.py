import json
import requests

def lambda_handler(event, context):
    response = requests.get("https://api.github.com")
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Hello from Lambda!',
            'github_status': response.status_code
        })
    }
