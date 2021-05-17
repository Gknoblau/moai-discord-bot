#!/usr/bin/env python
import datetime
import os
import time

import discord
import feedparser
import requests
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()

CHANNEL_ID = os.getenv('CHANNEL_ID')
USERS_FILE_PATH = os.getenv('USERS_FILE_PATH')
os.environ['TZ'] = 'Etc/UTC'
time.tzset()


import json

with open(USERS_FILE_PATH) as f:
    users = json.load(f)

class GoodReadsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.rss_reader.start()
        self.time_last_checked = time.localtime(time.time())
        self.published_messages = []

    def cog_unload(self):
        self.rss_reader.cancel()

    @tasks.loop(seconds=60.0)
    async def rss_reader(self):
        await self.bot.wait_until_ready()
        # channel = self.bot.get_channel(813991751656275980) # channel ID goes here
        channel = self.bot.get_channel(int(CHANNEL_ID)) # channel ID goes here
        print("Checking for new updates")
        for k, v in users.items():
            d = feedparser.parse(v["feed_url"], modified=v["last_modified"])
            print(k + ": " + str(d.status))
            if (d.status == 200):
                v["last_modified"] = d.modified
                for entry in d.entries:
                    if (self.time_last_checked <= entry.published_parsed):
                        print("Sending message")
                        await channel.send(entry.title)
        self.time_last_checked = time.localtime(time.time())


