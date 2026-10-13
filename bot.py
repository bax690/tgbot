import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command

# Вставьте сюда токен, который вы получили у @BotFather
TOKEN = ""

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        f"👋 **Привет, {message.from_user.full_name}!**\n\n"
        "Я твой новый бот, успешно запущенный на сервере. "
        "Чтобы узнать, что я умею, нажми /help."
    )

@dp.message(Command(commands=["help"]))
async def cmd_help(message: types.Message):
    await message.answer(
        "❓ **Справка**\n\n"
        "Пока что я умею отвечать только на две команды:\n"
        "• /start — перезапустить бота и получить приветствие.\n"
        "• /help — открыть это меню.\n\n"
        "🤖 *Создано специально для твоего сервера!*"
    )

async def main():
    print("Бот успешно запущен и слушает сервер...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
