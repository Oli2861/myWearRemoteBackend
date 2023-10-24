import dataclasses


@dataclasses.dataclass
class ControlResponse:
    def __init__(self, executedCommand: str):
        self.executedCommand = executedCommand

    def to_dict(self):
        return {
            "executedCommand": self.executedCommand
        }
