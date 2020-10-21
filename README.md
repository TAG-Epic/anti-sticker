# A bot to delete stickers - because fuck stickers
[![Invite here](https://img.shields.io/badge/Invite-Here-brightgreen?style=for-the-badge)](https://github.com/tag-epic/speedcord)
[![Uses SpeedCord](https://img.shields.io/badge/Uses-speedcord-brightgreen?style=for-the-badge)](https://discord.com/api/oauth2/authorize?client_id=766609544394309642&permissions=9216&scope=bot)  
This bot is dedicated to a new specific feature Discord has added a while ago and is slowly rolling out. What it is meant to do in reality is, delete any stickers sent by anyone in servers the bot is part of.

In order for this bot to work, the bot requires the following permissions in all channels you wish it to function in:
- `MANAGE_MESSAGES`
- `READ_MESSAGES`
- `SEND_MESSAGES`

To change the message the bot sends modify line 19 of `main.py` to say the message you wish to send.

## Demo
![Demo](https://cdn.discordapp.com/attachments/761924508965666816/768533210866122782/2020-10-21_18-10-40.gif)

---
### Running the bot with docker-compose

- Firstly, rename `docker-compose.yml.example` to `docker-compose.yml`
- Next, change the value of `token` in that file from `YOUR_BOT_TOKEN` to whatever your Discord bot token is. If you don't know how to create a bot, see [this guide](https://discordpy.readthedocs.io/en/latest/discord.html)
