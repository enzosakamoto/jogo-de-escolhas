from PySimpleGUI import PySimpleGUI as sg

# Função para criar as janelas
def criarJanela_Principal():
    sg.theme('Reddit')
    layout = [
        [sg.Push(), sg.Text('Bem-vindo! Descubra qual macaco você é!'), sg.Push()],
        [sg.Push(), sg.Button('Ir', button_color=('black', 'white')), sg.Button('Sair', button_color=('black', 'white')), sg.Push()],
        [sg.Push(), sg.Text('Versão 1.1'), sg.Push(), sg.Button('?', button_color=('white', 'red'))]
    ]
    return sg.Window('Tela inicial', layout=layout, finalize=True, size=(300, 100))

def criarJanelas(botaoesquerda, botaodireita):
    sg.theme('Reddit')
    layout = [
        [sg.Push(), sg.Text('O que você prefere?'), sg.Push()],
        [sg.Push(), sg.Button(botaoesquerda, button_color=('white', 'red')), sg.Button(botaodireita, button_color=('white', 'darkblue')), sg.Push()],
        [sg.Push(), sg.Button('Voltar', button_color=('black', 'white')), sg.Push()]
    ]
    return sg.Window('Jogo', layout=layout, finalize=True, size=(300, 120))

# Inicializando as janelas
janela_login, janela2, janela3, janela4 = criarJanela_Principal(), None, None, None

# Eventos
while True:
    janela, eventos, valores = sg.read_all_windows()

    if janela in (janela_login, janela2, janela3, janela4) and eventos in (sg.WIN_CLOSED, 'Sair'):
        break

    # Próxima janela
    if janela == janela_login and eventos == '?':
        sg.popup('Esse jogo está em desenvolvimento, portanto, há poucas escolhas ainda.')

    if janela == janela_login and eventos == 'Ir':
        janela2 = criarJanelas('Matar seu cachorro no mine', 'Ser atropelado')
        janela_login.hide()

    if janela == janela2 and eventos == 'Matar seu cachorro no mine':
        janela3 = criarJanelas('Morrer', 'Viver')
        janela2.hide()

    if janela == janela2 and eventos == 'Ser atropelado':
        janela4 = criarJanelas('Frio', 'Calor')
        janela2.hide()

    # Voltar janela
    if janela == janela2 and eventos == 'Voltar':
        janela2.hide()
        janela_login.un_hide()

    if janela == janela3 and eventos == 'Voltar':
        janela3.hide()
        janela2.un_hide()

    if janela == janela4 and eventos == 'Voltar':
        janela4.hide()
        janela2.un_hide()

    # Leitura final dos botões
    if janela == janela3 and eventos == 'Morrer':
        janela3.hide()
        janela_login.un_hide()
        sg.popup('Você é um orangotango!')

    if janela == janela3 and eventos == 'Viver':
        janela3.hide()
        janela_login.un_hide()
        sg.popup('Você é um mico-leão dourado!')

    if janela == janela4 and eventos == 'Frio':
        janela4.hide()
        janela_login.un_hide()
        sg.popup('Você é um gorila!')

    if janela == janela4 and eventos == 'Calor':
        janela4.hide()
        janela_login.un_hide()
        sg.popup('Você é um babuíno!')

janela.close()