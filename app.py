from flet import *
import flet as ft
import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyDRb86eWPxX1rsBDQ2C3rv1D51jb6ca9uU",
    'authDomain': "prepwise-24331.firebaseapp.com",
    'projectId': "prepwise-24331",
    'storageBucket': "prepwise-24331.firebasestorage.app",
    'databaseURL': "https:prepwise.firebaseio.com",
    'messagingSenderId': "942619832045",
    'appId': "1:942619832045:web:628aac95b808bd6af7e6e4",
    'measurementId': "G-H5JYMCJMNM"
    }
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def main(page: ft.Page):
    
    # Função para alternar a visibilidade da senha
    def toggle_password_visibility(e):        
        txt_senha.password = not txt_senha.password  # Alterna a visibilidade da senha
        icon_eye.icon = ft.icons.VISIBILITY if txt_senha.password else ft.icons.VISIBILITY_OFF  # Altera o ícone
        page.update()  # Atualiza a página para refletir a mudança
    txt_senha = ft.TextField(
            label="Informe sua senha", 
            text_align=ft.TextAlign.LEFT,
            text_style=ft.TextStyle(size=15, weight="bold"),
            width=260,  # Ligeiramente menor para encaixar o ícone
            border_radius=10,
            max_length=30,
            password=True,  # Esconder a senha por padrão
            )
    icon_eye = ft.IconButton(
            icon=ft.icons.VISIBILITY_OFF,  # Começa com o ícone de olho fechado
            on_click=toggle_password_visibility
        )
    # Função para gerenciar as rotas
    def on_route_change(e):
        page.views.clear()  # Limpa as views para adicionar a nova tela



        def btnEntrar(e):
            try:
                auth.sign_in_with_email_and_password(user_email.value, txt_senha.value)
                #page.go("/tela_usuario")
                page.snack_bar = ft.SnackBar(
                    content= ft.Text(value='Você entrou'),
                    bgcolor = 'green',
                    action='Ok',
                    duration = 3000
                )
                page.snack_bar.open = True
                user_email.value=None
                txt_senha.value=None
                page.update()

            except:
                page.snack_bar = ft.SnackBar(
                    content= ft.Text(value='Email ou senha errados'),
                    bgcolor = 'red',
                    action='Reescreva os campos',
                    duration = 3000
                )
                page.snack_bar.open = True
                user_email.value=None
                txt_senha.value=None
                page.update()
        
        
        
        
        # Tela de login
        if page.route == "/login":
            # Definindo o título da página
            page.title = "PrepWise"

            # Coloca o campo de senha e o botão de olho na mesma linha
            #senha_row = ft.Row(
            #    controls=[txt_senha, icon_eye],  # Coloca o campo de senha e o ícone na mesma linha   
            #    alignment=ft.MainAxisAlignment.CENTER
            #)
            
            user_email = ft.TextField(
                label="Informe seu email", 
                text_align=ft.TextAlign.LEFT,
                text_style=ft.TextStyle(size=15, weight="bold"),
                width=310,
                border_radius=10,
                color="Blue",
                )
            entrar = ft.ElevatedButton("Entrar", on_click=btnEntrar)

            # Adiciona a view de login à página
            page.views.append(
                ft.View(
                    "/login",
                    [
                        
                        ft.Text('Login', size=30, weight="bold"),


                        # Campo de email
                        user_email,
                        
                        
                        # Adiciona a linha com o campo de senha e o ícone
                        txt_senha,

                        # Botão de entrar redirecionando para /tela_inicial
                        #ft.ElevatedButton("Entrar", on_click=lambda _: page.go("/tela_inicial")),
                        entrar,
                        
                        ft.ElevatedButton("Não possui cadastro?", on_click=lambda _: page.go("/tela_cadastro")),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                )
            )
        #Tela Inicial
        elif page.route == "/tela_inicial":
            # Tela inicial
            page.views.append(
                ft.View(
                    "/tela_inicial",
                    [
                        ft.Text("Bem-vindo ao PrepWise", size=30, weight="bold"),

                        ft.ElevatedButton(
                            "Ir para Login", 
                            on_click=lambda _: page.go("/login"),
                        ),
                    ],
                    #horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    #vertical_alignment=ft.MainAxisAlignment.CENTER,
                )
            )
        elif page.route == "/tela_usuario":
            # Tela inicial
            page.views.append(
                ft.View(
                    "/tela_usuario",
                    [
                        ft.Text("Seu dissimulado", size=30, weight="bold"),

                        ft.ElevatedButton(
                            "Ir para Login", 
                            on_click=lambda _: page.go("/login"),
                        ),
                    ],
                    #horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    #vertical_alignment=ft.MainAxisAlignment.CENTER,
                )
            )
        elif page.route == "/tela_cadastro":
            ft.title = "PrepWise - Cadastro"
            senha_row = ft.Row(
                controls=[txt_senha, icon_eye],  # Coloca o campo de senha e o ícone na mesma linha   
                alignment=ft.MainAxisAlignment.CENTER
            )

            usuario_name = ft.TextField(
                label="Informe seu nome", 
                text_align=ft.TextAlign.LEFT,
                text_style=ft.TextStyle(size=15, weight="bold"),
                width=310,
                border_radius=10,
                color="Blue",
                )
            usuario_email_cadastro = ft.TextField(
                label="Informe seu email", 
                text_align=ft.TextAlign.LEFT,
                text_style=ft.TextStyle(size=15, weight="bold"),
                width=310,
                border_radius=10,
                color="Blue",
                        )
            #tela de cadastro
            page.views.append(
                ft.View(
                    "/tela_cadastro",[
                        ft.Text("Tela de cadastro"),

                        # Campo de nome completo
                        usuario_name,

                        # Campo de email
                        usuario_email_cadastro,
                        
                        # Adiciona a linha com o campo de senha e o ícone
                        senha_row,

                        # Botão de entrar redirecionando para /tela_inicial
                        ft.ElevatedButton("Cadastrar", on_click=lambda _: page.go("/tela_inicial")),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,

                    
                )
            )
        page.update()  # Atualiza a página com a nova view
    
    page.on_route_change = on_route_change

    # Defina a rota inicial (primeira tela)
    page.go("/login")

ft.app(target=main)