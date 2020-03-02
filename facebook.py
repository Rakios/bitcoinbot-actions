from rasa_core.channels.facebook import FacebookInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import os
from rasa_core.utils import EndpointConfig

# load your trained agent
interpreter = RasaNLUInterpreter("models/nlu/")
MODEL_PATH = "models/dialogue"
action_endpoint = EndpointConfig(url="https://bitcoin25bot-actions.herokuapp.com/webhook")

agent = Agent.load(MODEL_PATH, interpreter=interpreter)

input_channel = FacebookInput(
  fb_verify="prueba_bot",
  # you need tell facebook this token, to confirm your URL
  fb_secret="c0162ecbd77456288d82b02cff91e6ac",  # your app secret
  fb_access_token="EAAB9nZCZArLUYBAH11pEjGhAvJyZB3VPHfZAlwZAEUcEK6p7SFZCFWzgb2Ld6qpXEkCpqjJ68X5aWbiDpjDQiWg5KbZCgAYZB5uWQBULSsEn46SA2PnuLvVF12K8xJFfoJqn5yPxO4QVOhwOMW8ZAZBGMXrtNZBJY7pFhJZBsg4Ij6pp8QZDZD"
  # token for the page you subscribed to
)
# set serve_forever=False if you want to keep the server running
s = agent.handle_channels([input_channel], int(os.environ.get('PORT', 5004)), serve_forever=True)