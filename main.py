import sqlite3
import pandas as pd


def connect_to_db(db_name="school_attendance.db"):
    """
    Connect to an SQLite database and return the connection.
    """
    conn = sqlite3.connect(db_name)
    return conn


def create_table(conn, table_name, columns):
    """
    Create a table with the given columns.
    """
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});")
    conn.commit()


def insert_data(conn, table_name, csv_file):
    """
    Insert data from a CSV file into the specified table.
    """
    df = pd.read_csv(
        "https://github.com/nogibjj/Jiechen_Li_Mini_6_External_Database/"
        "raw/main/School_Attendance_by_Student_Group_and_District__2021-2022.csv"
    )
    df.to_sql(table_name, conn, if_exists="replace", index=False)


def read_data(conn, table_name):
    """
    Read data from the specified table and return as a dataframe.
    """
    return pd.read_sql(f"SELECT * FROM {table_name}", conn)


# ... [Your function definitions here]

if __name__ == "__main__":
    conn = connect_to_db("school_attendance_db.db")
    insert_data(
        conn,
        "school_attendance_db",
        (
            "https://github.com/nogibjj/Jiechen_Li_Mini_6_External_Database/"
            "raw/main/School_Attendance_by_Student_Group_and_District__2021-2022.csv"
        ),
    )
    data = read_data(conn, "school_attendance_db")
    print(data.head())
