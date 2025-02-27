from flask import Blueprint, jsonify

api = Blueprint("api", __name__, url_prefix="/api/v1")


@api.route("/health")
def health():
    return jsonify({"status": "ok"})


@api.route("/todos")
def get_todos():
    return jsonify(
        [
            {
                "id": 1,
                "title": "Watch CSSE6400 Lecture",
                "description": "Watch the lecture on Blackboard",
                "completed": False,
                "deadline_at": "2025-03-01T00:00:00Z",
                "created_at": "2025-02-01T00:00:00Z",
                "updated_at": "2025-02-01T00:00:00Z",
            }
        ]
    )


@api.route("/todos/<int:id>", methods=["GET"])
def get_todo(id):
    return jsonify(
        {
            "id": id,
            "title": "Watch CSSE6400 Lecture",
            "description": "Watch the lecture on Blackboard",
            "completed": False,
            "deadline_at": "2025-03-01T00:00:00Z",
            "created_at": "2025-02-01T00:00:00Z",
            "updated_at": "2025-02-01T00:00:00Z",
        }
    )


@api.route("/todos", methods=["POST"])
def create_todo():
    return (
        jsonify(
            {
                "id": 2,
                "title": "Watch CSSE6400 Lecture 2",
                "description": "Watch the lecture on Blackboard",
                "completed": False,
                "deadline_at": "2025-03-07T00:00:00Z",
                "created_at": "2025-02-01T00:00:00Z",
                "updated_at": "2025-02-01T00:00:00Z",
            }
        ),
        201,
    )


@api.route("/todos/<int:id>", methods=["PUT"])
def update_todo(id):
    return jsonify(
        {
            "id": id,
            "title": "Watch CSSE6400 Lecture",
            "description": "Watch the lecture on Blackboard",
            "completed": True,
            "deadline_at": "2025-03-01T00:00:00Z",
            "created_at": "2025-02-01T00:00:00Z",
            "updated_at": "2025-02-01T00:00:00Z",
        }
    )


@api.route("/todos/<int:id>", methods=["DELETE"])
def delete_todo(id):
    return jsonify(
        {
            "id": id,
            "title": "Watch CSSE6400 Lecture",
            "description": "Watch the lecture on Blackboard",
            "completed": True,
            "deadline_at": "2025-03-01T00:00:00Z",
            "created_at": "2025-02-01T00:00:00Z",
            "updated_at": "2025-02-01T00:00:00Z",
        }
    )
