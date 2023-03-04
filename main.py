import openai
from decouple import config


def chatwithme(value):

    API_KEY=config('API_KEY')
    openai.api_key=API_KEY
    model_engine='text-davinci-003'
    input1 = input()
    prompt = " give me selenium python code to "+input1+""

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completion.choices[0].text
    print(response)
chatwithme(123)