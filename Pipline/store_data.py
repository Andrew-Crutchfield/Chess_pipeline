import mysql.connector
from mysql.connector import Error
import config

def connect_db():
    try:
        conn = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME
        )
        print("✅ Connected to MySQL database")
        return conn
    except Error as e:
        print(f"❌ Error connecting to MySQL: {e}")
        return None

def save_to_mysql(df):
    conn = connect_db()
    if conn is None:
        return

    cursor = conn.cursor()

    for _, row in df.iterrows():
        try:
            cursor.execute("""
                INSERT INTO tournament_results (username, rating, player_rank, score)
                VALUES (%s, %s, %s, %s)
            """, (row['username'], row['rating'], row['rank'], row['score']))
        except Error as e:
            print(f"❌ Error inserting data: {e}")

    conn.commit()
    print("✅ Data successfully saved to MySQL")
    cursor.close()
    conn.close()
