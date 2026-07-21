from telegram import Bot
import asyncio
import os

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = "@onlineaaaaa"

async def main():
    bot = Bot(token=TOKEN)
    await bot.send_message(
        chat_id=CHAT_ID,
        text="🚀 أول رسالة من البوت!\n\nلو الرسالة دي وصلت يبقى كل حاجة شغالة ✅"
    )

asyncio.run(main())
