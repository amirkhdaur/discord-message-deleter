import discord
import asyncio
import config

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    channel = await client.fetch_channel(config.CHANNEL_ID)
    async for message in channel.history():
        if message.author == client.user:
            await message.delete()
            await asyncio.sleep(config.DELAY)
        

client.run(config.TOKEN)