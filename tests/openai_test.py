import os
import openai
import json
openai.api_key = os.getenv("OPENAI_API_KEY")

def openAIRequest(disposition, setup, requestString):
    prompt = f"I would like for you to read my request text and then return it as a json object where the response text's key is response_value in  html format. Here is the actual request text: {requestString}"

    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": disposition},
        {"role": "system", "content": setup},
        {"role": "user", "content": requestString}
      ]
    )
    x = str(completion.choices[0].message)
    y = json.loads(x)
    response_value = y["content"]
    return response_value

def rewordRequest(rewordString):
    disposition = "You are a Computer Science Ph.D. candidate, who is trying to be informal."
    setup = "You will be given text that could possibly garbled and filled with grammer errors. You need to reword it so that it makes sense."
    requestString = f"please reword this text: {rewordString}"
    return openAIRequest(disposition, setup, requestString)


response_value = rewordRequest("When you have time before the 29th Can you please put a 2024 ticket button like we had for day of cash bash  back on the site. ")
print(response_value)
