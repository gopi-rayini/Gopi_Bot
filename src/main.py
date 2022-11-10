import discord
import random
from discord.ext import commands
from discord import app_commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

class abot(discord.Client):
    def _init_(self):
        super()._init_(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=1023520764734996570))
        self.synced = True
        print('Bot is online')

bot = abot(intents=discord.Intents.default())
tree = app_commands.CommandTree(bot)

@tree.command(name="sex", description="Simulate sex", guild=discord.Object(id=1023520764734996570))
async def self(interaction: discord.Interaction):
    await interaction.response.send_message("Commencing sex...")

bot.run("ODE4ODk3Njc4NDgxMDk2NzM0.GpNX7J.vSrP-fPKEnpgnAmQ72w3vSQ2LqYnblaIM_q1g8")
