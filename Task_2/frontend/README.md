# Task Manager Frontend

A simple frontend application for managing tasks through a REST API.

The app allows you to:
- View a list of tasks
- Create new tasks
- Toggle task status
- Delete tasks

## 📦 Requirements

- Any modern web browser (Chrome, Firefox, Edge, Safari)
- A running backend API that exposes endpoints under `/api/tasks`

## ️⚙️ Environment Variables

The app uses one environment variable for API connectivity:

- **`API_URL`** – Base URL of the backend API (e.g. `http://localhost:5000`).

## 📦 API Endpoints

The frontend expects the backend API to expose the following endpoints:
- `GET /api/tasks` → Get list of tasks
- `POST /api/tasks` → Create a new task (expects `title`, `description`, `status`)
- `PATCH /api/tasks/:id` → Toggle task status
- `DELETE /api/tasks/:id` → Delete task by ID

## 🏃‍ Usage

- Start your backend API (Flask, FastAPI, etc.).
- Update app.js with your backend URL:
  ```js
  const API_URL = "http://localhost:5000";
  ```
- Open index.html in your browser.
- Use the form to create new tasks and manage them.

### Example

- Create a new task by filling out the form.
- Click `Toggle` to cycle task status (backend implementation required).
- Click `Delete` to remove a task.

## 🧪 Running Tests

At this point, only linter is implemented.

Code contains config file for `ESLint`. Install it via `npm` and apply to the code
directory.
