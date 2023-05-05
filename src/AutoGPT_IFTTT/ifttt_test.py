"""
Test class for IFTTT integration
"""
import os
import unittest

import requests

from . import AutoGPT_IFTTT
from .ifttt import call_webhook


class TestAutoGPT_IFTTT(unittest.TestCase):
    """
    This is the plugin test class for IFTTT Webhooks for Auto-GPT
    """

    def setUp(self):
        os.environ["IFTTT_WEBHOOK_TRIGGER_NAME"] = "TestAutoGPT"
        os.environ["IFTTT_KEY"] = "bTDGYU8MfQ8ZM6zrIoHVyx"
        self.title = "title"
        self.content = "this is content"
        self.summary= "user testing summary"

    def tearDown(self):
        os.environ.pop("IFTTT_WEBHOOK_TRIGGER_NAME", None)
        os.environ.pop("IFTTT_KEY", None)

    def test_call_webhook(self):
        try:
            output = call_webhook(
                title=self.title,
                summary=self.summary,
                content=self.content,
            )
            self.assertEqual(output.status_code, 200)
        except requests.exceptions.HTTPError as e:
            self.assertEqual(e.response.status_code, 401)
            

if __name__ == "__main__":
    unittest.main()
