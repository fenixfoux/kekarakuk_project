import flet as ft


def change_route(e: ft.RouteChangeEvent):
    e.page.route = e.control.key
    e.page.update()


class HomePage(ft.UserControl):
    def __init__(self):
        super().__init__()
        pass

    def main(self):
        content_page = ft.Column(
            controls=[
                ft.Text('home page'),
                ft.ElevatedButton(
                    key='/page_tests',
                    text='go to page test',
                    on_click=lambda ev: change_route(ev)
                ),
                ft.ElevatedButton(
                    key='/page_1',
                    text='not implemented yet',
                    on_click=lambda ev: change_route(ev),
                    disabled=True
                ),
                ft.ElevatedButton(
                    key='/page_2',
                    text='not implemented yet',
                    on_click=lambda ev: change_route(ev),
                    disabled=True
                ),
            ]
        )
        return content_page
