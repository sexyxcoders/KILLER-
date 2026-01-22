import random
import time

from py_yt import VideosSearch
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import config
from AloneMusic import app
from AloneMusic.misc import _boot_
from AloneMusic.plugins.sudo.sudoers import sudoers_list
from AloneMusic.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from AloneMusic.utils.decorators.language import LanguageStart
from AloneMusic.utils.formatters import get_readable_time
from AloneMusic.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string

# Telegram message effects
EFFECT_ID = [
    5046509860389126442,
    5107584321108051014,
    5104841245755180586,
    5159385139981059251,
]


# ========================= PRIVATE START ========================= #
@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    await message.react("🍓")

    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]

        # HELP PANEL
        if name.startswith("help"):
            keyboard = help_pannel(_)
            return await message.reply_video(
                video=config.START_VIDEO_URL,
                has_spoiler=True,
                caption=_["help_1"].format(config.SUPPORT_CHAT),
                reply_markup=keyboard,
            )

        # SUDO LIST
        if name.startswith("sud"):
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=(
                        f"{message.from_user.mention} checked <b>SUDO LIST</b>\n\n"
                        f"<b>User ID:</b> <code>{message.from_user.id}</code>\n"
                        f"<b>Username:</b> @{message.from_user.username}"
                    ),
                )
            return

        # TRACK INFO
        if name.startswith("inf"):
            m = await message.reply_text("🔎 Searching...")
            query = name.replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"

            results = VideosSearch(query, limit=1)
            data = (await results.next())["result"][0]

            caption = _["start_6"].format(
                data["title"],
                data["duration"],
                data["viewCount"]["short"],
                data["publishedTime"],
                data["channel"]["link"],
                data["channel"]["name"],
                app.mention,
            )

            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=_["S_B_8"], url=data["link"]),
                        InlineKeyboardButton(
                            text=_["S_B_9"], url=config.SUPPORT_CHAT
                        ),
                    ]
                ]
            )

            await m.delete()
            await app.send_photo(
                chat_id=message.chat.id,
                photo=data["thumbnails"][0]["url"].split("?")[0],
                caption=caption,
                has_spoiler=True,
                reply_markup=keyboard,
            )

            if await is_on_off(2):
                await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=(
                        f"{message.from_user.mention} checked <b>TRACK INFO</b>\n\n"
                        f"<b>User ID:</b> <code>{message.from_user.id}</code>\n"
                        f"<b>Username:</b> @{message.from_user.username}"
                    ),
                )
            return

    # NORMAL PRIVATE START
    keyboard = private_panel(_)
    await message.reply_video(
        video=config.START_VIDEO_URL,
        has_spoiler=True,
        message_effect_id=random.choice(EFFECT_ID),
        caption=_["start_2"].format(message.from_user.mention, app.mention),
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

    if await is_on_off(2):
        await app.send_message(
            chat_id=config.LOGGER_ID,
            text=(
                f"{message.from_user.mention} started the bot\n\n"
                f"<b>User ID:</b> <code>{message.from_user.id}</code>\n"
                f"<b>Username:</b> @{message.from_user.username}"
            ),
        )


# ========================= GROUP START ========================= #
@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    uptime = int(time.time() - _boot_)
    keyboard = start_panel(_)

    await message.reply_video(
        video=config.START_VIDEO_URL,
        has_spoiler=True,
        caption=_["start_1"].format(app.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

    await add_served_chat(message.chat.id)


# ========================= WELCOME HANDLER ========================= #
@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)

            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass

            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)

                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_CHAT,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                keyboard = start_panel(_)
                await message.reply_video(
                    video=config.START_VIDEO_URL,
                    has_spoiler=True,
                    caption=_["start_3"].format(
                        message.from_user.first_name,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(keyboard),
                )

                await add_served_chat(message.chat.id)
                await message.stop_propagation()

        except Exception as e:
            print(e)