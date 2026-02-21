import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot aktif: {bot.user}")

@bot.event
async def on_member_ban(guild, user):
    channel = discord.utils.get(guild.text_channels, name="genel")
    if channel:
        embed = discord.Embed(
            title="🚫 Birisi Banlandı!",
            description=f"{user.mention} sunucudan banlandı.",
            color=discord.Color.red()
        )
        embed.set_image(url="https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif")
        await channel.send(embed=embed)

TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)