'''  '''
import csv

class Crear_csv:
    def guardar_csv(self, datos):
        with open("Productos de CG.csv", 'w', newline='', encoding='utf-8') as archivo_csv:
            escritor = csv.writer(archivo_csv)
            escritor.writerows(datos)
        return None #provisional
