import requests

headers = {
    'Content-type': 'application/json',
}

json_data = {
    'text': 'Hello, World!',
}

response = requests.post(
    'https://hooks.slack.com/services/T083FE6JLQJ/B083FGC5CCS/{os.environ.get("SLACK_ID")}',
    headers=headers,
    json=json_data,
)
