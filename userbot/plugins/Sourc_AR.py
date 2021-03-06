import time
from platform import python_version

from telethon import version

from . import ALIVE_NAME, StartTime, catversion, get_readable_time, mention, reply_id

DEFAULTUSER = ALIVE_NAME or "I๐๐๐๐๐โฆโกโฉ"
CAT_IMG = Config.ALIVE_PIC or "https://telegra.ph/file/a8d253cce2e3f7770e492.jpg"
CUSTOM_ALIVE_TEXT = Config.CUSTOM_ALIVE_TEXT or "โ ๐ชู๐๐ูู๐๐ข๐ ูู๐ูู ๐ง๐ข ๐ง๐๐๐๐ง๐๐ข๐ก ๐ูู๐ฅูู๐๐ูู๐ฆ โ"
EMOJI = Config.CUSTOM_ALIVE_EMOJI or "๐ "


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if CAT_IMG:
        cat_caption = f"**{CUSTOM_ALIVE_TEXT}**\n"
        cat_caption += f"**{EMOJI} ูุงุนุฏุฉ ุงูุจูุงูุงุช ใ** `1.0.0`ใ\n"
        cat_caption += f"**{EMOJI} ุงุตุฏุงุฑ ุงููุชููุซูู  ใ** `1.0.0`ใ\n`"
        cat_caption += f"**{EMOJI} ุงุตุฏุงุฑ ุชููุซูู ุงูุนูุฑุจ**  ใ `1.0.0`ใ\n`"
        cat_caption += f"**{EMOJI} ุงุตุฏุงุฑ ุงูุจูุงูุซูู**  ใ `1.0.0`ใ\n`"
        cat_caption += f"{EMOJI} ใ `{uptime}`ใ **ูุฏุฉ ุงูุชุดุบูู**\n`"
        cat_caption += f"{EMOJI} ใ `{mention}`ใ **ุงููุณุชุฎุฏู**\n"
        cat_caption += f"**ฮ ใ** [๐ฒ๐๐๐๐ผ๐พ](t.me/iqthon)ใ**ููุงุฉ ุงูุณูุฑุณ** ๏ข\n"
        await alive.client.send_file(
            alive.chat_id, CAT_IMG, caption=cat_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
             f"**{CUSTOM_ALIVE_TEXT}**\n"
        f"**{EMOJI} ูุงุนุฏุฉ ุงูุจูุงูุงุช ใ** `1.0.0`ใ\n"
        f"**{EMOJI} ุงุตุฏุงุฑ ุงูุชููุซูู  ใ** `1.0.0`ใ\n`"
        f"**{EMOJI} ุงุตุฏุงุฑ ุชููุซูู ุงูุนุฑุจ ใ** `1.0.0`ใ\n"
        f"**{EMOJI} ุงุตุฏุงุฑ ุงูุจุงูุซูู ใ** `1.0.0`ใ\n`"
        f"**{EMOJI} ูุฏุฉ ุงูุชุดุบูู ใ** `{uptime}ใ\n`"
        f"**{EMOJI} ุงููุณุชุฎุฏู ใ** {mention}ใ\n",
        )


def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "ูู ูุชู ุชุนููู ูุงุนุฏุฉ ุจูุงูุงุช"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"โ {str(e)}"
        is_database_working = False
    else:
        output = "ุชุนูู ุจูุฌุงุญ"
        is_database_working = True
    return is_database_working, output


CMD_HELP.update(
    {
        "alive": "**Plugin :** `alive`\
      \n\n  โข  **Syntax : **`.alive` \
      \n  โข  **Function : **__status of bot will be showed__\
      \n\n  โข  **Syntax : **`.` \
      \n  โข  **Function : **__inline status of bot will be shown.__\
      \nSet `ALIVE_PIC` var for media in alive message"
    }
)
