# -*- coding: utf8 -*-

# import std
# import os
import asyncio

# import MCDR and its plugins
# from mcdreforged.api.command import *
from mcdreforged.api.types import ServerInterface
from mcdreforged.api.types import Info
# from ConfigAPI import config

from graia.broadcast import Broadcast
from graia.application import GraiaMiraiApplication
from graia.application.message.elements.internal import Plain
from graia.application.session import Session
from graia.application.message.chain import MessageChain
from graia.application.group import Group, Member
from graia.application.interrupt import InterruptControl
# from graia.application.interrupt.interrupts import GroupMessageInterrupt

# MCDR DATA
PLUGIN_METADATA = {
    'id': 'mirai_chat',
    'version': '1.0.0',
    'name': 'MiraiChat',
    'description': 'Use command "!!qq" to send something to qq',
    'author': [
        'Railgun_ALGO',  # The author of this plugin
        'Fallen_Breath'  # The author of MCDReforged
    ],
    'link': 'https://github.com/Railgun-wiki/MiraiChat',
    'dependencies': {
        'mcdreforged': '>=1.0.0',
    }
}


def on_load(server: ServerInterface, old):
    server.register_help_message('!!qq', 'Send words to QQ')


# Graia config
loop = asyncio.get_event_loop()

bcc = Broadcast(loop=loop)
app = GraiaMiraiApplication(
    broadcast=bcc,
    connect_info=Session(
        host="http://localhost:8080",  # 填入 httpapi 服务运行的地址
        authKey="graia-mirai-api-http-authkey",  # 填入 authKey
        account=5234120587,  # 你的机器人的 qq 号
        websocket=True  # Graia 已经可以根据所配置的消息接收的方式来保证消息接收部分的正常运作.
    )
)
inc = InterruptControl(bcc)


@bcc.receiver("GroupMessage")
async def group_message_handler(
    message: MessageChain,
    app: GraiaMiraiApplication,
    group: Group, member: Member,
    server: ServerInterface
):
    if message.asDisplay().startswith('!!mc'):
        msg = '[QQ][{}]{}'.format(member.id, message.asDisplay()[5:])
        server.say(msg)


def on_info(server: ServerInterface, info: Info, group: Group):
    if info.is_player:
        if info.content.startswith('!!qq'):
            await app.sendGroupMessage(group, MessageChain.create([Plain('[{}]{}'.format(info.player, info.content[5:]))]))


app.launch_blocking()
