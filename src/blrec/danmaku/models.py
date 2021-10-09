from typing import Literal

import attr


@attr.s(auto_attribs=True, slots=True, frozen=True)
class Metadata:
    user_name: str
    room_id: int
    room_title: str
    area: str
    parent_area: str
    live_start_time: int  # seconds
    record_start_time: int  # seconds
    recorder: str


@attr.s(auto_attribs=True, slots=True, frozen=True)
class Danmu:
    stime: float
    mode: int
    size: int
    color: int
    date: int  # milliseconds
    pool: int
    uid_hash: str
    uid: int
    uname: str
    dmid: int
    text: str


@attr.s(auto_attribs=True, slots=True, frozen=True)
class GiftSendRecord:
    ts: float
    uid: int
    user: str
    giftname: str
    giftcount: int
    cointype: Literal['sliver', 'gold']
    price: int


@attr.s(auto_attribs=True, slots=True, frozen=True)
class GuardBuyRecord:
    ts: float
    uid: int
    user: str
    giftname: str
    count: int
    price: int
    level: int


@attr.s(auto_attribs=True, slots=True, frozen=True)
class SuperChatRecord:
    ts: float
    uid: int
    user: str
    price: int
    time: int
    message: str
