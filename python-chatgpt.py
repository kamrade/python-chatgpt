# python v.3.9.6
# pip freeze > requirements.txt
# pip install -r requirements.txt

# To use only dependencies involved to the project
# pip install pipreqs
# pipreqs
# pipreqs --force

import requests

api_endpoint = "https://api.openai.com/v1/completions"
api_key = "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"

request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key,

}

request_data = {
    "model": "text-davinci-003",
    "prompt": "Write python script for hello world",
    "max_tokens": 100,
    "temperature": 0.5
}

response = requests.post(api_endpoint, headers=request_headers, json=request_data)
if response.status_code == 200:
    print(response.json())
else:
    print(f"Request failed with status code: {response.status_code}")