#!/bin/sh
envsubst '$API_URL' < /usr/share/nginx/html/app.js > /usr/share/nginx/html/app.js.tmp
mv /usr/share/nginx/html/app.js.tmp /usr/share/nginx/html/app.js
exec "$@"
