"""
5 Sections
1.The Import. 2. Layout Definition 3. Create Window 4. Event Loop 5. Close Window.
"""
# 1. The Import (Import PySimpleGUI as sg) It makes it easy to port
import PySimpleGUI as sg
sg.theme('TealMono')

# 2. Layout Definition. Put the Elements in their order in rows.
layout = [[sg.Push(),sg.Text('CALCULO DE INDICE DE MASA CORPORAL',font=("Times", 20)),sg.Push()],
          [sg.Text('Peso (en Kg):', size=(15,1), font=("Helvetica", 16)), sg.Input(key='Peso', font=("Helvetica", 16), enable_events=True)],
          [sg.Text('Altura (en Cm.):',size=(15,1), font=("Helvetica", 16)), sg.Input(key='Altura', font=("Helvetica", 16),enable_events=True)],
          [sg.Text('Tu IMC es de:',size=(15,1), font=("Helvetica", 16)), sg.Text(key="IMC_Out", font=("Helvetica", 16))],
          [sg.Text("AVISO:", size=(15,1), font=("Helvetica", 16)), sg.Text(key="recomendacion", font=("Helvetica", 16))],
          [sg.Button("OK", font=("Helvetica", 16)), sg.Button("Salir", font=("Helvetica", 16))]]

# 3.Create Window
window = sg.Window('IMC', layout)


# 4. Event Loop
while True:
    event, values = window.read()
    print(event, values) 
    if event in (None, "Salir"):
        break
    
    #Siguientes dos If son para garantizar que el usuario solamnte introduzca numeros
    if event == "Peso" and values["Peso"] and values["Peso"][-1] not in ("0123456789.-"):
        window["Peso"].update(values["Peso"][:-1])
        window["recomendacion"].update("Solamente puede introducir numeros", text_color='red')
    if event == "Altura" and values["Altura"] and values["Altura"][-1] not in ("0123456789.-"):
        window["Altura"].update(values["Altura"][:-1])
        window["recomendacion"].update("Solamente puede introducir numeros", text_color='red')
    
    if event == "OK":
        pesoTotal = int(values["Peso"]) #toma el string "Peso" y lo convierte a entero en una nueva variable
        alturaTotal = int(values["Altura"]) #toma el string "Altura" y lo convierte a entero en una nueva variable
        bmi = pesoTotal / (alturaTotal/100)**2 #formula para obtener BMI
        bmiRounded = round(bmi,2) # redondea BMI a dos digitos
        window["IMC_Out"].update(bmiRounded) #avienta el valor de BMi redondeado a la casilla "IMC_Out"
        
        #Recomendacion:
        if bmi < 18.5:
            window["recomendacion"].update("Su IMC indica un Peso Bajo", text_color='yellow')
        if bmi >= 18.5 and bmi < 25:
            window["recomendacion"].update("Su IMC indica Peso Normal", text_color='blue')
        if bmi >= 25 and bmi < 30:
            window["recomendacion"].update("Su IMC indica Sobrepeso", text_color='orange')
        if bmi > 30:
            window["recomendacion"].update("Su IMC indica Obesidad", text_color='red')


# 5. Close window
window.close()
exit()
