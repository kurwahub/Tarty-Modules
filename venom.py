from telethon import events

commands = "напиши '.venom' чтобы врубить веном мод ❤❤"

# Variable to track whether the feature is enabled
venom_enabled = False
current_chat_id = None

async def register(client):
    global venom_enabled, current_chat_id

    @client.on(events.NewMessage)
    async def handler(event):
        global venom_enabled, current_chat_id
        
        # Check if the message is a command to toggle the feature
        if event.raw_text == '.venom':
            venom_enabled = not venom_enabled
            current_chat_id = event.chat_id  # Set the current chat ID
            status = "включен" if venom_enabled else "выключен"
            await event.edit(f"веном {status}😈😈.")
            return
        
        # If the feature is enabled and the message is from the same chat, append 'venom' to the message
        if venom_enabled and event.chat_id == current_chat_id:
            await event.edit(event.raw_text + " venom")
