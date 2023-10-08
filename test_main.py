import main
import pandas as pd


def test_connect_to_db():
    conn_1 = main.connect_to_db()
    assert conn_1 is not None


def test_create_table():
    conn_1 = main.connect_to_db()
    main.create_table(conn_1, "test_table", "id INTEGER PRIMARY KEY, name TEXT")
    cursor = conn_1.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    assert ("test_table",) in tables


def test_insert_and_read_data():
    conn_1 = main.connect_to_db()
    main.create_table(
        conn_1,
        "test_table",
        (
            "id INTEGER PRIMARY KEY, "
            "District_code TEXT, "
            "District_name TEXT, "
            "Category TEXT, "
            "Student_group TEXT, "
            "Student_count INTEGER, "
            "Attendance_rate FLOAT"
        ),
    )
    main.insert_data(
        conn_1,
        "test_table",
        (
            "https://github.com/nogibjj/Jiechen_Li_Mini_6_External_Database/"
            "raw/main/School_Attendance_by_Student_Group_and_District__2021-2022.csv"
        ),
    )
    data = main.read_data(conn_1, "test_table")
    assert isinstance(data, pd.DataFrame)
    assert not data.empty
