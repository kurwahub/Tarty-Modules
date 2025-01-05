from telethon import events

commands = "Type '.hi' to receive a greeting."

async def register(client):
    @client.on(events.NewMessage)
    async def handler(event):
        if event.raw_text == '.hi':
            await event.reply("Hello!")
