import discord

client = discord.Client()

@client.event
async def on_ready():
    from_channels = [
        # channel ids from just enter your stupid channelids if its to much just remove the stupid channelids and client.get_channel(channelid) stupid nigga
        client.get_channel(channelid),
        client.get_channel(channelid),
        client.get_channel(channelid),
        client.get_channel(channelid),
        client.get_channel(channelid),
        client.get_channel(channelid),
        client.get_channel(channelid),
        client.get_channel(channelid),
        client.get_channel(channelid),
        client.get_channel(channelid)
    ]
    # to channelid 
    to_channel = client.get_channel(channelid)

    if None in from_channels or to_channel is None:
        return

    for from_channel in from_channels:
        async for message in from_channel.history():
            if message.attachments:
                for attachment in message.attachments:
                    file = await attachment.to_file()
                    await to_channel.send(file=file)
            await to_channel.send(content=message.content)

    await client.close()

client.run("stupid nigga just enter your token and dont remove bot = false", bot=False)