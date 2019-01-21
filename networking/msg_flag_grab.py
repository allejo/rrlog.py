from networking.game_data_flag import FlagData
from networking.game_packet import GamePacket
from networking.packet import Packet


class MsgGrabFlagPacket(GamePacket):
    __slots__ = (
        'player_id',
        'flag',
    )

    def __init__(self):
        super().__init__()

        self.type: str = 'MsgFlagGrab'
        self.player_id: int = -1
        self.flag: FlagData = None

    def _unpack(self):
        self.player_id = Packet.unpack_uint8(self.buffer)
        self.flag = Packet.unpack_flag(self.buffer)
