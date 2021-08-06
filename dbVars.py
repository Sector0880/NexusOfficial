# ГОТОВ
import json
import yaml


class Bot:
	def bot_config_data(self):
		with open("./botConfiguration/.db/bot/botConfiguration/botConfig.yml", "r") as read_file: return yaml.safe_load(read_file)
	def bot_switches_data(self):
		with open("./botConfiguration/.db/bot/botConfiguration/botSwitches.yml", "r") as read_file: return yaml.safe_load(read_file)
	
	def get_bot_presence(self): return self.bot_config_data()["presence"]["title"]

	#def get_bot_output_correct(self): return self.bot_switches_data()["dev"][0]["special-functions"][0]["commands"][0]["output"]["correct"]
	def get_bot_output_correct(self): return self.bot_switches_data()["dev"]["special-functions"]["commands"]["output"]["correct"]
	#def get_bot_output_partial_sleep(self): return self.bot_switches_data()["dev"][0]["special-functions"][0]["commands"][0]["output"]["partial-sleep"]
	def get_bot_output_partial_sleep(self): return self.bot_switches_data()["dev"]["special-functions"]["commands"]["output"]["partial-sleep"]
	#def get_bot_output_emoji(self): return self.bot_switches_data()["dev"][0]["special-functions"][0]["commands"][0]["output"]["emoji"]
	def get_bot_output_emoji(self): return self.bot_switches_data()["dev"]["special-functions"]["commands"]["output"]["emoji"]

	#def get_bot_message_output_delete_after(self): return self.bot_switches_data()["dev"][0]["special-functions"][1]["message-output"]["delete_after"]
	def get_bot_message_output_delete_after(self): return self.bot_switches_data()["dev"]["special-functions"]["message-output"]["delete_after"]

	#def get_bot_mention_embs_stopwatch(self): return self.bot_switches_data()["dev"][1]["updates"][0]["commands"][0]["mention"]["embs"]["stopwatch"]
	def get_bot_mention_embs_stopwatch(self): return self.bot_switches_data()["dev"]["updates"]["commands"]["mention"]["embs"]["stopwatch"]
	#def get_bot_mention_embs_checks(self): return self.bot_switches_data()["dev"][1]["updates"][0]["commands"][0]["mention"]["embs"]["checks"]
	def get_bot_mention_embs_checks(self): return self.bot_switches_data()["dev"]["updates"]["commands"]["mention"]["embs"]["checks"]

	#def get_bot_testers_work_code_conditions(self): return self.bot_switches_data()["testers"][0]["work_code-conditions"]
	def get_bot_testers_work_code_conditions(self): return self.bot_switches_data()["testers"]["work_code-conditions"]

bot_presence = Bot().get_bot_presence

bot_output_correct = Bot().get_bot_output_correct
bot_output_partial_sleep = Bot().get_bot_output_partial_sleep
bot_output_emoji = Bot().get_bot_output_emoji

bot_message_output_delete_after = Bot().get_bot_message_output_delete_after

bot_mention_embs_stopwatch = Bot().get_bot_mention_embs_stopwatch
bot_mention_embs_checks = Bot().get_bot_mention_embs_checks

bot_testers_work_code_conditions = Bot().get_bot_testers_work_code_conditions


class Guild:
	def guilds_config_data(self):
		with open("./botConfiguration/.db/guildsConfiguration/guildsConfig.json", "r") as read_file: return json.load(read_file)

	def get_guild_name(self, ctx): return self.guilds_config_data()[str(ctx.guild.id)]["overview"]["name"]
	def get_guild_prefix(self, ctx): return self.guilds_config_data()[str(ctx.guild.id)]["prefix"]
	def get_guild_language(self, ctx): return self.guilds_config_data()[str(ctx.guild.id)]["language"]
	
	def get_guild_premium(self, ctx): return self.guilds_config_data()[str(ctx.guild.id)]["additional-features"][0]["privileges"][0]["premium"]
	def get_guild_show_id(self, ctx): return self.guilds_config_data()[str(ctx.guild.id)]["additional-features"][2]["show_id"]
	def get_guild_tester(self, ctx): return self.guilds_config_data()[str(ctx.guild.id)]["additional-features"][1]["modes"][0]["tester"]

	def get_guild_bot_output(self, ctx): return self.guilds_config_data()[str(ctx.guild.id)]["protection"][0]["gateaway"]["bot_output"]

guild_name = Guild().get_guild_name
guild_prefix = Guild().get_guild_prefix
guild_language = Guild().get_guild_language

guild_premium = Guild().get_guild_premium
guild_show_id = Guild().get_guild_show_id
guild_tester = Guild().get_guild_tester

guild_bot_output = Guild().get_guild_bot_output


class Staff:
	def staff_config_data(self):
		with open("./botConfiguration/.db/staff/list/staffList.json", "r") as read_file: return json.load(read_file)

	def get_staff_owner_id(self): return self.staff_config_data()["owner"]["id"]

	def get_testers(self): return self.staff_config_data()["testers"]

staff_owner_id = Staff().get_staff_owner_id

staff_testers = Staff().get_testers


class Doc:
	class Errors:
		def get_error_server_blocked(self):
			with open("./botConfiguration/.db/doc/errors/serverBlocked.yml") as read_file: return yaml.safe_load(read_file)
		def get_error_invalid_language(self):
			with open("./botConfiguration/.db/doc/errors/invalidLanguage.yml") as read_file: return yaml.safe_load(read_file)
		def get_error_terminal_traceback_error(self):
			with open("./botConfiguration/.db/doc/errors/terminalTracebackError.yml") as read_file: return yaml.safe_load(read_file)
		def get_error_terminal_command_error(self):
			with open("./botConfiguration/.db/doc/errors/terminalCommandError.yml") as read_file: return yaml.safe_load(read_file)

error_server_blocked = Doc().Errors().get_error_server_blocked
error_invalid_language = Doc().Errors().get_error_invalid_language
error_terminal_traceback_error = Doc().Errors().get_error_terminal_traceback_error
error_terminal_command_error = Doc().Errors().get_error_terminal_command_error