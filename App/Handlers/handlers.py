from aiogram.filters import ChatMemberUpdatedFilter, IS_NOT_MEMBER, MEMBER
from aiogram.types import ChatMemberUpdated
from aiogram import Router, Bot
import logging

router = Router()

@router.chat_member(ChatMemberUpdatedFilter(IS_NOT_MEMBER >> MEMBER))
async def handle_new_member(event: ChatMemberUpdated, bot: Bot):
    user = event.new_chat_member.user
    chat = event.chat

    if user.is_bot:
        logging.info(f"Bot added: {user.id}")
        return
    
    logging.info(f"New member: {user.full_name} in {chat.title}")

    Welcome_text = (
    f"👋 Привет, {user.mention_html()}!\n"
    f"Добро пожаловать в {chat.title}!\n"
    "Представся и расскажи о себе вкатце\n"
    "1. Имя\n"
    "2. Возраст\n"
    "3. Какие языки знаешь (Python, JavaScript, C++, и т.д.)\n"
    "4. Какая специализация (Frontend, Backend, Fullstack, DevOps, Data Science и т.д.)\n"
    )

    await bot.send_message(
        chat_id=chat.id,
        text = Welcome_text,
        parse_mode="HTML"
    )