import flet as ft
from utiles.all_variables import all_persons as persons

class PersPage:
    def __init__(self, pers_id):
        self.pers_id = pers_id
        self.content_page = ft.Column()

    def create_content_page(self):
        current_pers = {}
        for one_pers in persons['eng']:
            if int(one_pers['id']) == int(self.pers_id):
                current_pers = one_pers.copy()

        self.content_page.controls.append(ft.Text(f"page id: {current_pers['id']}"))
        self.content_page.controls.append(ft.Text(f"This is {current_pers['name']}'s page"))
        self.content_page.controls.append(ft.Text(f"{current_pers['name']} is {current_pers['age']} years old"))
        self.content_page.controls.append(ft.Text(f"{current_pers['description']}"))
        self.content_page.controls.append(ft.ElevatedButton('Go home', on_click=self.go_home))
        return self.content_page

    def go_home(self, event):
        event.page.go('/')