from flask import Flask
from flask import request
from service import ToDoService

app = Flask(__name__)


@app.route('/todo/', methods=["POST"])
def create_todo():
    result = ToDoService().create(request.get_json)
    return result.to_json()


@app.route('/todo/done/<todo_id>', methods=["PUT"])
def done_to_do(to_do_id):
    result = ToDoService().done(to_do_id)
    return result.to_json()


@app.route('todo/undone', methods=["GET"])
def get_undone_to_dos():
    result = ToDoService().get_undone()
    return result


if __name__ == '__main__':
    app.run()
