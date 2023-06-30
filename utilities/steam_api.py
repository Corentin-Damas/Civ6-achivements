from dotenv import load_dotenv
import os
import requests
import json


def get_game_data():
    load_dotenv("config.env")

    ACCOUNT_ID = os.getenv("MY_STEAM_ID")  # Currently my account
    GAME_ID = 289070  # Sid Meier's Civilization VI app id
    API_KEY = os.getenv("STEAM_API_KEY")  # Your Api key

    res = requests.get(
        f"https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid={GAME_ID}&key={API_KEY}&steamid={ACCOUNT_ID}&l=en"
    )
    # l=en at the end is very import, it give you all the achivement Name and details
    res.raise_for_status()

    player_game_info = res.json()
    game_name = player_game_info["playerstats"]["gameName"]
    game_achievements = player_game_info["playerstats"]["achievements"]

    # Create the new document
    data = {game_name: game_achievements}
    with open("game_data.json", "w") as outfile:
        json.dump(data, outfile)
