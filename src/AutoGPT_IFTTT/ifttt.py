"""This is a plugin to IFTTT Webhooks for Auto-GPT"""
from pprint import pprint
import requests
import os


"""
Creates a new Webhook call to IFTTT

Parameters:
    - title: The title of the page.
    - summary: A brief summary of the page.
    - content: The content of the page.

Returns:
    - If the page is created successfully, returns a string indicating the success
        and the URL of the newly created page.
    - If there is an error during the creation process, returns the error message.
"""


def call_webhook(title: str, summary: str , content: str):
    triggerName = os.getenv("IFTTT_WEBHOOK_TRIGGER_NAME")
    key = os.getenv("IFTTT_KEY")

    url = "https://maker.ifttt.com/trigger/" + triggerName
    url += "/json/with/key/" + key
    headers = {
        "content-type": "application/json",
    }

    payload = {
        "data": [
            {
                "title": title,
                "summary": summary,
                "content": content,
            },
        ]
    }

    response = requests.post(url, headers=headers, json=payload, timeout=60)
    return response
