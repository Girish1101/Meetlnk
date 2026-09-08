import psycopg

passwords = [
    "postgres", "password", "root", "admin", "1234", "12345", "123456", "12345678",
    "meetink", "Girish1101", "girish", "", "postgres123", "admin123", "root123",
    "pass", "password123", "meetink123", "gep", "summerintern", "intern", "Postgres",
    "Postgres123", "PostgreSQL", "postgresql", "123456789"
]
users = ["postgres", "ASUS"]

found = False
for u in users:
    for p in passwords:
        try:
            conn = psycopg.connect(f"host=127.0.0.1 port=5432 user={u} password={p} dbname=postgres connect_timeout=1")
            print(f"SUCCESS! User={u}, Password={p}")
            conn.close()
            found = True
            break
        except Exception as e:
            pass
    if found:
        break

if not found:
    print("No default password matched.")
