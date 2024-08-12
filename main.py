import discord
from discord.ext import tasks
import requests
from datetime import datetime
import asyncio

TOKEN = 'TOKEN'  # Replace with your actual bot token
TIMEZONE_API_URL = 'http://worldtimeapi.org/api/timezone/Asia/Colombo'

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def get_sri_lankan_time():
    response = requests.get(TIMEZONE_API_URL)
    data = response.json()
    current_time = data['datetime']
    return datetime.fromisoformat(current_time).strftime('%H:%M')

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    scheduled_tasks.start()  # Start the scheduled tasks loop

@tasks.loop(minutes=1)  # Check every minute
async def scheduled_tasks():
    now = get_sri_lankan_time()
    print(f"Current Sri Lankan time: {now}")  # Debugging line
    channel = discord.utils.get(client.get_all_channels(), name='rem')  # Replace with your channel name

    if now == '22:09':  # Morning message
        print("Sending good morning message")  # Debugging line
        embed = discord.Embed(
            title="Good Morning!",
            description="Hello baby! Good Morning! We have lot's of Work to Do Today <3",
            color=0xFF69B4  # Pink color
        )
        embed.set_thumbnail(url="profile_pic.png")  # Optional thumbnail
        await channel.send(embed=embed)
    elif now == '20:00':  # Night message
        print("Sending good night message")  # Debugging line
        embed = discord.Embed(
            title="Good Night!",
            description="Hee! Let's Go To sleep --- baby! Let's Start again with Tomorrow",
            color=0xFF69B4  # Pink color
        )
        embed.set_thumbnail(url="profile_pic.png")  # Optional thumbnail
        await channel.send(embed=embed)

client.run(TOKEN)
