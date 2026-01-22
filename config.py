#
# Copyright (C) 2021-2022 by TheAloneteam@Github, < https://github.com/TheAloneTeam >.
#
# This file is part of < https://github.com/TheAloneTeam/TheAloneMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TheAloneTeam/TheAloneMusic/blob/master/LICENSE >
# All rights reserved.

import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_URL = getenv("API_URL", 'https://api.nexgenbots.xyz') #youtube song url
VIDEO_API_URL = getenv("VIDEO_API_URL", 'https://api.video.thequickearn.xyz')
API_KEY = getenv("API_KEY", None)

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "22657083"))
API_HASH = getenv("API_HASH", "d6186691704bd901bdab275ceaab88f3")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "8228009347:AAEbWfkUTuhx8H6qP1vKdEH_ZvMvaGIQpUI")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://itzrayn01_db_user:7MufiiQtN2lJ02Sc@cluster0.bfxbeey.mongodb.net/?appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

# Set this to true if you want post ads automatically
ADS_MODE = getenv("ADS_MODE", None)

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002276415311"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "5277773671"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/sexyxcoders/KILLER-",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/NexaCoders")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/NexaMeetup")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", None))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQFZuDsAEQ_HYRJb7cdcK7SIbPLuxHkb-tC2naFnKQowm9s4ct_jfWrM5zAUbnx6D-YXDxdm5PR9vhqGETE4g_jP1KLyRS_wEhcN68HkarodlIZzhoT2eCgExC0pqC9d_NsHuF7p5NkOX5W4KSKtihFR1k39rHJk8_9Gushq9K8rtpcneFG40knfDjf5wgLZdtDRTQT5ZGePX0NlvqoHObZeOmiGK4vRM2mfqB-RyAuC90WwsZQ0GRlR8te490QXGgLdRZLk7hIbqNNhP23pr1MnmWqKvVVJvpxex0zOqdRMmLIcOS5hAn1d3vFC9I0VAfLT38s3wMW_bhBQz-YLWl3UpXqG-QAAAAHYxh9NAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_VIDEO_URL = getenv(
    "START_VIDEO_URL",
    "https://files.catbox.moe/m8wvfi.mp4"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/vxezej.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/8p0047.jpg"
STATS_IMG_URL = "https://files.catbox.moe/cdekos.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/8p0047.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/8p0047.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/8p0047.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/8p0047.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/8p0047.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/8p0047.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/8p0047.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/8p0047.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
