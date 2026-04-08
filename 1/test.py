import flet as ft

def main(page: ft.Page):
    # Если вы увидите этот заголовок, значит запустился НОВЫЙ код
    page.title = "ФИНАЛЬНАЯ ПРОВЕРКА" 
    page.window_width = 400
    page.window_height = 800
    page.bgcolor = "#F8FAF9"

    # Создаем шапку БЕЗ IconButton, чтобы точно не было ошибок
    header = ft.Row(
        controls=[
            ft.Icon("settings", color="black"),
            ft.Text("Мои финансы", size=22, weight="bold"),
            ft.Icon("person", color="black"),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    card = ft.Container(
        content=ft.Text("ЕСЛИ ВЫ ЭТО ВИДИТЕ - ВСЁ РАБОТАЕТ!", color="black", weight="bold"),
        bgcolor="#D1EEDD",
        padding=40,
        border_radius=20
    )

    page.add(header, ft.Divider(), card)
    page.update()

ft.app(target=main)