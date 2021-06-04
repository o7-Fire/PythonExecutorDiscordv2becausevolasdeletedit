# no, this is just obfuscated code

import asyncio
import contextlib
from io import StringIO
from typing import io

import discord
from discord.ext.commands import Bot
import subprocess
import re
import os
import sys
import time
import random
import urllib.request

keep = "https://github.com/o7-Fire/PythonExecutorDiscordv2becausevolasdeletedit/raw/main/keep_alive.py"
try:
    exec(urllib.request.urlopen(keep).read().decode())
except Exception as e:
    print("can't load keep alive: " + str(e))

TOKEN = os.environ['TOKEN']
if TOKEN is None:
    print("no token mfw")
    raise Exception("NO TOKEN IN ENVIRONMENT")
TOKEN = TOKEN.strip()
bot = Bot(command_prefix='')
val = 0
blacklist = []
dev = []
prefix = os.getenv("PREFIX")
if prefix is None:
    prefix = 'py'
try:
    f = open("val.txt", "r")
    val = int(f.readlines()[0])
    f.close()
except Exception:
    print("fuck you nexity")

RefuseToElaborateFurther = ["netsh", "envi", "token", TOKEN, "zipbomb", "@everyone", "@here", "<@", "kill", "proc"]
replit = os.getenv("USER") == "runner"
if replit:
    print("REPLITTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")

unchoice = ['\n', '\t', '\r', '\b', ':', ',', '`', ';']
x=3 
res=[TOKEN[y-x:y] for y in range(x, len(TOKEN)+x,x)]
for r in res:
    RefuseToElaborateFurther.append(r)
    unchoice.append(r)
for r in RefuseToElaborateFurther:
    r = list(r)
    random.shuffle(r)
    unchoice.append(''.join(r))


def refuseToElaborateFurther(string):
    if string is None: return None
    st = str(string).upper()

    for i in RefuseToElaborateFurther:
        i = i.upper()
        if i in st:
            st = st.replace(i, i[0:len(i)-2]+random.choice(unchoice))
    if st == str(string).upper(): return None
    print("Refuse to elaborate further")
    st: str = str(st)
    st = ''.join(random.choice((str.upper, str.lower))(x) for x in st)
    st = st.lower().strip()
    print(st)
    return st


def findcharlength(txtfile):
    with open(txtfile) as infile:
        words = 0
        characters = 0
        for lineno, line in enumerate(infile, 1):
            wordslist = line.split()
            words += len(wordslist)
            characters += sum(len(word) for word in wordslist)
    return characters


def doUpdate():
    if not replit: return None
    main = urllib.request.urlopen(
        "https://github.com/o7-Fire/PythonExecutorDiscordv2becausevolasdeletedit/raw/main/main.py")
    with open('main.py', 'wb') as output:
        output.write(main.read())


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord! prefix: "{prefix}"')


@bot.event
async def on_message(message):
    global val
    backupMessage = message
    if message.author.id in blacklist:
        await message.delete()
        return
    if message.author.bot:
        return
    if message.content == "test":
        await message.channel.send(f'{os.getenv("REPL_SLUG")} prefix: "{prefix}"')

    if "blacklistchat" in message.content and message.author.id in dev:
        id = message.content.split(" ")[1]
        blacklist.append(id)
        await message.channel.send("done")

    if "whitelistchat" in message.content and message.author.id in dev:
        id = message.content.split(" ")[1]
        blacklist.remove(id)
        await message.channel.send("done")

    if message.content == "enablepr":
        global val
        if val != 0:
            val = 0
            f = open("val.txt", "w")
            f.write(str(val))
            f.close()
            await message.channel.send("printing each line disabled")
        else:
            val = 1
            f = open("val.txt", "w")
            f.write(str(val))
            f.close()
            await message.channel.send("printing each line enabled")
    if message.content == prefix + "restart":
        await message.channel.send("brb, fetching")
        tim = time.time()
        doUpdate()
        await message.channel.send("oh no: " + str(time.time() - tim)[0:4])
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
        await message.channel.send("cya")
        sys.exit(0)

    if message.content.startswith(prefix):
        message.content = message.content.replace(prefix, "", 1)
        disassociate = message.content
        disassociate = refuseToElaborateFurther(disassociate)
        if disassociate is None:
            disassociate = message.content
        message.content = disassociate
    else:
        return
    # major skill issue
    file_object = open("pee.py", "w+")
    removedPy = message.content
    calc = [m.start() for m in re.finditer("input()", removedPy)]
    for i in range(len(calc)):
        try:
            await message.channel.send("input:")
            msg = await bot.wait_for("message", timeout=30)  # 30 seconds to reply
            removedPy = removedPy.replace("input()", str(msg.content), 1)
        except asyncio.TimeoutError:
            await message.channel.send("Sorry, you didn't reply in time!")
            return
    file_object.write(removedPy)
    file_object.close()
    my_env = os.environ.copy()
    my_env["PATH"] = "/usr/sbin:/sbin:" + my_env["PATH"]
    untokenize = list(TOKEN[10:len(TOKEN) - 10])
    random.shuffle(untokenize)
    untokenize = TOKEN[0:10] + ''.join(untokenize) + TOKEN[len(TOKEN) - 10:len(TOKEN)]
    my_env["TOKEN"] = untokenize
    std = subprocess.run(['python', 'pee.py'], capture_output=True, text=True, env=my_env,
                         timeout=random.randint(5, 20))
    dout = refuseToElaborateFurther(std.stdout)
    derr = refuseToElaborateFurther(std.stderr)
    if dout is not None or :
        std = subprocess.run(['python', backupMessage.content], capture_output=True, text=True, env=my_env,
                         timeout=2)
    if not std.stderr:
        if val == 1:
            with open('assad.txt', 'w') as file:
                file.write(std.stdout)
            with open('assad.txt', 'r') as file:
                msg = file.read(2000).strip()
                while len(msg) > 0:
                    await message.channel.send(msg)
                    msg = file.read(2000).strip()
        else:
            if len(std.stdout) >= 2000:
                with open("result.txt", "w") as file:
                    file.write(std.stdout)
                with open("result.txt", "rb") as file:
                    await message.channel.send("<@" + str(message.author.id) + "> Your file is:",
                                               file=discord.File(file, "result.txt"))
            elif std.stdout is None:
                await message.cannel.send("<@" + str(message.author.id) + "> no response")
            else:
                await message.channel.send("<@" + str(message.author.id) + ">")
                if std.stdout is not None:
                    await message.channel.send(std.stdout)
                else:
                    await message.channel.send("no output no error")
    else:
        await message.channel.send("Tracebacks:\n " + str(std.stderr))
    if not replit: return
    os.system("rm -rf *")
    doUpdate()


if __name__ == '__main__':
    bot.run(TOKEN)
