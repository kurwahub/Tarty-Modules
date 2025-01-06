import time
import asyncio
from telethon import events

@client.on(events.NewMessage(pattern='!ping'))
async def ping(event):
    start_time = time.time()
    
    # Send a request to the Telegram API to measure the ping
    await client.send_message('me', 'Ping test')  # Sending a message to self to measure response time
    end_time = time.time()
    
    # Calculate the ping
    telegram_ping = f"{(end_time - start_time) * 1000:.2f} ms"  # Convert to milliseconds

    # Calculate uptime
    uptime = time.time() - client.start_time
    uptime_str = f"{int(uptime // 3600)}h {int((uptime % 3600) // 60)}m {int(uptime % 60)}s"

    # Edit the message
    await event.reply(f"🚀 Telegram ping: {telegram_ping}\n✈️ Uptime: {uptime_str}")

# Store the start time when the client starts
client.start_time = time.time()
