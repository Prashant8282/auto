import telegram
import asyncio

# Replace with your Telegram Bot token
TELEGRAM_BOT_TOKEN = '6459647682:AAGX4P4aozvOj9zBwzYNO3_-DDBeT_ejeIY' 

# Time to wait before deleting messages (in seconds)
DELETE_DELAY = 30  

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

async def delete_message(chat_id, message_id):
    await asyncio.sleep(DELETE_DELAY)
    await bot.delete_message(chat_id=chat_id, message_id=message_id)

def handle_message(update, context):
    message = update.message
    # Schedule the message to be deleted
    asyncio.create_task(delete_message(message.chat_id, message.message_id))

if name == 'main':
    updater = telegram.Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    message_handler = telegram.MessageHandler(telegram.Filters.text, handle_message)
    dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()
