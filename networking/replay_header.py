from typing import BinaryIO

from networking.packable_interface import PackableInterface
from networking.packet import Packet
from networking.replay_duration import ReplayDuration


class ReplayHeader(PackableInterface):
    CALLSIGN_LEN = 32
    MOTTO_LEN = 128
    SERVER_LEN = 8
    MESSAGE_LEN = 128
    HASH_LEN = 64
    WORLD_SETTING_SIZE = 30

    __slots__ = [
        'magic_number',
        'version',
        'offset',
        'file_time',
        'player',
        'flags_size',
        'world_size',
        'callsign',
        'motto',
        'server_version',
        'app_version',
        'real_hash',
        'length',
    ]

    def __init__(self):
        self.magic_number = -1
        self.version = -1
        self.offset = 0
        self.file_time = 0
        self.player = -1
        self.flags_size = 0
        self.world_size = 0
        self.callsign = ''
        self.motto = ''
        self.server_version = ''
        self.app_version = ''
        self.real_hash = ''
        self.length = None

    def unpack(self, buf: BinaryIO) -> None:
        self.magic_number = Packet.unpack_uint32(buf)
        self.version = Packet.unpack_uint32(buf)
        self.offset = Packet.unpack_uint32(buf)
        self.file_time = Packet.unpack_int64(buf)
        self.player = Packet.unpack_uint32(buf)
        self.flags_size = Packet.unpack_uint32(buf)
        self.world_size = Packet.unpack_uint32(buf)
        self.callsign = Packet.unpack_string(buf, ReplayHeader.CALLSIGN_LEN)
        self.motto = Packet.unpack_string(buf, ReplayHeader.MOTTO_LEN)
        self.server_version = Packet.unpack_string(buf, ReplayHeader.SERVER_LEN)
        self.app_version = Packet.unpack_string(buf, ReplayHeader.MESSAGE_LEN)
        self.real_hash = Packet.unpack_string(buf, ReplayHeader.HASH_LEN)

        self.length = ReplayDuration(self.file_time)

        # Skip the appropriate number of bytes since we're not making use of this
        # data yet

        buf.read(4 + ReplayHeader.WORLD_SETTING_SIZE)

        if self.flags_size > 0:
            buf.read(self.flags_size)

        buf.read(self.world_size)