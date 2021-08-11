# ГОТОВ
import discord
from discord.ext import commands

from datetime import datetime
import json
import os


def get_prefix(bot, ctx):
	with open("./botConfiguration/.db/guildsConfiguration/guildsConfig.json", "r") as file: return json.load(file)[str(ctx.guild.id)]["prefix"]

bot = commands.AutoShardedBot(
	command_prefix = get_prefix,
	case_insensitive = True,
	shard_count = 1,
	intents = discord.Intents.all()
)

bot.remove_command("help")


print("\n".join([
	"ooooo      ooo",
	"`888b.     `8'",
	" 8 `88b.    8   .ooooo.  oooo    ooo oooo  oooo   .oooo.o",
	" 8   `88b.  8  d88' `88b  `88b..8P'  `888  `888  d88(  '8",
	" 8     `88b.8  888ooo888    Y888'     888   888  `'Y88b.",
	" 8       `888  888        .o8''88b    888   888  o.  )88b",
	"o8o        `8  `Y8bod8P' o88'   888o  `V88V'V8P' 8""888P'",
	"\n"
]))


class LoadingCogs:
	#[bot.load_extension(f"cogs.events.guilds.{filename[:-3]}") for filename in os.listdir("./cogs/events/guilds") if filename.endswith(".py")]
	for filename in os.listdir("./botConfiguration/cogs/events/guilds"):
		if filename.endswith(".py"):
			bot.load_extension(f"botConfiguration.cogs.events.guilds.{filename[:-3]}")

			print(f"{datetime.now()} Файлы {', '.join([filename])} в коге cogs/events/guilds загружены!")
	#[bot.load_extension(f"cogs.events.bot.{filename[:-3]}") for filename in os.listdir("./cogs/events/bot") if filename.endswith(".py")]
	for filename in os.listdir("./botConfiguration/cogs/events/bot"):
		if filename.endswith(".py"):
			bot.load_extension(f"botConfiguration.cogs.events.bot.{filename[:-3]}")

			print(f"{datetime.now()} Файлы {', '.join([filename])} в коге cogs/events/bot загружены!")
	
	#[bot.load_extension(f"cogs.commands.{filename[:-3]}") for filename in os.listdir("./cogs/commands") if filename.endswith(".py")]
	#for filename in os.listdir("./cogs/commands"):
		#if filename.endswith(".py"):
			#bot.load_extension(f"cogs.commands.{filename[:-3]}")

			#print(f"{datetime.now()} Файлы {', '.join([filename])} в коге cogs/commands загружены!")
	
	#for filename in os.listdir("./botConfiguration/cogs/commands/special"):
		#if filename.endswith(".py"):
			#bot.load_extension(f"botConfiguration.cogs.commands.special.{filename[:-3]}")

			#print(f"{datetime.now()} Файлы {', '.join([filename])} в коге cogs/commands/special загружены!")


bot.run("ODA2Nzk0OTA2NTc1MzA2Nzcy.YBuoTw.5vavmBfr5Jd0Goi63cRQLP2M8wU")