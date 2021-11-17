import discord
import logging
import sys
from discord.ext import commands
from .cogs import music, error, meta
from . import config

cfg = config.load_config()

bot = commands.Bot(command_prefix=cfg["prefix"])


@bot.event
async def on_ready():
    logging.info(f"Logged in as {bot.user.name}")
    game = discord.Game("우성이가 살려낸 은빈이")
    await bot.change_presence(status=discord.Status.online, activity=game)


COGS = [music.Music, error.CommandErrorHandler, meta.Meta]


def add_cogs(bot):
    for cog in COGS:
        bot.add_cog(cog(bot, cfg))  # Initialize the cog and add it to the bot


def run():
    add_cogs(bot)
    if cfg["token"] == "":
        raise ValueError(
            "No token has been provided. Please ensure that config.toml contains the bot token."
        )
        sys.exit(1)
    bot.run(cfg["token"])
