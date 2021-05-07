# Aritra-sBot

## About
Aritra-sBot is a personal Discord utility bot designed to bring a variety of quick-access tools into a chat server. While it started as a fun project to explore the Discord API, it has grown into a functional toolkit that handles everything from real-time weather forecasts and Wikipedia summaries to basic social interactions. It serves as a practical implementation of an asynchronous bot capable of orchestrating multiple third-party API integrations.

## Technical Details
The bot is built using Python and the `discord.py` (v1.7.1) framework. The architecture is based on an asynchronous event-loop, where the bot listens for commands to trigger specific handlers.

Key technical components include:
- Geocoding: The bot utilizes `geopy.geocoders.Nominatim` to translate natural language place names into precise latitude and longitude coordinates.
- Weather Integration: It consumes a weather REST API to retrieve detailed atmospheric data, splitting the output into day and night segments for better readability.
- Information Retrieval: A dedicated integration with the `wikipedia` library allows the bot to fetch and return concise summaries of specified queries.
- Deployment: The project is structured for cloud hosting on Heroku, utilizing a `Procfile` for process orchestration and a `runtime.txt` to specify the Python environment.

## Execution
1. Clone the repository to your local machine.
2. Install the necessary dependencies:
   `pip install -r requirements.txt`
3. Configure your bot token by setting an environment variable named `token1` with your Discord Bot Token.
4. Run the bot using the main script:
   `python Aritra-sBot.py`

Note: You must obtain a bot token from the Discord Developer Portal and ensure the bot has the required "Message Content" and "Server Members" intents enabled to function correctly.