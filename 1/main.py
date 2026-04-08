import flet as ft

def main(page: ft.Page):
    # Мобильные настройки для Android
    page.title = "Финансы"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = ft.padding.only(top=25, left=16, right=16, bottom=10)
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.bgcolor = ft.Colors.WHITE
    
    # Отключаем скролл для всей страницы (будем использовать скролл в колонках)
    page.scroll = None
    
    # Получаем размер экрана (адаптивно)
    screen_width = page.width if page.width else 400
    
    # ========== ФУНКЦИИ СТРАНИЦ ==========
    
    def show_finances_page(e):
        """Страница Финансы"""
        page.clean()
        page.add(
            ft.Column(
                [
                    ft.Container(height=20),
                    ft.Text("💰 Финансы", size=28, weight=ft.FontWeight.BOLD),
                    ft.Container(height=10),
                    ft.Text("Здесь будет подробная статистика", size=16, color=ft.Colors.GREY_600),
                    ft.Text("📊 Графики расходов", size=14, color=ft.Colors.GREY_500),
                    ft.Text("📈 Анализ трат", size=14, color=ft.Colors.GREY_500),
                    ft.Container(height=30),
                    ft.ElevatedButton(
                        "← На главную", 
                        on_click=show_main_page,
                        bgcolor=ft.Colors.BLUE_400, 
                        color=ft.Colors.WHITE,
                        width=200,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
                scroll=ft.ScrollMode.AUTO,  # Добавляем скролл для длинного контента
            )
        )
        page.update()
    
    def show_ai_page(e):
        """Страница AI"""
        page.clean()
        page.add(
            ft.Column(
                [
                    ft.Container(height=20),
                    ft.Text("🤖 AI", size=28, weight=ft.FontWeight.BOLD),
                    ft.Container(height=10),
                    ft.Text("Здесь будет искусственный интеллект", size=16, color=ft.Colors.GREY_600),
                    ft.Text("💡 Персональные советы", size=14, color=ft.Colors.GREY_500),
                    ft.Text("📊 Анализ трат", size=14, color=ft.Colors.GREY_500),
                    ft.Text("💰 Прогноз бюджета", size=14, color=ft.Colors.GREY_500),
                    ft.Container(height=30),
                    ft.ElevatedButton(
                        "← На главную", 
                        on_click=show_main_page,
                        bgcolor=ft.Colors.BLUE_400, 
                        color=ft.Colors.WHITE,
                        width=200,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
                scroll=ft.ScrollMode.AUTO,
            )
        )
        page.update()
    
    def show_support_page(e):
        """Страница Поддержка"""
        page.clean()
        page.add(
            ft.Column(
                [
                    ft.Container(height=20),
                    ft.Text("🎧 Поддержка", size=28, weight=ft.FontWeight.BOLD),
                    ft.Container(height=10),
                    ft.Text("Свяжитесь с нами", size=16, color=ft.Colors.GREY_600),
                    ft.Text("📧 support@financeapp.com", size=14, color=ft.Colors.BLUE),
                    ft.Text("📞 +7 (999) 123-45-67", size=14, color=ft.Colors.BLUE),
                    ft.Container(height=20),
                    ft.Text("Часто задаваемые вопросы:", size=16, weight=ft.FontWeight.BOLD),
                    ft.Text("❓ Как добавить операцию?", size=14),
                    ft.Text("❓ Как изменить валюту?", size=14),
                    ft.Text("❓ Как удалить операцию?", size=14),
                    ft.Container(height=30),
                    ft.ElevatedButton(
                        "← На главную", 
                        on_click=show_main_page,
                        bgcolor=ft.Colors.BLUE_400, 
                        color=ft.Colors.WHITE,
                        width=200,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
                scroll=ft.ScrollMode.AUTO,
            )
        )
        page.update()
    
    def show_settings_page(e):
        """Страница Настройки"""
        page.clean()
        page.add(
            ft.Column(
                [
                    ft.Container(height=20),
                    ft.Text("⚙️ Настройки", size=28, weight=ft.FontWeight.BOLD),
                    ft.Container(height=10),
                    ft.Text("Настройки приложения", size=16, color=ft.Colors.GREY_600),
                    ft.Container(height=20),
                    ft.Text("Валюта:", size=16, weight=ft.FontWeight.BOLD),
                    ft.Row([
                        ft.TextButton("$ USD", on_click=lambda _: show_toast("USD выбран")),
                        ft.TextButton("€ EUR", on_click=lambda _: show_toast("EUR выбран")),
                        ft.TextButton("₽ RUB", on_click=lambda _: show_toast("RUB выбран")),
                    ]),
                    ft.Container(height=20),
                    ft.Text("Тема:", size=16, weight=ft.FontWeight.BOLD),
                    ft.Row([
                        ft.TextButton("🌞 Светлая", on_click=lambda _: show_toast("Светлая тема")),
                        ft.TextButton("🌙 Темная", on_click=lambda _: show_toast("Темная тема")),
                    ]),
                    ft.Container(height=30),
                    ft.ElevatedButton(
                        "← На главную", 
                        on_click=show_main_page,
                        bgcolor=ft.Colors.BLUE_400, 
                        color=ft.Colors.WHITE,
                        width=200,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
                scroll=ft.ScrollMode.AUTO,
            )
        )
        page.update()
    
    def show_toast(message):
        """Показывает временное сообщение"""
        page.snack_bar = ft.SnackBar(content=ft.Text(message), duration=2000)
        page.snack_bar.open = True
        page.update()
    
    # ========== ГЛАВНАЯ СТРАНИЦА ==========
    
    def show_main_page(e=None):
        """Показывает главную страницу"""
        page.clean()
        
        # Статус бар с временем
        time_row = ft.Row(
            [ft.Text("10:45 AM", size=16, weight=ft.FontWeight.BOLD)],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        
        # Блок баланса
        balance_card = ft.Container(
            content=ft.Column([
                ft.Text("ОБЩИЙ БАЛАНС", size=14, color=ft.Colors.GREY_600),
                ft.Text("100 000 $", size=48, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN),
                ft.Text("💰 Доступно", size=12, color=ft.Colors.GREY_500),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
            padding=20,
            bgcolor=ft.Colors.GREY_100,
            border_radius=20,
            width=screen_width - 40 if screen_width else 360,
        )
        
        # Заголовок операций
        operations_title = ft.Text("Последние операции", size=20, weight=ft.FontWeight.BOLD)
        
        # Функция создания операции
        def create_operation(title, category, amount, time):
            return ft.Container(
                content=ft.Row([
                    ft.Column([
                        ft.Text(title, weight=ft.FontWeight.BOLD, size=16),
                        ft.Text(category, size=12, color=ft.Colors.GREY_600),
                    ], spacing=2),
                    ft.Container(expand=True),
                    ft.Column([
                        ft.Text(f"-{amount} $", color=ft.Colors.RED, weight=ft.FontWeight.BOLD, size=16),
                        ft.Text(time, size=12, color=ft.Colors.GREY_600),
                    ], horizontal_alignment=ft.CrossAxisAlignment.END, spacing=2),
                ]),
                padding=15,
                bgcolor=ft.Colors.WHITE,
                border=ft.border.all(1, ft.Colors.GREY_300),
                border_radius=12,
                margin=ft.margin.only(bottom=10),
                ink=True,  # Эффект нажатия
                on_click=lambda _: show_toast(f"Операция: {title} - {amount}$"),
            )
        
        # Список операций
        operations_list = ft.Column([
            create_operation("Супермаркет", '"Лента"', 20, "10:30"),
            create_operation("Аптека", '"Вита"', 10, "10:15"),
            create_operation("Кафе", '"Кофе и точка"', 15, "09:45"),
            create_operation("Транспорт", '"Такси"', 8, "Вчера"),
        ], spacing=0, scroll=ft.ScrollMode.AUTO, height=300)
        
        # Кнопка добавления операции
        add_button = ft.FloatingActionButton(
            icon=ft.icons.ADD,
            on_click=lambda _: show_toast("Добавление операции (будет позже)"),
            bgcolor=ft.Colors.BLUE_400,
            foreground_color=ft.Colors.WHITE,
        )
        
        # Нижнее меню (увеличено для пальцев)
        bottom_nav = ft.Container(
            content=ft.Row([
                ft.TextButton("💰", on_click=show_finances_page, 
                             style=ft.ButtonStyle(color=ft.Colors.BLUE, icon_size=28),
                             icon="wallet"),
                ft.TextButton("🤖", on_click=show_ai_page,
                             style=ft.ButtonStyle(color=ft.Colors.BLUE, icon_size=28),
                             icon="smart_toy"),
                ft.TextButton("🎧", on_click=show_support_page,
                             style=ft.ButtonStyle(color=ft.Colors.BLUE, icon_size=28),
                             icon="support_agent"),
                ft.TextButton("⚙️", on_click=show_settings_page,
                             style=ft.ButtonStyle(color=ft.Colors.BLUE, icon_size=28),
                             icon="settings"),
            ], alignment=ft.MainAxisAlignment.SPACE_AROUND),
            padding=ft.padding.only(top=10, bottom=10),
            bgcolor=ft.Colors.GREY_50,
            border=ft.border.only(top=ft.BorderSide(1, ft.Colors.GREY_300)),
        )
        
        # Основной контент с прокруткой
        main_content = ft.Column([
            time_row,
            ft.Container(height=10),
            balance_card,
            ft.Container(height=20),
            operations_title,
            ft.Container(height=10),
            operations_list,
        ], scroll=ft.ScrollMode.AUTO, spacing=0)
        
        # Добавляем всё на страницу
        page.add(main_content)
        page.add(bottom_nav)
        page.add(add_button)
        page.update()
    
    # Запускаем главную страницу
    show_main_page()

# Запуск для Android
if __name__ == "__main__":
    ft.app(target=main)