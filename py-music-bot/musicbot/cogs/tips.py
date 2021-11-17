from discord.ext import commands
import discord
import random


class Tips(commands.Cog):
    """Commands for providing tips about using the bot."""

    def __init__(self, bot, config):
        self.bot = bot
        self.config = config[__name__.split(".")[-1]]
        self.tips = ["Only admins and the song requester can immediately skip songs. Everybody else will have to vote!",
                     f"You can check out my source code here: {self.config['github_url']}"]

