import PySimpleGUI as sg

sg.theme('BluePurple')
layout = [
[sg.Text('Valor 1'), sg.Input(key='v1', size=15), sg.Text('Valor 2'), sg.Input(key='v2', size=15)],
[sg.Text('Valor 3'), sg.Input(key='v3', size=15), sg.Text('Valor 4'), sg.Input(key='v4', size=15)],
[sg.Button('Resultado')],
[sg.Text('', key= 'resp_simples',)],
[sg.Button('Mostrar Conta')],
[sg.Text('', key= 'resp_completa')]
]


window = sg.Window('Regra de Três Simples', layout)

while True:
    events, values = window.read()
    if events == sg.WIN_CLOSED:
        break
    elif events == 'Resultado':
        if values['v1'] == 'x':
            p2 = (float(values['v2']))
            p3 = (float(values['v3']))
            p4 = (float(values['v4']))
            resultado = (p2 * p3) / p4
            window['resp_simples'].update(f"    X está para {p2}, assim como {p3} está para {p4}, sendo X = {resultado}")
        elif values['v2'] == 'x':
            p1 = (float(values['v1']))
            p3 = (float(values['v3']))
            p4 = (float(values['v4']))
            resultado = (p1 * p4) / p3
            window['resp_simples'].update(f"    {p1} está para X, assim como {p3} está para {p4}, sendo X = {resultado}")
        elif values['v3'] == 'x':
            p1 = (float(values['v1']))
            p2 = (float(values['v2']))
            p4 = (float(values['v4']))
            resultado = (p2 * p4) / p2
            window['resp_simples'].update(f"    {p1} está para {p2}, assim como X está para {p4}, sendo X = {resultado}")
        elif values['v4'] == 'x':
            p1 = (float(values['v1']))
            p2 = (float(values['v2']))
            p3 = (float(values['v3']))
            resultado = (p2 * p3) / p1
            window['resp_simples'].update(f"    {p1} está para {p2}, assim como {p3} está para X, sendo X = {resultado}")


    elif events == 'Mostrar Conta':
        if values['v1'] == 'x':
            window['resp_completa'].update(f'''
            {values['v1']} - {values['v2']}
            {values['v3']} - {values['v4']}
            
            {values['v4']}x = {values['v3']} * {values['v2']}
            {values['v4']}x = {float(values['v3']) * float(values['v2'])}
            x = {float(values['v3']) * float(values['v2'])} / {float(values['v4'])}

            x = {(float(values['v3']) * float(values['v2'])) / float(values['v4'])}''')
        elif values['v2'] == 'x':
            window['resp_completa'].update(f'''
            {values['v1']} - {values['v2']}
            {values['v3']} - {values['v4']}
            
            {values['v3']}x = {values['v1']} * {values['v4']}
            {values['v3']}x = {float(values['v1']) * float(values['v4'])}
            x = {float(values['v1']) * float(values['v4'])} / {float(values['v3'])}

            x = {(float(values['v1']) * float(values['v4'])) / float(values['v3'])}''')
        elif values['v3'] == 'x':
            window['resp_completa'].update(f'''
            {values['v1']} - {values['v2']}
            {values['v3']} - {values['v4']}
            
            {values['v2']}x = {values['v1']} * {values['v4']}
            {values['v2']}x = {float(values['v1']) * float(values['v4'])}
            x = {float(values['v1']) * float(values['v4'])} / {float(values['v2'])}

            x = {(float(values['v1']) * float(values['v4'])) / float(values['v2'])}''')
        elif values['v4'] == 'x':
            window['resp_completa'].update(f'''
            {values['v1']} - {values['v2']}
            {values['v3']} - {values['v4']}
            
            {values['v1']}x = {values['v2']} * {values['v3']}
            {values['v1']}x = {float(values['v2']) * float(values['v3'])}
            x = {float(values['v2']) * float(values['v3'])} / {float(values['v1'])}

            x = {(float(values['v2']) * float(values['v3'])) / float(values['v1'])}''')

window.close()