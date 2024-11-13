"""
    Cruz Bravo Alejandro
    Menú que permite la creación de un automata y su recorrido del mismo mediante una cadena
    12/11/24

"""

import pandas as pd
import os


class automata:
    def __init__(self):
        self.Q = self.definir_estados()
        self.Sigma = self.definir_alfabeto()
        self.Delta = self.definir_transicion()
        self.Start_State, self.Accept_State  = self.set_start_accept()
        self.estadoActual = None
        self.guardarCSV();

    """
        Pedir al usuario el estado inicial y los estados de aceptación.
        Validar que pertenezcan a Q
    """
    def set_start_accept(self):

        while(True):
            start = input("Dame el estado inicial del automata: ")
            aceptacion = input("Dame el o los estados de aceptación: ").split()
            
            # Asegurar que los estados que se proporcionaron son válidos

            if(start in self.Q) and (set(aceptacion).issubset(set(self.Q))):
                return start,aceptacion
            
            else:
                print("Favor de proporcionar el estado inicial y los estados de aceptación que deben estar en Q: {}.".format(self.Q))
                
                
    """Pedir al usuario el conjunto de esta Q"""
    def definir_estados(self):

        Q_in = input("\nDame el conjunto de estados, separados por espacio en blanco: ").split()
        print("Estados: {}".format(Q_in))
        return Q_in
    
    
    """Pedir al usuario el alfabeto"""
    def definir_alfabeto(self):

        Sigma_in = input("\nDame el alfabeto: ").split()
        print("Estados: {}".format(Sigma_in))
        return Sigma_in

    
    """ Crear las funciones de transición (Q x Sigma) del automata"""
    def definir_transicion(self):

        transi_dict = {q: {a:"JACHI" for a in self.Sigma} for q in self.Q}

        for key, dict_value in transi_dict.items():
            print("\nEstoy en el estado {}. Escribir JACHI si no existe estado de transición".format(key))

            for alfabeto_in, transi_state in dict_value.items():
                transi_dict[key][alfabeto_in] = input(
                    "Estoy en {} y veo {}, ¿a qué estado voy: ".format(key,alfabeto_in))
            
            print("\nFUNCIÓN DE TRANSICIÓN Q x SIGMA -> Q")
            print("Estado actual \t Alfabeto de Entrada \t Siguiente Estado")
            for key, dict_value in transi_dict.items():
                for alfabeto_in, transi_state in dict_value.items():
                    print("{}\t{}\t{}".format(key,alfabeto_in,transi_state))
        return transi_dict
    
    """ Guardamos el automata en un CSV"""
    def guardarCSV(self):
        data = {
            'Estados': [self.Q],
            'Alfabeto': [self.Sigma],
            'Transiciones': [self.Delta],
            'Estado Inicial': [self.Start_State],
            'Estados de Aceptación': [self.Accept_State]
        }
        df = pd.DataFrame(data)
        
        df.to_csv('automata_data.csv', index=False)
        print("\n\nDatos guardados en 'automata_data.csv'")

""" Recorrer el automata con la cadena entrante y comprobar si llega al estado final"""
def recorrer_automata(data, w):
    estadoInicial = data[3][1]
    transiciones = eval(data[2][1])
    estadosAceptacion = data[4][1] 
    
    estadoActual = estadoInicial


    for simbolo in w:
        if estadoActual in transiciones and simbolo in transiciones[estadoActual]:
            estadoActual = transiciones[estadoActual][simbolo]  
        else:
            # Si no hay transición para ese símbolo, la cadena es rechazada
            print(f"Cadena rechazada en símbolo '{simbolo}', sin transición desde el estado '{estadoActual}'")
            print("\n_____________________________________________________")
            return False

    if estadoActual in estadosAceptacion:
        print("Cadena aceptada")
        print("_____________________________________________________")
        return True
    else:
        print("Cadena rechazada")
        print("_____________________________________________________")
        return False

    
    
if __name__ == "__main__":
    print("\n")
    print("\tSeleccione una opción a realizar:\n")
    
    """Despliega el menú"""
    while True:
        option = input("\t1- Definir el automata.\n \t2- Cargar cadena.\n \t3- Salir del programa. \n\n Escriba un número: ")
        match option:
            case "1":
                print("_____________________________________________________")
                print("\nDefinir automata")
                option = input("\t1- Crear un automata.\n \t2- Cargar un automata.\n \t3-Volver al menu \n\n Escriba un número: ")
                
                match option:
                    case "1":
                        print("\n_____________________________________________________")
                        obj = automata()
                        
                    case "2":
                        print("\n_____________________________________________________")
                        print("\tAutomata cargado\n")
                        if not os.path.exists('automata_data.csv'):
                            print("\tEl archivo 'automata_data.csv' no existe. Regresando al menú principal.")
                            continue
                        
                        data = pd.read_csv('automata_data.csv', header=None)
                        print("Estados:",data[0][1],"\nAlfabeto:",data[1][1],"\nTransiciones:",data[2][1],"\nEstado Inicial:",data[3][1],"\nEstado de aceptación:",data[4][1])
                        print("\n_____________________________________________________")
                        
                    case "3":

                        print("\nRegresando al menú principal")
                        print("\n_____________________________________________________")
                        continue
                    case _:
                        print("Opción no válida")
                
            case "2":
                print("\n_____________________________________________________")
                print("\nCargar cadena")
                if not os.path.exists('automata_data.csv'):
                    print("\tEl automata no ha sido definido. Regresando al menú principal.")
                    continue
                w = input("Ingrese la cadena: ")
                data = pd.read_csv('automata_data.csv', header=None)
                recorrer_automata(data,w)
                
            case "3":
                print("\nCerrar programa")
                break

            case _:
                print("\n_____________________________________________________")
                print("Opción no válida")
