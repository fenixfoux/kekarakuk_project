import datetime
import flet as ft

from utiles.all_variables import list_of_names_of_main_pages, selected_language


class MainBirthdays:
    def __init__(self):
        self.selected_language = selected_language
        self.name = list_of_names_of_main_pages[self.selected_language]['pages']['birthday']['name']
        self.header_section = ft.Column()

        self.content_page = ft.Column()

    def create_header_section(self):
        header = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row(
                    controls=[ft.Text(f"This is {self.name}"), ]
                ),
                ft.Row([
                    ft.ElevatedButton('home', on_click=self.go_home),
                    ft.ElevatedButton('new birthday', on_click=lambda ev: self.modal_confirm_dialog(ev))
                ])
            ]
        )
        self.header_section.controls.append(header)

        return self.header_section

    def create_content_page(self):
        self.content_page.controls.append(self.create_header_section())
        return self.content_page

    def modal_confirm_dialog(self, ev):
        full_name = ft.TextField(label='full name', hint_text='full name')
        details = ft.TextField(label='details', hint_text='some details')
        selected_date = ft.Text(f"{datetime.date.today()}")
        def change_date(e):
            selected_date.value = date_picker.value.date()
            e.control.page.update()

        def date_picker_dismissed(e):
            date_picker.value = datetime.datetime.now().date()

        date_picker = ft.DatePicker(
            on_change=change_date,
            on_dismiss=date_picker_dismissed,
            first_date=datetime.datetime(1900, 1, 1),
            last_date=datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day),
        )
        self.content_page.controls.append(date_picker)

        date_button = ft.IconButton(
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda _: date_picker.pick_date(),
        )

        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text(f"new person's birthday"),
            content=ft.Column(
                tight=True,
                controls=[
                    full_name,
                    details,
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.START,
                                controls=[ft.Text('Select birthday:'), selected_date]
                            ),
                            date_button]
                    )
                ]
            ),
            actions=[
                ft.TextButton("Yes",
                              on_click=lambda e: add_birthday(
                                  e,
                                  person_name=full_name.value,
                                  person_details=details.value,
                                  person_birthday=date_picker.value.date()
                              )),
                ft.TextButton("No", on_click=lambda e: close_dlg(e, False)),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        ev.control.page.dialog = dlg
        dlg.open = True
        ev.control.page.update()

        def add_birthday(e, person_name, person_details , person_birthday):
            print(f"="*50)
            print(f"person_name: {person_name}")
            print(f"person_details: {person_details}")
            print(f"person_birthday: {person_birthday}")
            print(f"="*50)
            dlg.open = False
            e.control.page.update()


        def close_dlg(e, confirmed: bool):
            print(confirmed)
            dlg.open = False
            e.control.page.update()

    def go_home(self, event):
        event.page.go('/')
