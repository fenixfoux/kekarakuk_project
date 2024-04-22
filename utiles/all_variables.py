"""file for all variables in all languages"""

# DATA BASE
storage_path = './storages/'

birthdays_db_name = 'birthdays_db.db'
birthdays_table_name = 'todo'
birthdays_db_filepath = storage_path + birthdays_db_name

all_persons = {
    'eng': [
        {
            'id': 34253,
            'name': 'ignis',
            'age': 51,
            'description': "some personage details"
        },
        {
            'id': 234534,
            'name': 'argent',
            'age': 42,
            'description': "some personage details"
        },
        {
            'id': 5435,
            'name': 'katty',
            'age': 37,
            'description': "some personage details"
        },
    ]
}
selected_language = 'eng'
list_of_names_of_main_pages = {
    'eng': {
        'pages': {
            'home': {
                'key': 'home',
                'name': "Home page"
            },
            'heroes': {
                'key': "heroes",
                'name': "Heroes page"
            },
            'task_manager': {
                'key': 'task_manager',
                'name': "Task manager page"
            },
            'birthday': {
                'key': 'birthday',
                'name': "Birthday page"
            },
        }
    },
    'rus': {
        'pages': {
            'home': {
                'key': 'home',
                'name': "Домашняя страница"
            },
            'heroes': {
                'key': "heroes",
                'name': "Страница героев"
            },
            'task_manager': {
                'key': 'task_manager',
                'name': "Менеджер задач"
            },
            'birthday': {
                'key': 'birthday',
                'name': "Дни рождения"
            },
        }
    }
}

# print(list_of_names_of_main_pages['eng'])
