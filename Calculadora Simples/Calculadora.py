import PySimpleGUI as sg

sg.theme('DarkAmber')

janela = [
[sg.Text('Valor 1'), sg.Input(key='v1',size=(15,0),justification='center'), sg.Text('Valor 2'), sg.Input(key='v2',size=(15,0),justification='center')],
[sg.Text('')],
[sg.Button('+',size=(8,0)), sg.Button('-',size=(8,0)), sg.Button('X',size=(8,0)), sg.Button('/',size=(8,0))],
[sg.Text('')],
[sg.Button('Calcular'), sg.Text('', key= 'message')],
]


window = sg.Window('Calculadora Simples', layout=janela)
resultado = 0

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '+':
        resultado = values['v1'] + values['v2']
    if event == '-':
        resultado = values['v1'] - values['v2']
    if event == '*':
        resultado = values['v1'] * values['v2']
    if event == '/':
        resultado = values['v1'] / values['v2']
    if event == 'Calcular':
        window['message'].update(f'                     O Resultado e {resultado}')