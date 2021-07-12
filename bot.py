import os

import discord
from rasa.nlu.model import Interpreter

from utils import aqi_response, time_response, weather_responce


HANDLERS = {
    'aqi': aqi_response,
    'time': time_response,
    'weather': weather_responce,
}


bot = discord.Client()
interpreter = Interpreter.load('models/nlu')


@bot.event
async def on_ready():
    # load model
    print("Bot is ready")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg = message.content
    parse_res = interpreter.parse(msg)

    if parse_res['intent']['confidence'] < 0.75:
        await message.channel.send("Didn't get it(\nTry again")
    else:
        if parse_res['entities']:
            intent = parse_res['intent']['name']
            location = parse_res['entities'][0]['value']
            await message.channel.send(HANDLERS[intent](location))
        else:
            await message.channel.send('Unable to find the location.')


if __name__ == '__main__':
    bot.run(os.environ.get('DISCORD_TOKEN'))
