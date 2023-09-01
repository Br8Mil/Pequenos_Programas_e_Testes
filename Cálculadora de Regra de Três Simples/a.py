#Copiado alguns trechos de código da página https://www.tutorialspoint.com/pysimplegui/pysimplegui_input_element.htm
#e https://stackoverflow.com/questions/70892428/pysimplegui-how-do-i-convert-a-value-from-string-to-float-using

import PySimpleGUI as sg

sg.theme('DarkAmber')

janela = [
[sg.Text('Valor 1'), sg.Input('', enable_events=True, expand_x=True, key='v1',size=(15,0)), sg.Text('Valor 2'), sg.Input('', enable_events=True, expand_x=True, key='v2',size=(15,0))],
[sg.Text('Valor 3'), sg.Input('', enable_events=True, expand_x=True, key='v3',size=(15,0)), sg.Text('Valor 4                X')],
[sg.Button('Calcular')],
]


window = sg.Window('Regra de 3 Simples', layout=janela)

while True:
    event, values = window.read()
    print(event, values)
    n1, n2, n3 , = 0, 0, 0

    if event == sg.WIN_CLOSED:
        break

    if values['v1'][-1] not in ('0123456789'):
        sg.popup("Por favor, dígite apenas números.")
        window['v1'].update(values['v1'][:-1])
    elif values['v1'][-1]:
        n1 = float(values['v1'])
    
    if values['v2'][-1] not in ('0123456789'):
        sg.popup("Por favor, dígite apenas números.")
        window['v2'].update(values['v2'][:-1])
    elif values['v2'][-1]:
        n2 = float(values['v2'])

    if values['v3'][-1] not in ('0123456789'):
        sg.popup("Por favor, dígite apenas números.")
        window['v3'].update(values['v3'][:-1])
    elif values['v3'][-1]:
        n3 = float(values['v3'])

    
    if event == 'Calcular':
        valor1 = values[n1]
        valor2 = values[n2]
        valor3 = values[n3]
        resul = valor2 * valor3
        resul/= valor1
        print(f'O valor de X e {resul}')
window.close()