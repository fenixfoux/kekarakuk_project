import flet as ft

from pages.pages_router import page_route_change_handler


def main(one_page: ft.Page):
    # print(one_page.window_height)
    # print(one_page.window_width)

    # todo: check for data bases, and create them if doesn't exist

    one_page.on_route_change = lambda _: page_route_change_handler(one_page)
    one_page.go(one_page.route)

    one_page.update()


ft.app(target=main)
