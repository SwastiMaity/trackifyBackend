#!/bin/bash
# Script to run FastAPI app and expose via ngrok
# Requires ngrok to be installed and authtoken configured

/workspaces/trackifyBackend/.venv/bin/uvicorn main:app --host 127.0.0.1 --port 8000 &
UVICORN_PID=$!

ngrok http 8000

kill $UVICORN_PID
