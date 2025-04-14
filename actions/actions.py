# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

import openai
from anthropic import Anthropic
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import os
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)


class ActionDefaultClaudeResponse(Action):
    load_dotenv()

    def name(self) -> str:
        return "action_ask_claude"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        api_key = os.getenv("CLAUDE_API_KEY")

        user_message = tracker.latest_message.get("text")

        client = Anthropic(api_key=api_key)
        try:
            response = client.messages.create(
                model="claude-3-opus-20240229",
                messages=[
                    {"role": "system", "content": "You are an expert on Finance topics. Summarize the response in under 300 words:"},
                    {"role": "user", "content": user_message}
                ],
                max_tokens=350
            )
            response_dict = response.model_dump()

            claude_reply = response_dict["choices"][0]["message"]["content"]

            dispatcher.utter_message(text=claude_reply)

        except Exception as e:
            error_message = f"Error: {e}"
            logger.error(error_message)
            dispatcher.utter_message(
                text="I'm sorry, I couldn't fetch an answer at the moment. Please try again later."
            )
            print(f"Error: {e}")

        return []
