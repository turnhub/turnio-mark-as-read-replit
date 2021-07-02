from flask import Flask, request
import os
import requests

app = Flask('app')

# Repl provides these environment variables, we use it
# to construct the URL that this repl will be accessible on.
repl_owner = os.environ.get("REPL_OWNER")
repl_slug = os.environ.get("REPL_SLUG")
repl_url = f'https://{repl_slug}.{repl_owner.lower()}.repl.co'

TOKEN = os.environ.get("TOKEN")
HOST = os.environ.get("HOST", "https://whatsapp.turn.io")

@app.route('/')
def hello_world():
  return f'The Turn UI integration API endpoint is at {repl_url}/mark-read'

@app.route('/mark-read', methods=['POST'])
def mark_read():
  json = request.json
  if 'messages' not in json:
    return ''
  
  [message] = json["messages"]
  message_id = message["id"]

  put_response = requests.put(f"{HOST}/v1/messages/{message_id}", 
    headers={
      "Authorization": f"Bearer {TOKEN}",
    },
    json={
      "status": "read"
    })
  print(put_response.text)

  return ''

app.run(host='0.0.0.0', port=8080)
