import flet as ft
import random

def main(page: ft.Page):
    # Dark grey theme setup
    page.bgcolor = "#1E1E1E"  # Solid dark grey background
    page.title = "Number generator  "
    page.window_full_s_screen = True
    page.padding = 0
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # UI elements
    number_display = ft.Text(
        "0",
        size=100,
        weight="bold",
        color=ft.Colors.WHITE
    )

    generate_button = ft.ElevatedButton(
        "Generate",
        bgcolor="#333333",  # Dark grey button
        color=ft.Colors.WHITE,
        width=300,
        height=60,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            padding=20,
            overlay_color="#404040",  # Slightly lighter on press
        )
    )

    github_link = ft.Text(
        "GitHub: d3fpy",
        size=16,
        color=ft.Colors.WHITE70  # Slightly transparent white
    )

    # Layout
    content = ft.Column(
        [
            number_display,
            generate_button,
            github_link,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=40
    )

    # Button functionality
    def generate_random(e):
        number_display.value = str(random.randint(1, 100))
        page.update()

    generate_button.on_click = generate_random
    github_link.on_click = lambda e: page.launch_url("https://github.com/d3fpy")

    page.add(content)

ft.app(target=main)