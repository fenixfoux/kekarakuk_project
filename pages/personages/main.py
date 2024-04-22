import flet as ft
from utiles.all_variables import all_persons as persons, list_of_names_of_main_pages, selected_language


class MainHeroes:
    def __init__(self):
        self.selected_language = selected_language
        self.name = list_of_names_of_main_pages[self.selected_language]['pages']['heroes']['name']
        self.content_page = ft.Column()

    def create_content_page(self):
        self.content_page.controls.append(ft.Text(f"{self.name}"))
        for person in persons["eng"]:
            self.content_page.controls.append(
                ft.ElevatedButton(
                    text=f"Go to {person['name']}'s page",
                    on_click=lambda ev, pers_id=person['id']: self.go_to_person_page(ev, pers_id)
                ))

        return self.content_page

    def go_to_person_page(self, event, person_id):
        event.page.go(f'/hero_page/{person_id}')
