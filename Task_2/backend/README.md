# Flask Task Manager

A simple task management API built with Flask, MySQL, Redis caching, and SQLAlchemy. The app supports full CRUD for
tasks, status toggling, and caching for improved performance.

## ⚙️ Environment Variables

The app relies on environment variables to connect to MySQL, Redis, and frontend host.

| Variable         | Description                                                | Default |
|------------------|------------------------------------------------------------|---------|
| `MYSQL_USER`     | MySQL username                                             | -       |
| `MYSQL_PASSWORD` | MySQL password                                             | -       |
| `MYSQL_HOST`     | MySQL host                                                 | -       |
| `MYSQL_DB`       | MySQL database name                                        | -       |
| `REDIS_HOST`     | Redis host                                                 | `redis` |
| `REDIS_PORT`     | Redis port                                                 | `6379`  |
| `FE_HOST`        | Frontend host for CORS. `hostname:port` or just `hostname` | -       |

## 🏃‍♂️ Running the App

1. Install dependencies:

```shell
pip install -r requirements.txt
```

2. Set environment variables (example for Linux/macOS):

```shell
export MYSQL_USER=root
export MYSQL_PASSWORD=pass
export MYSQL_HOST=localhost
export MYSQL_DB=tasks_db
export REDIS_HOST=localhost
export REDIS_PORT=6379
export FE_HOST=localhost:8080
```

3. Run the app:

```shell
python run.py
```

The API will be available at http://localhost:5000/api/tasks.

## 📦 API Endpoints

| Method | Endpoint          | Description        |
|--------|-------------------|--------------------|
| GET    | `/api/tasks`      | List all tasks     |
| POST   | `/api/tasks`      | Create a new task  |
| PATCH  | `/api/tasks/<id>` | Toggle task status |
| DELETE | `/api/tasks/<id>` | Delete a task      |

## 🧪 Running Tests

### Unit test

The tests use pytest with:

- In-memory SQLite database
- In-memory cache (no Redis required)

Install pytest if not already installed:

```shell
pip install pytest
```

From the project root, run:

```shell
PYTHONPATH=$(pwd) pytest -v
```

All tests will run isolated from MySQL and Redis.

### Linters

Code contains config files for `Flake8`, `isort` and `black` tools. Install them via `pip` and apply to the code
directory.

## ✅ Features

- CRUD API for tasks
- Status toggling: `New → In progress → Done → Re-opened`
- Redis caching with Flask-Caching
- CORS configured for frontend host
- Modular Flask app structure for easier testing and maintenance

## ⚡ Notes

- Ensure MySQL and Redis are running before starting the app.
