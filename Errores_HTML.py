
#provisional
from bs4 import BeautifulSoup
import requests
from abc import ABC, abstractmethod #esto hace un metodo abstracto en python
class errores_HTML():
    #url = 'https://compragamer.com/productos?cate=15'
    def ingreso_errores(self, url):
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            html_content = response.content
            soup = BeautifulSoup(html_content, 'html.parser')
            
        except requests.exceptions.Timeout:
            print(f"Error de Timeout al conectar a {url}. Reintentando...")
            soup = None
            # Aquí podrías implementar lógica de reintento (ej. con time.sleep)
        except requests.exceptions.ConnectionError:
            print(f"Error de Conexión: No se pudo conectar a {url}. Verifique su conexión.")
            soup = None
        return soup


