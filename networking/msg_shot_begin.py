from typing import Optional

from networking.game_data_firing_info import FiringInfoData
from networking.game_packet import GamePacket
from networking.packet import Packet


class MsgShotBeginPacket(GamePacket):
    __slots__ = (
        'firing_info',
    )

    def __init__(self):
        super().__init__()

        self.type: str = 'MsgShotBegin'
        self.firing_info: Optional[FiringInfoData] = None

    def _unpack(self):
        self.firing_info = Packet.unpack_firing_info(self.buffer)
