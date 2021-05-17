#!/usr/bin/env python
import os
from discord.ext import commands
from goodreads import GoodReadsCog
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')

bot.add_cog(GoodReadsCog(bot))
bot.run(TOKEN)
