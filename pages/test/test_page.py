import flet as ft
from pages.home_page import change_route
from pages.test.pers_class import OnePers
from utiles.all_variables import all_pers


class PageTest(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.selected_language = 'eng'
        self.pers_list = all_pers[self.selected_language]
        self.test_section = ft.Column()
        self.content_page = ft.Column()
        self.pers_content_page = ft.Column()

        self.associated_data = ''

        self.append_content_in_section()
        self.main()

    def append_content_in_section(self):
        # TRIED METHOD 1
        for element in self.pers_list:
            self.test_section.controls.append(
                ft.ElevatedButton(
                    key="/pers_page",
                    text=f"go to {str(element['name'])}'s page",
                    data=str(element['name']),
                    # on_click=lambda ev: change_route(ev),
                    # on_click=lambda ev: [self.test_func(ev), change_route(ev)],
                    on_click=lambda ev: self.test_func_1(ev),
                ),
            )
        # TRIED METHOD 2
        # another button and method but also i can't pass into new page anything, trying firstly to associate data to
        # a self.associated_data and later use that to fill ft.Text value
        self.test_section.controls.append(
                ft.ElevatedButton(
                    key="/pers_page_2",
                    text=f"go to thomas's page",
                    data=str('thomas'),
                    # on_click=lambda ev: change_route(ev),
                    on_click=lambda ev: [self.associate_data(ev), change_route(ev)],
                ),
        )

    # TRIED METHOD 1 FUNCTION
    def test_func_1(self, event):
        person_name = event.control.data
        self.pers_content_page.controls.append(ft.Text(person_name))
        self.pers_content_page.controls.append(ft.Text("O_o"))
        print(self.pers_content_page.controls)  # here I see that controls was added successfully

        change_route(event)

    # TRIED METHOD 2 FUNCTIONS
    def associate_data(self, event):
        self.associated_data = event.control.data
        print(f"self.associated_data: {self.associated_data}")

    def create_pers_page_content(self):
        self.pers_content_page.controls.append(ft.Text("O_o"))
        self.pers_content_page.controls.append(ft.Text(self.associated_data))  # field is generated but empty
        self.pers_content_page.controls.append(ft.Text("o_O"))
        return self.pers_content_page

    def main(self):
        self.content_page.controls.append(ft.Text('test page'), )
        self.content_page.controls.append(
            ft.ElevatedButton(
                key='/',
                text='go home',
                on_click=lambda ev: change_route(ev)
            ),
        )
        self.content_page.controls.append(self.test_section)
