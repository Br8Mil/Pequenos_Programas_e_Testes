import PySimpleGUI as sg

sg.theme('BluePurple')
layout = [
[sg.Text('Valor 1'), sg.Input(key='v1', size=15), sg.Text('Valor 2'), sg.Input(key='v2', size=15)],
[sg.Text('Valor 3'), sg.Input(key='v3', size=15), sg.Text('X')],
[sg.Button('Calcular')],
[sg.Text('', key= 'resposta_simples')],
[sg.Button('Mostrar Conta')],
[sg.Text('', key= 'resposta_completa')]
]


window = sg.Window('Regra de Três Simples', layout)

while True:
    events, values = window.read()
    if events == sg.WIN_CLOSED:
        break
    if events == 'Calcular':
        p1 = (float(values['v1']))
        p2 = (float(values['v2']))
        p3 = (float(values['v3']))
        resultado = (p2 * p3) / p1
        window['resposta_simples'].update(f"    {p1} está para {p2} assim como {p3} está para X, sendo X = {resultado}")


    if events == 'Mostrar Conta':
        window['resposta_completa'].update(f'''
        {float(values['v1'])} - {float(values['v2'])}
        {float(values['v3'])} - X
            
        {float(values['v1'])}x = {float(values['v3'])} * {float(values['v2'])}
        {float(values['v1'])}x = {float(values['v3']) * float(values['v2'])}
        x = {(float(values['v3']) * float(values['v2']))} / {float(values['v1'])}

        x = {resultado}''')

window.close()