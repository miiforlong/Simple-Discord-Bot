# Copyright (C) 2026 Lixiod Technologies

import discord
from discord.ext import commands
from discord import app_commands

class Utility(commands.Cog):
"""Information and utility commands."""

def __init__(self, bot):
    self.bot = bot

# Ping command : 

@app_commands.command(name="ping", description="Displays the bot's latency.")
async def ping(self, interaction: discord.Interaction):
    latency = round(self.bot.latency * 1000)
    await interaction.response.send_message(f" Pong! Latency: **{latency} ms**")

# ServerInfo command : 

@app_commands.command(name="serverinfo", description="Displays server details.")
async def serverinfo(self, interaction: discord.Interaction):
    guild = interaction.guild
    embed = discord.Embed(title=f"Info - {guild.name}", color=discord.Color.blue())
    if guild.icon:
        embed.set_thumbnail(url=guild.icon.url)
    embed.add_field(name="Members", value=str(guild.member_count), inline=True)
    embed.add_field(name="Created on", value=guild.created_at.strftime("%d/%m/%Y"), inline=True)
    embed.add_field(name="Owner", value=str(guild.owner), inline=True)
    
    await interaction.response.send_message(embed=embed)

# UserInfo command : 

@app_commands.command(name="userinfo", description="Displays information about a user.")
async def userinfo(self, interaction: discord.Interaction, member: discord.Member = None):
    target = member or interaction.user
    embed = discord.Embed(title=f"Profile of {target.display_name}", color=target.color)
    embed.set_thumbnail(url=target.display_avatar.url)
    embed.add_field(name="ID", value=target.id, inline=False)
    embed.add_field(name="Joined on", value=target.joined_at.strftime("%d/%m/%Y"), inline=True)
    embed.add_field(name="Account created on", value=target.created_at.strftime("%d/%m/%Y"), inline=True)
    
    await interaction.response.send_message(embed=embed)

# Avatar command :

@app_commands.command(name="avatar", description="Displays a user's avatar.")
async def avatar(self, interaction: discord.Interaction, member: discord.Member = None):
    target = member or interaction.user
    embed = discord.Embed(title=f"Avatar of {target.display_name}", color=target.color)
    embed.set_image(url=target.display_avatar.url)
    
    await interaction.response.send_message(embed=embed)

async def setup(bot):
await bot.add_cog(Utility(bot))
