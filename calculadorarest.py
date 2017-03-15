#!/usr/bin/python3

import webapp


class calcrest(webapp.webApp):

    def parse(self,request):
        metodo = request.split(' ',2)[0]
        try:
            recurso = request.split(' ',2)[1]
        except:
            recurso = '/'
        try:
            solicitud = request.split('\r\n\r\n')[1]
        except:
            solicitud = ""

        return(metodo, recurso, solicitud)


    def process(self,peticion):
        metodo, recurso, solicitud = peticion
        if metodo == "GET":
            if recurso == '/':
                httpCode = "200 OK"
                htmlBody = "<html><h1>Puedes introducir: </h1><body>" \
                    + "<p>Una suma: suma operando1+operando2</p>" \
                    + "<p>Una resta: resta operando1-operando2</p>" \
                    + "<p>Una division: division operando1/operando2</p>" \
                    + "<p>Una multiplicacion: multiplicacion operando1*operando2</p>"  \
                    + '<form method="POST" action="">' \
                    + 'Operacion: <input type="text" name="op"><br>' \
                    + '<input type="submit" value="Enviar"><br>' \
                    + '</form>' \
                    + "</body></html>"
            else:
                httpCode = "200 OK"
                htmlBody = "<html><body>" \
                + 'ERROR: URL NO VALIDA' \
                + "</body></html>"

        elif metodo == "PUT" or metodo == "POST":
            try:
                if solicitud != "":
                    operacion = solicitud.split("=")[1]     #con esto me queda operador+num1operadornum2
                    operador = operacion.split("+")[0]     #con esto me quedo con operacion solo
                    numeros = operacion.split("+")[1]       #con esto me queda num1operadornum2
                    if operador == 'suma':
                        num1 = numeros.split("%2B")[0]     #hago con %2B porque asi me toma el operador +
                        num2 = numeros.split("%2B")[1]
                        resultado = int(num1) + int(num2)   #el resultado es la suma de ambos pasado a entero
                        httpCode = "200 OK"
                        htmlBody = "<html><body><h1> " + num1 + " + " + num2 + " = " \
                                    + str(resultado) + " </h1></body></html>"
                    elif operador == 'resta':
                        num1 = numeros.split("-")[0]
                        num2 = numeros.split("-")[1]
                        resultado = int(num1) - int(num2)   #el resultado es la suma de ambos pasado a entero
                        httpCode = "200 OK"
                        htmlBody = "<html><body><h1> " + num1 + " - " + num2 + " = " \
                                    + str(resultado) + " </h1></body></html>"
                    elif operador == 'multiplicacion':
                        num1 = numeros.split("*")[0]
                        num2 = numeros.split("*")[1]
                        resultado = int(num1) * int(num2)   #el resultado es la suma de ambos pasado a entero
                        httpCode = "200 OK"
                        htmlBody = "<html><body><h1> " + num1 + " * " + num2 + " = " \
                                    + str(resultado) + " </h1></body></html>"
                    elif operador == 'division':
                        num1 = numeros.split("%2F")[0]     #hago con %2F porque asi me toma el operador /
                        num2 = numeros.split("%2F")[1]
                        resultado = int(num1) / int(num2)   #el resultado es la suma de ambos pasado a entero
                        httpCode = "200 OK"
                        htmlBody = "<html><body><h1> " + num1 + " / " + num2 + " = " \
                                    + str(resultado) + " </h1></body></html>"
                    else:
                        httpCode = "200 OK"
                        htmlBody = "<html><body>" \
                        + 'ERROR:  OPERACION NO VALIDA cara pedo' \
                        + "</body></html>"

                else:
                    httpCode = "200 OK"
                    htmlBody = "<html><body>" \
                    + 'ERROR:  OPERACION NO VALIDA mamasita parrales' \
                    + "</body></html>"

            except IndexError:
                httpCode = "200 OK"
                htmlBody = "<html><body>" \
                + 'Asegurate de que rellenas el formulario tal y como se pide' \
                + "</body></html>"

        else:
            httpCode = "450 Metodo no valido"
            htmlBody = " "

        return (httpCode, htmlBody)


if __name__ == "__main__":
    myWebApp = calcrest("localhost", 1234)
