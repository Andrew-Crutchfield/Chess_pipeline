import requests
import config

def fetch_tournament_data():
    try:
        url = f"{config.API_URL}/{config.TOURNAMENT_ID}"
        response = requests.get(url, headers=config.HEADERS)
        response.raise_for_status()
        print("✅ Successfully fetched data from Lichess API")
        return response.json()
    except requests.RequestException as e:
        print(f"❌ API request failed: {e}")
        return None
