import discord, random, datetime, os
from discord.ext import commands
import wikipedia as w
import Modules.WeatherForcast.WeatherForcast as wf

client = commands.Bot(command_prefix = "")

@client.event
async def on_ready():
	print("Bot is Ready")
	
@client.command(aliases =["_help", "Commands", "commands", "Bot help", "bot help"])
async def Help(ctx):
	with open('BotHelp.txt') as a:
		await ctx.send(a.read())

@client.command(aliases = ["Hello", "Hi", "hello", "greet", "Greet"])
async def hi(ctx):
	await ctx.send("Hi!")
	
@client.command(aliases = ["Bye", "Tata", "tata", "Good bye", "good bye", "see ya", "See ya"])
async def bye(ctx):
	await ctx.send("Bye!")


'''@client.command(aliases = ["stonepapercissor", "stone", "Spc"])
async def spc(ctx):
	games = 5
	await ctx.send("This is a stone-paper-cissors game!")
	await ctx.send(f"Total games = {games}")'''
    
@client.command(aliases = ["Time"])
async def time(ctx):
	t = datetime.datetime.now().strftime('%I:%M %p')
	await ctx.send(t)

@client.command(aliases = ["wiki", "Wiki", "Wikipedia"])
async def wikipedia(ctx, *,src): # ctx, *,src
	info = f"Could not find {src}."
	try:
		info = w.summary(str(src).strip(),5)
	except: pass
	await ctx.send(info)

@client.command(aliases = ["Weather", "forecast", "Forecast"])
async def weather(ctx, *, place):
	try:
		weather = wf.forecast(place)
		intro = "Weather forecast for " + weather['place'].title() + " is:\n"
		day = ""
		if weather['day']['phrases']:
			day += "\tWeather: " + weather['day']['phrases'] + "\n"
		if weather['day']['temperature']:
			day += "\tLowest Temperature: " + str(weather['day']['temperature']) + "\n"
		if weather['day']['precipitate']:
			day += "\tPrecipitation: " + str(weather['day']['precipitate']) + "\n"
		if weather['day']['humidity']:
			day += "\tHumidity: " + str(weather['day']['humidity']) + "\n"
		day += "\n"

		night = ""
		if weather['night']['phrases']:
			night += "\tWeather: " + weather['night']['phrases'] + "\n"
		if weather['night']['temperature']:
			night += "\tLowest Temperature: " + str(weather['night']['temperature']) + "\n"
		if weather['night']['precipitate']:
			night += "\tPrecipitation: " + str(weather['night']['precipitate']) + "\n"
		if weather['night']['humidity']:
			night += "\tHumidity: " + str(weather['night']['humidity']) + "\n"
		night += "\n"
		
		tell = intro
		if len(day) > 10:
			tell += "Day :\n" + day
		if len(night) > 10:
			tell += "Night :\n" + night
	except: tell = f"Could not find place {place.title()}."
	await ctx.send(tell)

client.run(os.getenv("token1"))
