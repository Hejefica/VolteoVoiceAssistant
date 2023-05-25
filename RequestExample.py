import requests
import json

OPENAI_API_KEY = "Bearer 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"

headers = {
    "Content-Type": "application/json",
    "Authorization": OPENAI_API_KEY,
}

data = {
    "model": "text-davinci-003",
    "prompt": "Hola ChatGPT, quien es mejor? Messi o Ronaldo?",
    "temperature": 0.7,
    "max_tokens": 256,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
}

response = requests.post("https://api.openai.com/v1/completions", headers=headers, data=json.dumps(data))
response_json = response.json()
text = response_json["choices"][0]["text"]

# Aquí puedes hacer lo que necesites con la respuesta
print(text)