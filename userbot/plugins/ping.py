import asyncio
import datetime

from . import mention 

@bot.on(admin_cmd(pattern="ping$"))
@bot.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    event = await eor(event, "`·.·★ ℘ıŋɠ ★·.·´")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
        f"╰•★★  ℘ơŋɠ ★★•╯\n\n    ⚘  `{ms}`\n    ⚘  __**Oɯɳҽɾ**__ **:**  {mention}"
    )


CmdHelp("ping").add_command(
  "ping", None, "Checks the ping speed of your DIPESHBOT"
).add_warning(
  "✅ Harmless Module"
).add()
