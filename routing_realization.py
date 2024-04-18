import flet as ft

# persons = ['ignis', 'argent', 'katty']
persons = {
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


class OnePers:
    def __init__(self, pers_id, pers_name, pers_age, pers_description):
        self.pers_id = pers_id
        self.pers_name = pers_name
        self.pers_age = pers_age
        self.pers_description = pers_description


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


def page_route_change_handler(page):
    home_page = HomePage().create_content_page()
    pages = {
        '/': ft.View(
            "/",
            [home_page],
        ),
    }

    if page.route.startswith('/pers_page'):
        person_id = page.route.split('/')[-1]
        pers_page = PersPage(person_id).create_content_page()
        pages[page.route] = ft.View(
            route=page.route,
            controls=[pers_page]
        )

    page.views.clear()
    page.views.append(pages.get(page.route, pages['/']))
    page.update()


def main(one_page: ft.Page):
    one_page.on_route_change = lambda _: page_route_change_handler(one_page)
    one_page.go(one_page.route)
    one_page.update()


ft.app(target=main)
