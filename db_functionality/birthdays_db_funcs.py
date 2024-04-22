import sqlite3 as sq
import os

from pages.birthdays.person import Person
from utiles.all_variables import birthdays_db_filepath, birthdays_table_name



def check_for_db():
    if not os.path.exists(birthdays_db_filepath):
        # con = sq.connect(todo_db_filepath)
        # con.commit()
        # con.close()
        create_empty_tables()

def create_empty_tables():
    """that function will be used for create empty tables when the app will be firstly started"""
    db = sq.connect(birthdays_db_filepath)
    cur = db.cursor()
    create_todo_table_sql = (f"CREATE TABLE IF NOT EXISTS {birthdays_table_name} "
                             f"( "
                             f"task_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                             f"parent_task_id INTEGER,"
                             f"task_name TEXT,"
                             f"task_description TEXT,"
                             f"task_status TEXT,"
                             f"task_created_date TEXT, "
                             f"task_due_date TEXT, "
                             f"task_is_favorite TEXT "
                             f" )")
    cur.execute(create_todo_table_sql)

    db.commit()
    db.close()