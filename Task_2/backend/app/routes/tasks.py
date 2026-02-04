from flask import Blueprint, jsonify, request

from ..extensions import cache, db
from ..models import Task

bp = Blueprint("tasks", __name__, url_prefix="/api/tasks")


@bp.route("", methods=["GET"])
@cache.cached(key_prefix="all_tasks")
def list_tasks():
    records = Task.query.order_by(Task.id.asc()).all()
    tasks = [
        {"id": t.id, "title": t.title, "status": t.status, "description": t.description or ""}
        for t in records
    ]
    return jsonify(tasks)


@bp.route("", methods=["POST"])
def upload_tasks():
    title = request.form.get("title")
    description = request.form.get("description")
    status = request.form.get("status")

    if title:
        t = Task(title=title, description=description, status=status or "New")
        db.session.add(t)
        db.session.commit()
        cache.delete("all_tasks")
        return "Success", 200
    return "Title not found", 400


@bp.route("/<int:task_id>", methods=["PATCH"])
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    status_cycle = ["New", "In progress", "Done", "Re-opened"]

    try:
        current_index = status_cycle.index(task.status)
        if current_index == 3:
            task.status = "In progress"
        else:
            next_index = (current_index + 1) % len(status_cycle)
            task.status = status_cycle[next_index]
    except ValueError:
        task.status = "New"  # fallback if status is invalid

    db.session.commit()
    cache.delete("all_tasks")
    return jsonify({"id": task.id, "status": task.status})


@bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    cache.delete("all_tasks")
    return jsonify({"message": f"Task {task_id} deleted"}), 200
