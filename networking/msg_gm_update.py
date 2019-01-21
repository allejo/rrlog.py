from typing import Optional

from networking.game_data_shot import ShotData
from networking.game_packet import GamePacket
from networking.packet import Packet


class MsgGMUpdatePacket(GamePacket):
    __slots__ = (
        'target',
        'shot',
    )

    def __init__(self):
        super().__init__()

        self.type: str = 'MsgGMUpdate'
        self.target: int = -1
        self.shot: Optional[ShotData] = None

    def _unpack(self):
        self.target = Packet.unpack_uint8(self.buffer)
        self.shot = Packet.unpack_shot(self.buffer)
