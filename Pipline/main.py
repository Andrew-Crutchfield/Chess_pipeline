from fetch_data import fetch_tournament_data
from process_data import process_tournament_data
from store_data import save_to_mysql

def main():
    print("🚀 Starting pipeline...")

    data = fetch_tournament_data()
    if not data:
        print("❌ Pipeline failed during data fetch.")
        return

    df = process_tournament_data(data)
    if df is None:
        print("❌ Pipeline failed during data processing.")
        return

    save_to_mysql(df)

    print("✅ Pipeline completed successfully!")

if __name__ == "__main__":
    main()
