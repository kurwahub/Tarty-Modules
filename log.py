import os
from telethon import events

commands = "Enter '.logchat' to log messages! arguments: --no-caps, --log-bots, --dont-log-bots"

# Log file path
LOG_FILE = "chat_log.txt"

# Initialize logging settings
log_bots = False
log_lowercase = False

@client.on(events.NewMessage(pattern=r'.logchat (.+)'))
async def log_chat(event):
    global log_bots, log_lowercase

    # Parse arguments
    args = event.pattern_match.group(1).split()
    for arg in args:
        if arg == "--no-caps":
            log_lowercase = True
        elif arg == "--log-bots":
            log_bots = True
        elif arg == "--dont-log-bots":
            log_bots = False

    await event.reply("Logging settings updated!")

@client.on(events.NewMessage())
async def message_handler(event):
    global log_bots, log_lowercase

    # Check if logging is enabled
    if log_bots or (not log_bots and not event.sender_id.is_bot):
        message_text = event.raw_text
        if log_lowercase:
            message_text = message_text.lower()

        # Log the message to the file
        with open(LOG_FILE, "a", encoding="utf-8") as log_file:
            log_file.write(f"{event.sender_id}: {message_text}\n")

        # Optionally, you can also print to console for real-time feedback
        print(f"Logged: {event.sender_id}: {message_text}")

# Ensure the log file exists
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", encoding="utf-8") as log_file:
        log_file.write("Chat Log:\n")
