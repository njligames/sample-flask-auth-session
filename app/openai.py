# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
import openai
import json

class OpenAI():
    openai.api_key = os.getenv("OPENAI_API_KEY")

    def __init__(self, disposition, setup, key = os.getenv("OPENAI_API_KEY")):
        self.disposition = disposition
        self.setup = setup
        openai.api_key = key

    def request(self, disposition, setup, requestString):
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

    def setDisposition(self, disposition):
        self.disposition = disposition

    def setSetup(self, disposition):
        self.setup = setup

    def rewordRequest(self, requestString):
        return self.request(self.disposition, self.setup, requestString)

