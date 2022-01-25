from dotenv import load_dotenv
import sqlite3, os

load_dotenv()

DB_PATH = os.getenv('DB_PATH')
SH_PATH = os.getenv('SH_PATH')

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

c.execute('SELECT Link FROM Monitors')
results = c.fetchall()

if results:
    for link in results:
        os.system(f'./{SH_PATH} {link}')
else:
    print('[!] Empty Database')
    exit()
