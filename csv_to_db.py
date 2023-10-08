import csv
import sqlite3

# Step 1: Read the CSV file
csv_file_path = (
    "/Users/castnut/Desktop/706_Data_Engineering/mini_6/"
    "Jiechen_Li_Mini_6_External_Database/"
    "School_Attendance_by_Student_Group_and_District__2021-2022.csv"
)
with open(csv_file_path, "r", newline="") as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # Get the header (column names)
    data = list(csv_reader)  # Get the rest of the data

# Step 2: Create a new SQLite database
db_file_path = (
    "/Users/castnut/Desktop/706_Data_Engineering/mini_6/"
    "Jiechen_Li_Mini_6_External_Database/school_attendance_db.db"
)
conn = sqlite3.connect(db_file_path)
cursor = conn.cursor()

# Step 3: Create a table in the database
# For this example, I'm assuming all columns have TEXT data type.
# You might want to modify this based on your actual data.
columns = ", ".join([f'"{col}" TEXT' for col in header])
create_table_query = f"CREATE TABLE IF NOT EXISTS db_table ({columns})"
print(create_table_query)
cursor.execute(create_table_query)


# Step 4: Insert data from CSV into the database table
placeholders = ", ".join(["?"] * len(header))
insert_query = f"INSERT INTO db_table VALUES ({placeholders})"
cursor.executemany(insert_query, data)

# Step 5: Commit and close
conn.commit()
conn.close()
