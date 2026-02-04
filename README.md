# Task Manager — Dockerized Full-Stack Application

**This is a full-stack Flask + Nginx task manager application, fully containerized with support for production and dev
modes, CI/CD, security, and robust initialization.**

## System requirements

- `Docker 20.10+`
- `Docker Compose v2.10+`

## Quick start (Production)

- Copy .env with the command `cp .env.example .env`.
- Run the application with the command `docker compose --profile prod up -d`.
- Open in browser `http://localhost:8081`.

### After starting the application:

- Table `task` already exists.
- `CRUD` works (creating, editing, deleting tasks).
- All data is saved between restarts.

## Quick start (Develop)

- Copy .env with the command `cp .env.example .env`.
- Run the application with the command `docker compose --profile dev up -d`.
- Open in browser `http://localhost:8081`.

### Benefits of dev mode after launch:

- `Backend`: Changes in `.py` files -> automatic reload of `Flask` ​​(`FLASK_DEBUG=1`).
- `Frontend`: changes in `index.html`, `app.js`, `style.css` -> instant update without rebuilding.
- `MySQL/Redis`: work the same as in `production`.

> There is no need to rebuild images - everything is updated on the fly.

## Features of the project implementation

### Networks

- All services operate in an isolated `app-network` and communicate by name:
    - mysql
    - redis
    - redis-persist
    - backend
    - backend-dev
    - frontend
    - frontend-dev

### Initializing the database

#### The `MySQL` init script is used via the `docker-entrypoint-initdb.d` mechanism:

- On first launch the following are created:
    - Database `tasks_db`.
    - User `appuser` with password `secretpass`.
    - `task` table.
- The backend does not depend on `db.create_all()` - the schema is fixed as a delivery artifact.
- File: `mysql/init/01-init.sql`.

### Redis Persistence

#### Two modes are supported:

- **Ephemeral Redis** (default): Data is lost on restart.
- **Persistent Redis:** data is stored in a named volume.
    - Starting persistent mode: `docker compose --profile redis-persistent --profile prod up -d`.

### Nginx: Reverse Proxy, SPA Fallback & Security

#### SPA Fallback

- The config contains:

```
   location / {
    try_files $uri $uri/ /index.html;
}
```

- When requesting any path (e.g. `/tasks/123`), Nginx first tries to find a physical file with that name (`$uri`).
- If the file does not exist, it checks whether the path is a directory (`$uri/`).
- If there is no directory, it returns `index.html`.

> Note: `location /api/*` has higher priority than `location /`, so requests will never fallback to `index.html`.

#### Exception /api/*

```
location /api/ {
    proxy_pass http://backend:5000;
}
```

- Takes precedence over `location /`.
- All requests to `/api/...` are proxied to the `backend`, rather than being replaced by `index.html`.

#### Security Headers

- Added basic security headers:

```
add_header X-Content-Type-Options "nosniff" always;
add_header X-Frame-Options "DENY" always;
add_header Referrer-Policy "no-referrer" always;
```

- `X-Content-Type-Options`: nosniff - Prevents MIME sniffing (XSS).
- `X-Frame-Options: DENY` - protects against clickjacking.
- `Referrer Policy`: no-referrer - increases privacy.

> Note: `X-Frame-Options: DENY`
> This is selected because the app does not use and does not plan to use `iframe` embedding. This provides maximum
> protection against `clickjacking attacks` without adding unnecessary complexity. The `SAMEORIGIN` option is not required
> since there are no internal `iframes` or `embed scripts`.

### CI Pipeline

The pipeline in `.github/workflows/ci.yml` includes:

- Linting:
    - Backend: `flake8`, `isort`, `black`.
    - Frontend: `eslint`.
- Tests: `pytest` (unit tests).
- Build: `Multi-stage` Docker images.
- Security Scan: `Trivy` (crashes on `HIGH/CRITICAL` vulnerabilities).
