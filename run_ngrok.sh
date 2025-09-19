#!/bin/bash
# Improved script to run FastAPI app and expose via ngrok with a fixed domain
# Requires ngrok authtoken and reserved domain

set -e

FIXED_DOMAIN="olivaceous-bobette-winterless.ngrok-free.app"

echo "Starting FastAPI app on 127.0.0.1:8000..."
/home/swastimaity/Documents/trackifyBackend/venv/bin/uvicorn main:app --host 127.0.0.1 --port 8000 &
UVICORN_PID=$!

sleep 2

echo "Starting ngrok tunnel on fixed domain $FIXED_DOMAIN..."
ngrok http --domain=$FIXED_DOMAIN 8000 > ngrok.log &
NGROK_PID=$!

sleep 3

echo "ngrok tunnel started: https://$FIXED_DOMAIN"

wait $NGROK_PID

echo "Shutting down FastAPI app..."
kill $UVICORN_PID
rm -f ngrok.log
