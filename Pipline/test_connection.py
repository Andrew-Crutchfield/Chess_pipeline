import mysql.connector
import config

def test_db_connection():
    try:
        conn = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME
        )
        
        if conn.is_connected():
            print("✅ Successfully connected to the MySQL database!")
            cursor = conn.cursor()
            
            cursor.execute("SHOW TABLES;")
            tables = cursor.fetchall()
            
            if tables:
                print("Tables in the database:")
                for table in tables:
                    print(f" - {table[0]}")
            else:
                print("❗ No tables found in the database.")
                
            cursor.close()
        else:
            print("❌ Failed to connect.")
            
    except mysql.connector.Error as e:
        print(f"❌ Error: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()
            print("✅ Connection closed.")

if __name__ == "__main__":
    test_db_connection()
