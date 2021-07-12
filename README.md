# DiscoJarvis

Assistant bot for Discord.

## Functionality

Currently can tell you weather, time and AQI (air quality index)

## Train model

Add new data to `data/nlu.yml` and edit `config.yml` to modify pipeline. Run the following command to retrain the model:

```
rasa train nlu
```

## Run bot

Add environment variable *DISCORD_TOKEN* and asign your bot token to it.
 
 Start the bot:

`python bot.py`
