import requests
import json
import uuid

url = "https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp2"

payload = {
	"graphApi": 'https://vddk1ckj11.execute-api.us-east-1.amazonaws.com/TestProd', #<post api for storing the graph>,
	"botName": 'jarvis', # <name of your Amazon Lex Bot>, 
	"botAlias":  'jarvispublish', # <alias name given when publishing the bot>,
	"identityPoolId": 'us-east-1:212702ad-0e4f-47ca-92de-478b56f7e924',
	"accountId": '606663771088', #<your aws account id used for accessing lex>,
	"submitterEmail": 'hpark102@illinois.edu',
	"secret": 'uEqglDP3inGXwXFm',# <insert your secret token from coursera>,
	#"region": 'us-east-1', #<Region where your lex is deployed (Ex: us-east-1)>
    }

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)