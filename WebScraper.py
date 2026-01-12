import Crear_csv, Errores_HTML, Busqueda_contenido

class WebScreaper:
    #url = print("Ingrese la url: ")
    #url = 'https://compragamer.com/productos?cate=15'
    url = 'https://compragamer.com/productos?cate=15'
    def __init__(self):
        self.pasador = Errores_HTML.errores_HTML()
        self.datos = Busqueda_contenido.busqueda_contenido()
        self.archivocsv = Crear_csv.Crear_csv()
    
    def inicio(self, url):
        
        sopi = self.pasador.ingreso_errores(url)
        datitos = self.datos.parser(sopi)

        self.archivocsv.guardar_csv(datitos)
if __name__ == "__main__":
    scraper = WebScreaper()
    # Usamos la URL que definiste en la clase o pasamos una nueva
    scraper.inicio(scraper.url)
    print("Proceso finalizado con éxito.")
