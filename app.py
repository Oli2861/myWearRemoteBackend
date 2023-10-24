import os

from flask import Flask, make_response

from Audio import Audio
from Commands import Commands, WindowsCommands
from ControlResponse import ControlResponse
from VolumeResponse import VolumeResponse

app = Flask(__name__)

adjustment_amount: float = 2.5
audio_provider: Audio = Audio()

command_provider: Commands | None = None
if os.name == "nt":
    command_provider = WindowsCommands()

assert command_provider is not None


@app.route("/volume-up", methods=["PUT"])
def volume_up():
    new_volume = audio_provider.change_volume_by(adjustment_amount)
    response = VolumeResponse("volume-up", new_volume).to_dict()
    return make_response(response, 200)


@app.route("/volume-down", methods=["PUT"])
def volume_down():
    new_volume = audio_provider.change_volume_by(-adjustment_amount)
    response = VolumeResponse("volume-down", new_volume).to_dict()
    return make_response(response, 200)


@app.route("/play", methods=["PUT"])
def play():
    command_provider.play()
    response = ControlResponse("play").to_dict()
    return make_response(response, 200)


@app.route("/pause", methods=["PUT"])
def pause():
    command_provider.pause()
    response = ControlResponse("pause").to_dict()
    return make_response(response, 200)


@app.route("/next", methods=["PUT"])
def next():
    command_provider.next()
    response = ControlResponse("next").to_dict()
    return make_response(response, 200)


@app.route("/previous", methods=["PUT"])
def previous():
    command_provider.previous()
    response = ControlResponse("previous").to_dict()
    return make_response(response, 200)


if __name__ == "__main__":
    app.run(ssl_context=("./res/certificate.crt.pem", "./res/private_key.key.pem"), host="0.0.0.0", port=5000)
