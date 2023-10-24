from flask import Blueprint, make_response

from Audio import Audio
from CommandExecutor import get_command_provider, CommandExecutor, Command
from ControlResponse import ControlResponse
from VolumeResponse import VolumeResponse

media = Blueprint("media", __name__, url_prefix="/media")
adjustment_amount: float = 2.5

audio_provider: Audio = Audio()
command_provider: CommandExecutor = get_command_provider()


@media.route("/volume-up", methods=["PUT"])
def volume_up():
    new_volume = audio_provider.change_volume_by(adjustment_amount)
    response = VolumeResponse("volume-up", new_volume, success=True).to_dict()
    return make_response(response, 200)


@media.route("/volume-down", methods=["PUT"])
def volume_down():
    new_volume = audio_provider.change_volume_by(-adjustment_amount)
    response = VolumeResponse("volume-down", new_volume, success=True).to_dict()
    return make_response(response, 200)


@media.route("/play", methods=["PUT"])
def play():
    success = command_provider.execute(Command.PLAY)
    response = ControlResponse("play", success).to_dict()
    return make_response(response, 200)


@media.route("/pause", methods=["PUT"])
def pause():
    success = command_provider.execute(Command.PAUSE)
    response = ControlResponse("pause", success).to_dict()
    return make_response(response, 200)


@media.route("/stop", methods=["PUT"])
def stop():
    success = command_provider.execute(Command.STOP)
    response = ControlResponse("stop", success).to_dict()
    return make_response(response, 200)


@media.route("/next", methods=["PUT"])
def next():
    success = command_provider.execute(Command.NEXT)
    response = ControlResponse("next", success).to_dict()
    return make_response(response, 200)


@media.route("/previous", methods=["PUT"])
def previous():
    success = command_provider.execute(Command.PREVIOUS)
    response = ControlResponse("previous", success).to_dict()
    return make_response(response, 200)
