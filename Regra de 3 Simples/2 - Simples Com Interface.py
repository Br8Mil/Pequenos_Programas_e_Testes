import PySimpleGUI as sg

sg.theme('BluePurple')
janela = [
[sg.Text('Valor 1'), sg.Input(key='v1', size=15), sg.Text('Valor 2'), sg.Input(key='v2', size=15)],
[sg.Text('Valor 3'), sg.Input(key='v3', size=15), sg.Text('X')],
[sg.Button('Calcular'), sg.Text('', key= 'message')],
]

window = sg.Window('Regra de Três Simples', janela)

while True:
    events, values = window.read()
    if events == sg.WIN_CLOSED:
        break
    if events == 'Calcular':

        p1 = int(values['v1'])
        p2 = int(values['v2'])
        p3 = int(values['v3'])
        resultado = (p2*p3)/p1
        window['message'].update(f'                               O resultado de X = {resultado}')

window.close()