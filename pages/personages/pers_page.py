import flet as ft

from pages.personages.bottom_nav_bar import bottom_navigation_bar
from utiles.all_variables import all_persons as persons, list_of_names_of_main_pages


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

        self.content_page.controls.append(ft.TextButton(
            text='go to Heroes page',
            on_click=lambda ev: self.go_to_page(ev, list_of_names_of_main_pages['eng']['pages']['heroes']['key'])
        ))
        return self.content_page

    def go_home(self, event):
        event.page.go('/')

    def go_to_page(self, event, page_name):
        event.page.go(f"/main_pages/{page_name}")
