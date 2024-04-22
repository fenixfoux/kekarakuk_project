import flet as ft


class TaskManager:
    def __init__(self):
        self.name = 'Task manager'
        self.content_page = ft.Column()

    def create_content_page(self):
        self.content_page.controls.append(ft.Text(f"This is {self.name} page"))
        self.content_page.controls.append(ft.ElevatedButton('Go home', on_click=self.go_home))
        return self.content_page

    def go_home(self, event):
        event.page.go('/')
