import PySimpleGUI as sg

def porcentagem_normal():
    print("Calcular '?¹%' de '?²'\n?¹ = caixa sem texto para valor 1\n?2 = caixa sem texto para valor 2")
    value1 = 0.0
    value1 = input("valor 1")
    value2 = 0.0
    value2 =  input("valor 2")
    result = (value1 / 100) * value2
    return result

def porcentagem_qntPorcDe():
    print("'?¹'% é quantos porcento de '?²'?\n?¹ = caixa sem texto para valor 1\n?2 = caixa sem texto para valor 2")    
    value1 = 0.0
    value1 = input("valor 1")
    value2 = 0.0
    value2 =  input("valor 2")
    result = (value1 / value2) * 100
    #quando retornar o resultado adicionar um ""+ result + "%"
    return result

def porcentagem_ehPorcDe():
    print("'?¹' é '?²%' de?\n?¹ = caixa sem texto para valor 1\n?2 = caixa sem texto para valor 2")    
    value1 = 0.0
    value1 = input("valor 1")
    value2 = 0.0
    value2 =  input("valor 2")
    result = (value1 / (value2 / 100))
    return result

def porcentagem_maisPorc():
    print("'?¹' mais '?²%' é:\n?¹ = caixa sem texto para valor 1\n?2 = caixa sem texto para valor 2")    
    value1 = 0.0
    value1 = input("valor 1")
    value2 = 0.0
    value2 =  input("valor 2")
    result = value1 * (1 + (value2 / 100))
    return result

def porcentagem_menosPorc():
    print("'?¹' menos '?²%' é:\n?¹ = caixa sem texto para valor 1\n?2 = caixa sem texto para valor 2")    
    value1 = 0.0
    value1 = input("valor 1")
    value2 = 0.0
    value2 =  input("valor 2")
    result = value1 * (1 - (value2 / 100))
    return result

section1 = [[sg.Input('Input sec 1', key='-IN1-')],
            [sg.Input(key='-IN11-')],
            [sg.Button('Button section 1',  button_color='yellow on green'),
             sg.Button('Button2 section 1', button_color='yellow on green'),
             sg.Button('Button3 section 1', button_color='yellow on green')]]

section2 = [[sg.I('Input sec 2', k='-IN2-')],
            [sg.I(k='-IN21-')],
            [sg.B('Button section 2',  button_color=('yellow', 'purple')),
             sg.B('Button2 section 2', button_color=('yellow', 'purple')),
             sg.B('Button3 section 2', button_color=('yellow', 'purple'))]]


layout =   [[sg.Text('Window with 2 collapsible sections')],
            [sg.Checkbox('Blank checkbox'), sg.Checkbox('Hide Section 2', enable_events=True, key='-OPEN SEC2-CHECKBOX')],
            #### Section 1 part ####
            [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC1-', text_color='yellow'), sg.T('Section 1', enable_events=True, text_color='yellow', k='-OPEN SEC1-TEXT')],
            [collapse(section1, '-SEC1-')],
            #### Section 2 part ####
            [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC2-', text_color='purple'),
             sg.T('Section 2', enable_events=True, text_color='purple', k='-OPEN SEC2-TEXT')],
            [collapse(section2, '-SEC2-')],
            #### Buttons at bottom ####
            [sg.Button('Button1'),sg.Button('Button2'), sg.Button('Exit')]]

window = sg.Window('Visible / Invisible Element Demo', layout)

opened1, opened2 = True, True

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event.startswith('-OPEN SEC1-'):
        opened1 = not opened1
        window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened1 else SYMBOL_UP)
        window['-SEC1-'].update(visible=opened1)

    if event.startswith('-OPEN SEC2-'):
        opened2 = not opened2
        window['-OPEN SEC2-'].update(SYMBOL_DOWN if opened2 else SYMBOL_UP)
        window['-OPEN SEC2-CHECKBOX'].update(not opened2)
        window['-SEC2-'].update(visible=opened2)

window.close()

porcentagem = 0
repeticao = 1
while repeticao == 1:
    print("1 - Calcular '?¹%' de '?²'\n2 - '?¹'% é quantos porcento de '?²'?\n3 - '?¹' é '?²%' de?\n4 - '?¹' mais '?²%' é:\n5 - '?¹' menos '?²%' é:")
    porcentagem = input("Escolha a porcentagem que quer calcular: (de 1 a 5)\nEscolha: ")
    if porcentagem == 1:
        resultado = porcentagem_normal()
        print(resultado)
    elif porcentagem == 2:
        resultado = porcentagem_qntPorcDe()
        print(resultado+"%")
    elif porcentagem == 3:
        resultado = porcentagem_ehPorcDe()
        print(resultado)
    elif porcentagem == 4:
        resultado = porcentagem_maisPorc()
        print(resultado)
    elif porcentagem == 5:
        resultado = porcentagem_menosPorc()
        print(resultado)
        orcentagem = 0
    repeticao = 0