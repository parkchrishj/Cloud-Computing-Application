import requests
import json
url = "https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp3-grader-partial"
payload = {
            "accountId": '036025816517',
            "submitterEmail": 'hpark102@illinois.edu',
            "secret": 'TazkQjQHTgw819FI',
            "ipaddress": '35.168.8.134:5000'
    }
r = requests.post(url, data=json.dumps(payload))
print(r.status_code, r.reason)
print(r.text)
