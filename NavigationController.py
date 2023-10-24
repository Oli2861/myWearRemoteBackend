from flask import Blueprint, make_response

from CommandExecutor import get_command_provider, Command
from ControlResponse import ControlResponse

navigation = Blueprint("navigation", __name__, url_prefix="/navigation")
command_provider = get_command_provider()


@navigation.route("/left", methods=["PUT"])
def left():
    success = command_provider.execute(Command.LEFT)
    response = ControlResponse("left", success).to_dict()
    return make_response(response, 200)


@navigation.route("/right", methods=["PUT"])
def right():
    success = command_provider.execute(Command.RIGHT)
    response = ControlResponse("right", success).to_dict()
    return make_response(response, 200)


@navigation.route("/up", methods=["PUT"])
def up():
    success = command_provider.execute(Command.UP)
    response = ControlResponse("up", success).to_dict()
    return make_response(response, 200)


@navigation.route("/down", methods=["PUT"])
def down():
    success = command_provider.execute(Command.DOWN)
    response = ControlResponse("down", success).to_dict()
    return make_response(response, 200)


@navigation.route("/select", methods=["PUT"])
def select():
    success = command_provider.execute(Command.SELECT)
    response = ControlResponse("select", success).to_dict()
    return make_response(response, 200)
