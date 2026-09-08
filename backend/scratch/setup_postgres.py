import psycopg

conn = psycopg.connect("host=127.0.0.1 port=5432 user=postgres password=PostgreSQL dbname=postgres", autocommit=True)
cur = conn.cursor()

cur.execute("SELECT datname FROM pg_database WHERE datname = 'meetink'")
exists = cur.fetchone()

if not exists:
    print("Database 'meetink' does not exist. Creating...")
    cur.execute("CREATE DATABASE meetink")
    print("Database 'meetink' created successfully!")
else:
    print("Database 'meetink' already exists.")

conn.close()

# Now connect to meetink and create extension vector
conn_meetink = psycopg.connect("host=127.0.0.1 port=5432 user=postgres password=PostgreSQL dbname=meetink", autocommit=True)
cur_m = conn_meetink.cursor()
try:
    cur_m.execute("CREATE EXTENSION IF NOT EXISTS vector;")
    print("Vector extension enabled successfully!")
except Exception as e:
    print(f"Vector extension note: {e}")
conn_meetink.close()
