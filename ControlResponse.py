import dataclasses


@dataclasses.dataclass
class ControlResponse:
    def __init__(self, executedCommand: str, success: bool):
        self.executedCommand = executedCommand
        self.success = success

    def to_dict(self):
        return {
            "executedCommand": self.executedCommand,
            "success": self.success
        }
