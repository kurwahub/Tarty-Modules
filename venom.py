from telethon import events

commands = "напиши '.venom' чтобы врубить веном мод ❤❤"

# Variable to track whether the feature is enabled
venom_enabled = False

async def register(client):
    global venom_enabled

    @client.on(events.NewMessage)
    async def handler(event):
        global venom_enabled
        
        # Check if the message is a command to toggle the feature
        if event.raw_text == '.venom':
            venom_enabled = not venom_enabled
            status = "enabled" if venom_enabled else "disabled"
            await event.reply(f"веном включен😈😈 {status}.")
            return
        
        # If the feature is enabled, append 'venom' to the message
        if venom_enabled:
            await event.reply(event.raw_text + " venom")
