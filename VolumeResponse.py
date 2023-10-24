import dataclasses

from ControlResponse import ControlResponse


@dataclasses.dataclass
class VolumeResponse(ControlResponse):
    def __init__(self, executedCommand: str, volume: float):
        super().__init__(executedCommand)
        self.volume = volume

    def to_dict(self):
        return {
            "executedCommand": self.executedCommand,
            "volume": self.volume
        }
