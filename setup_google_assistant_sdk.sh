#!/bin/sh

#JSON_PATH=$1

#詳しくは以下URLを参照
#https://developers.google.com/assistant/sdk/guides/library/python/embed/run-sample

sudo apt-get update
sudo apt-get install python3-dev python3-venv
#python3 -m venv env
#env/bin/python -m pip install --upgrade pip setuptools wheel
#source env/bin/activate

sudo apt-get install portaudio19-dev libffi-dev libssl-dev libmpg123-dev
python -m pip install --upgrade google-assistant-library
python -m pip install --upgrade google-assistant-sdk[samples]
python -m pip install --upgrade google-auth-oauthlib[tool]


#ここからは手動のほうが良い

#google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype \
#      --scope https://www.googleapis.com/auth/gcm \
#      --save --headless --client-secrets $JSON_PATH
