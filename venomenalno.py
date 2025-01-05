from telethon import events

commands = "Введите '.venomenalno' в группе, чтобы активировать модуль."

# Variable to track whether the feature is enabled and the current chat ID
venomenalno_enabled = False
current_chat_id = None

async def register(client):
    global venomenalno_enabled, current_chat_id

    @client.on(events.NewMessage)
    async def handler(event):
        global venomenalno_enabled, current_chat_id
        
        # Check if the message is a command to toggle the feature
        if event.raw_text == '.venomenalno':
            venomenalno_enabled = not venomenalno_enabled
            current_chat_id = event.chat_id  # Set the current chat ID
            status = "включен" if venomenalno_enabled else "выключен"
            await event.edit(f"Модуль веноменально {status} в этой группе.")
            return
        
        # If the feature is enabled and the message is from the same chat, check for "веном"
        if venomenalno_enabled and event.chat_id == current_chat_id:
            if "веном" in event.raw_text.lower():
                await event.reply("веноменально")
