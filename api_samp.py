import requests

api_key='AIzaSyCHL4GqaB_lqSkVSIhyZZTeIagVj73npPA'
api_url=f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

prompt=input('enter prompt to AI: ')

payload = {
    'contents':[
        {'role':'user','parts':[{'text':prompt}]}
    ]
}

response = requests.post(api_url,json=payload)

if response.status_code == 200:
    data = response.json()
    try:
        reply = data['candidates'][0]['content']['parts'][0]['text']
        print("Gemini:",reply)
    except (KeyError,IndexError):
        print("Unexpected format response")
        print(data)
else:
    print(response.status_code,response.text)