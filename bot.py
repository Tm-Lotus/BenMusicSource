from pyrogram import Client, idle
from pyromod import listen



bot = Client(
    "mo",
    api_id=8923378,
    api_hash="4008406712b80bb7589425540e2697e9",
    bot_token="6878180342:AAG2cii5bLrKTMzWvE7FFiHCqbV_W5XtBrc",
    plugins=dict(root="MZombie")
    )

DEVS = ["BENN_DEV"]

bot_id = bot.bot_token.split(":")[0]

async def start_zombiebot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    for hh in DEVS:
        try:
            await bot.send_message(hh, "**تم تشغيل الصانع بنجاح ...🥀**")
        except:
            pass
    await idle()
