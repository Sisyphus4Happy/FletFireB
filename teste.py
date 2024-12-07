import flet as ft

def main(page: ft.Page):
    # Configurações gerais da página
    page.title = "App de Estudos"
    page.window_width = 800
    page.window_height = 600

    # Cabeçalho
    header = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("EstudosApp", style="headlineMedium", expand=True),
                ft.IconButton(icon=ft.icons.NOTIFICATIONS, tooltip="Notificações"),
                ft.IconButton(icon=ft.icons.PERSON, tooltip="Perfil"),
            ],
            alignment="spaceBetween",
        ),
        padding=ft.padding.all(20),
        bgcolor=ft.colors.BLUE_50,
        height=60,
    )

    # Menu lateral
    menu = ft.Container(
        content=ft.Column(
            controls=[
                ft.IconButton(icon=ft.icons.HOME, tooltip="Início"),
                ft.IconButton(icon=ft.icons.BOOK, tooltip="Meus Flashcards"),
                ft.IconButton(icon=ft.icons.BAR_CHART, tooltip="Progresso"),
                ft.IconButton(icon=ft.icons.SETTINGS, tooltip="Configurações"),
            ],
            alignment="center",
            spacing=20,
        ),
        width=70,
        bgcolor=ft.colors.BLUE_100,
        padding=ft.padding.all(10),
    )

    # Conteúdo principal
    main_content = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Bem-vindo(a) ao EstudosApp!", style="headlineLarge"),
                ft.Text("Escolha uma opção abaixo para começar.", style="bodyMedium"),
                ft.Row(
                    controls=[
                        ft.ElevatedButton("Criar Flashcards", icon=ft.icons.ADD),
                        ft.ElevatedButton("Revisar Flashcards", icon=ft.icons.VISIBILITY),  # Substituído por VISIBILITY
                    ],
                    alignment="center",
                    spacing=20,
                ),
                ft.Divider(height=20),
                ft.Text("Seus estudos recentes", style="headlineSmall"),
                ft.ListView(
                    controls=[
                        ft.ListTile(
                            title=ft.Text("Matemática: Funções"),
                            subtitle=ft.Text("Última revisão: 2 dias atrás"),
                            leading=ft.Icon(ft.icons.BOOK),
                        ),
                        ft.ListTile(
                            title=ft.Text("História: Revolução Francesa"),
                            subtitle=ft.Text("Última revisão: 1 dia atrás"),
                            leading=ft.Icon(ft.icons.BOOK),
                        ),
                    ],
                    expand=True,
                ),
            ],
            spacing=20,
        ),
        padding=ft.padding.all(20),
        expand=True,
    )

    # Layout principal com cabeçalho, menu e área central
    page.add(
        ft.Row(
            controls=[
                menu,
                ft.Column(
                    controls=[
                        header,
                        main_content,
                    ],
                    expand=True,
                ),
            ],
        )
    )

# Executar o aplicativo
ft.app(target=main)
