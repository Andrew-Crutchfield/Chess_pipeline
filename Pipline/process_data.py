import pandas as pd

def process_tournament_data(data):
    if not data or "players" not in data:
        print("❌ Invalid or missing data")
        return None

    players = data["players"]
    df = pd.DataFrame(players)

    df = df[['username', 'rating', 'rank', 'score']]

    print("✅ Data processed and cleaned")
    return df
