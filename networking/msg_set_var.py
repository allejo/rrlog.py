from typing import List

from networking.game_packet import GamePacket
from networking.packet import Packet


class BZDBSetting:
    __slots__ = (
        'name',
        'value',
    )


class MsgSetVarPacket(GamePacket):
    __slots__ = (
        'settings',
    )

    def __init__(self):
        super().__init__()

        self.type: str = 'MsgSetVar'
        self.settings: List[BZDBSetting] = []

    def _unpack(self):
        count: int = Packet.unpack_uint16(self.buffer)

        for i in range(0, count):
            setting: BZDBSetting = BZDBSetting()

            name_len: int = Packet.unpack_uint8(self.buffer)
            setting.name = Packet.unpack_string(self.buffer, name_len)

            value_len: int = Packet.unpack_uint8(self.buffer)
            setting.value = Packet.unpack_string(self.buffer, value_len)

            self.settings.append(setting)