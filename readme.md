1. Overview

One-Tap SOS is a lightweight, beginner-friendly disaster management tool that enables victims to send instant help alerts with their location during floods, earthquakes, or network outages.

Victims press one button → location is logged in backend.

Rescuers see alerts on a live map dashboard.

If internet is weak, an SMS/WhatsApp fallback lets victims still share location.

⚡ Built in just 3 hours by 6 members during a hackathon.

2. Problem Statement

Disasters often knock out internet and power, leaving victims unable to communicate.
Rescue teams waste precious time searching blind, causing avoidable loss of life.

3. Solution

📍 One-Tap SOS Button → shares live location to backend.

🗺️ Responder Dashboard → real-time map showing victims’ alerts.

📩 SMS/WhatsApp fallback → for low internet connectivity.

✅ Lightweight + Easy → works on any smartphone browser, no login needed.

4. Key Features

Victim View:

Big red SOS button.

Captures geolocation using browser API.

Sends to backend (/sos endpoint).

Generates SMS/WhatsApp deep link with coordinates.

Responder View:

Map dashboard (Leaflet.js).

Auto-refresh every 5 seconds.

Displays markers for each alert with timestamp.

Backend:

FastAPI + SQLite for lightweight storage.

/sos → POST endpoint to store alerts.

/alerts → GET endpoint to fetch alerts.

5. Tech Stack
Frontend

HTML, CSS, JavaScript

Leaflet.js (map visualization)

Geolocation API (get victim location)

Backend

Python + FastAPI

SQLite (simple DB for SOS logs)

SQLAlchemy ORM

CORS Middleware for API access

Optional Enhancements

PWA (Progressive Web App) for offline caching

SMS gateway (Twilio, Vonage) — optional if allowed

Free hosting: Replit / Render / Heroku

Frontend (Victim)

Open victim.html in browser.

Click SOS → sends location.

Copy SMS/WhatsApp link if needed.

Frontend (Responder)

Open responder.html in browser.

Map auto-refreshes with victim locations.

8. Roles & Learning Goals

Backend Lead → FastAPI, SQLite, API endpoints.

Victim Frontend → HTML, Geolocation, fetch API.

Responder Map → Leaflet.js, AJAX.

UI/UX → CSS polish, optional PWA.

QA → ngrok testing, integration.

Pitch Lead → Deck + presentation.

9. Demo Flow

Victim clicks SOS → alert stored.

Responder dashboard shows red marker.

SMS fallback works on low internet.

Judges see live demo on two screens.

10. Future Scope

🔔 Push notifications to responders.

🏥 Integration with hospitals/NGOs.

📡 Offline mesh networks.

🌍 Open-source toolkit for communities.
