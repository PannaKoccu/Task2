def test_empty_tasks(client):
    rv = client.get("/api/tasks")
    assert rv.status_code == 200
    assert rv.get_json() == []


def test_create_task(client):
    # Send as form data (matches frontend FormData)
    rv = client.post(
        "/api/tasks", data={"title": "Test Task", "description": "Desc", "status": "New"}
    )
    assert rv.status_code == 200

    # Check that the task was created
    rv = client.get("/api/tasks")
    tasks = rv.get_json()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Test Task"
    assert tasks[0]["description"] == "Desc"
    assert tasks[0]["status"] == "New"


def test_toggle_task(client):
    # create task
    client.post("/api/tasks", data={"title": "Toggle Me", "status": "New"})
    rv = client.get("/api/tasks")
    task_id = rv.get_json()[0]["id"]

    # toggle once
    rv = client.patch(f"/api/tasks/{task_id}")
    assert rv.status_code == 200
    assert rv.get_json()["status"] == "In progress"


def test_delete_task(client):
    client.post("/api/tasks", data={"title": "Delete Me", "status": "New"})
    rv = client.get("/api/tasks")
    task_id = rv.get_json()[0]["id"]

    rv = client.delete(f"/api/tasks/{task_id}")
    assert rv.status_code == 200
    assert "deleted" in rv.get_json()["message"]
