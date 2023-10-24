import dataclasses

from ControlResponse import ControlResponse


@dataclasses.dataclass
class VolumeResponse(ControlResponse):
    def __init__(self, executedCommand: str, volume: float, success: bool):
        super().__init__(executedCommand, success)
        self.volume = volume

    def to_dict(self):
        return {
            "executedCommand": self.executedCommand,
            "volume": self.volume
        }
