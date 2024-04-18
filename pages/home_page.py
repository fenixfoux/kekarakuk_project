import flet as ft
from utiles.all_variables import all_persons as persons

class HomePage:
    def __init__(self):
        self.name = 'home page'
        self.content_page = ft.Column()

    def create_content_page(self):
        self.content_page.controls.append(ft.Text(f"This is home page"))
        for person in persons["eng"]:
            self.content_page.controls.append(
                ft.ElevatedButton(
                    text=f"Go to {person['name']}'s page",
                    on_click=lambda ev, pers_id=person['id']: self.go_to_person_page(ev, pers_id)
                ))
        return self.content_page

    def go_to_person_page(self, event, person_id):
        event.page.go(f'/pers_page/{person_id}')