import asyncio
import random

from . import catmemes

@bot.on(admin_cmd(outgoing=True, pattern="kiss$"))
@bot.on(sudo_cmd(pattern="kiss$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    catevent = await edit_or_reply(event, "`kiss`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["π€΅       π°", "π€΅     π°", "π€΅  π°", "π€΅ππ°"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await catevent.edit(animation_chars[i % 4])


@bot.on(admin_cmd(outgoing=True, pattern="fuk$"))
@bot.on(sudo_cmd(pattern="fuk$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    catevent = await edit_or_reply(event, "`fuking....`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["π       βοΈ", "π     βοΈ", "π  βοΈ", "πβοΈπ¦"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await catevent.edit(animation_chars[i % 4])


@bot.on(admin_cmd(outgoing=True, pattern="sex$"))
@bot.on(sudo_cmd(pattern="sex$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    catevent = await edit_or_reply(event, "`sex`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["π€΅       π°", "π€΅     π°", "π€΅  π°", "π€΅πΌπ°"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await catevent.edit(animation_chars[i % 4])


CMD_HELP.update(
    {
        "gali": "**plugin : **`gali`\
        \n\n**Commands :**\
        \n  β’  `.abuse`\
        \n  β’  `.abusehard`\
        \n  β’  `.rendi`\
        \n  β’  `.rape`\
        \n  β’  `.fuck`\
        \n  β’  `.thanos`\
        \n  β’  `.kiss`\
        \n  β’  `.fuk`\
        \n  β’  `.sex`\
        \n\n**Function :**\
        \n__First 5 are random gali string generaters__\
        \n__Last 3 are animations__\
        "
    }
)
