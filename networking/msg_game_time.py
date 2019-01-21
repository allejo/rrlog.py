from networking.game_packet import GamePacket
from networking.packet import Packet


class MsgGameTimePacket(GamePacket):
    __slots__ = (
        'msb',
        'lsb',
    )

    def __init__(self):
        super().__init__()

        self.type: str = 'MsgGameTime'
        self.msb: int = -1
        self.lsb: int = -1

    def _unpack(self):
        self.msb = Packet.unpack_uint32(self.buffer)
        self.lsb = Packet.unpack_uint32(self.buffer)