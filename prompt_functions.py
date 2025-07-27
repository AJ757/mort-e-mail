import requests
from google import genai
from google.genai import types

api_key='AIzaSyCHL4GqaB_lqSkVSIhyZZTeIagVj73npPA'
api_url=f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

def prompt_ai(prompt:str=None,history=None):
    if history is None:
        history=[]
    if prompt is not None:
        history.append({'role':'user','parts':[{'text':prompt}]})
    
    response = requests.post(api_url,json={'contents':history})

    if response.status_code == 200:
        data = response.json()
        try:
            reply = data['candidates'][0]['content']['parts'][0]['text']
            return reply
        except (KeyError,IndexError):
            return "Unexpected response format"
    else:
        return "Error: "+response.text
    
def add_history(role,text,history=None):
    if history is None:
        history=[]
    if role in ['user','model','system']:
        history.append({'role':role,'parts':[{'text':text}]})
    return history

def prompt_ai_2(user:str=None,system:str=None):
    client=genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user,
        config=types.GenerateContentConfig(system_instruction=system)
    )
    return response.text