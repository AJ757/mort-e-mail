import prompt_functions as P

history=[]
while True:
    prompt = input("\nEnter prompt: ")
    history=P.add_history('user',prompt,history)
    reply = P.prompt_ai(prompt)
    history=P.add_history('model',reply,history)
    print('Gemini :\n',reply)
    if input('Continue chat? y/n: ') in 'Nn':
        break