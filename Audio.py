from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


class Audio:
    def __init__(self):
        self.devices = AudioUtilities.GetSpeakers()
        self.interface = self.devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.volume = self.interface.QueryInterface(IAudioEndpointVolume)

    def change_volume_by(self, amount: float) -> float:
        curr_volume = self.volume.GetMasterVolumeLevel()
        new_volume = curr_volume + amount
        print(f"Changing volume from {curr_volume} to {new_volume}")
        self.volume.SetMasterVolumeLevel(new_volume, None)
        return new_volume
