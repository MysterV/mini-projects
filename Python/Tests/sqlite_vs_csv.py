import pandas as pd
import sqlite3
import numpy as np
import time
import os
from pprint import pprint


NUM_ROWS = 100000
NUM_COLUMNS = 100


# Generate table
data = pd.DataFrame(np.random.rand(NUM_ROWS, NUM_COLUMNS),
                    columns=[f'col_{i}' for i in range(NUM_COLUMNS)])



# 1. CSV Performance Test
csv_file = 'test_data.csv'

# write to CSV file
start_csv_write = time.time()
data.to_csv(csv_file, index=False)
end_csv_write = time.time()

# read from CSV file
start_csv_read = time.time()
csv_data = pd.read_csv(csv_file)
end_csv_read = time.time()
os.remove(csv_file)



# 2. SQLite Performance Test
sqlite_file = 'test_data.sqlite'
conn = sqlite3.connect(sqlite_file)

# write to sqlite db file
start_sqlite_write = time.time()
data.to_sql('test_table', conn, if_exists='replace', index=False)
end_sqlite_write = time.time()

# read from sqlite db file
start_sqlite_read = time.time()
sqlite_data = pd.read_sql('SELECT * FROM test_table', conn)
end_sqlite_read = time.time()
conn.close()
os.remove(sqlite_file)



# Results
results = {
    "CSV Write Time (s)": end_csv_write - start_csv_write,
    "CSV Read Time (s)": end_csv_read - start_csv_read,
    "SQLite Write Time (s)": end_sqlite_write - start_sqlite_write,
    "SQLite Read Time (s)": end_sqlite_read - start_sqlite_read
}
pprint(results)
