import flet as ft
from utiles.all_variables import list_of_names_of_main_pages, selected_language


class HomePage:
    def __init__(self):
        self.selected_language = selected_language
        self.name = list_of_names_of_main_pages[self.selected_language]['pages']['home']['name']
        self.content_page = ft.Column()

    def create_content_page(self):
        self.content_page.controls.append(ft.TextButton(
            text='go to - Heroes page',
            on_click=lambda ev: self.go_to_page(ev, list_of_names_of_main_pages['eng']['pages']['heroes']['key'])
        ))

        self.content_page.controls.append(ft.TextButton(
            text='go to - Task manager page',
            on_click=lambda ev: self.go_to_page(
                ev,
                list_of_names_of_main_pages['eng']['pages']['task_manager']['key'])
        ))

        self.content_page.controls.append(ft.TextButton(
            text=f"go to - Birthday's page",
            on_click=lambda ev: self.go_to_page(
                ev,
                list_of_names_of_main_pages['eng']['pages']['birthday']['key'])
        ))

        self.content_page.controls.append(ft.Text(f"{self.name}"))
        return self.content_page

    def go_to_page(self, event, page_name):
        event.page.go(f"/main_pages/{page_name}")
