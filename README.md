# Web Scraper - Compra Gamer 

Este es un proyecto de Web Scraping desarrollado en Python que extrae información de productos (nombres y precios) del sitio web Compra Gamer. El objetivo principal fue aplicar conceptos de **Programación Orientada a Objetos (POO)** y manejo de excepciones en un entorno real.

## 🚀 Funcionalidades
- Extracción automatizada de títulos y precios de productos.
- Manejo de errores de conexión y tiempos de espera (timeouts).
- Almacenamiento de datos en formato **CSV** para su posterior análisis.
- Arquitectura modular y escalable.

## 🛠️ Tecnologías utilizadas
- **Python 3.x**
- **BeautifulSoup4**: Para el parseo de HTML.
- **Requests**: Para gestionar las peticiones HTTP.
- **CSV**: Para la persistencia de datos.

## 📂 Estructura del Proyecto
El código se divide en módulos según su responsabilidad:
- `WebScraper.py`: Clase principal que orquestra el flujo de ejecución.
- `Busqueda_contenido.py`: Se encarga de analizar el HTML y extraer los datos específicos.
- `Errores_HTML.py`: Gestiona las conexiones y el manejo de excepciones HTTP.
- `Crear_csv.py`: Clase dedicada a la creación y escritura del archivo de salida.

## 🔧 Instalación y Uso
1. Clona el repositorio:
   ```bash
   git clone [https://github.com/TuUsuario/nombre-del-repo.git](https://github.com/TuUsuario/nombre-del-repo.git)
