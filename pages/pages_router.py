import flet as ft

from pages.birthdays.main import MainBirthdays
from pages.home_page import HomePage
from pages.personages.main import MainHeroes
from pages.personages.pers_page import PersPage
from pages.task_manager.main import TaskManager


def page_route_change_handler(page):
    home_page = HomePage().create_content_page()
    pages = {
        '/': ft.View(
            "/",
            [home_page],
        ),
    }
    if page.route.startswith('/main_pages'):
        page_key = page.route.split('/')[-1]
        if page_key == "heroes":
            heroes_page = MainHeroes().create_content_page()
            pages[page.route] = ft.View(
                route=page.route,
                controls=[heroes_page]
            )
        elif page_key == "task_manager":
            task_manager_page = TaskManager().create_content_page()
            pages[page.route] = ft.View(
                route=page.route,
                controls=[task_manager_page]
            )
        elif page_key == "birthday":
            birthday_page = MainBirthdays().create_content_page()
            pages[page.route] = ft.View(
                route=page.route,
                controls=[birthday_page]
            )

    if page.route.startswith('/hero_page'):
        person_id = page.route.split('/')[-1]
        pers_page = PersPage(person_id).create_content_page()
        pages[page.route] = ft.View(
            route=page.route,
            controls=[pers_page]
        )

    page.views.clear()
    page.views.append(pages.get(page.route, pages['/']))
    page.update()