"""
Created by Epic at 10/15/20
"""
from speedcord import Client
from speedcord.http import Route
from speedcord.ext.typing.context import MessageContext
from os import environ as env

client = Client(512)
client.token = env["token"]


@client.listen("MESSAGE_CREATE")
async def on_message(data, shard):
    if len(data.get("stickers", [])) != 0:
        r = Route("DELETE", "/channels/{channel_id}/messages/{message_id}", channel_id=data["channel_id"], message_id=data["id"])
        await client.http.request(r)

client.run()

