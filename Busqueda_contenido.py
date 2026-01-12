""" <cgw-product-card _nghost-ng-c1896830227="" class="ng-star-inserted"><a _ngcontent-ng-c1896830227="" queryparamshandling="merge" class="cg__primary-card hover medium notSelected product-card responsive vertical" href="/producto/Memoria_Kingston_DDR5_64GB_2x32GB_6000MHz_Fury_Beast_Black_RGB_CL30_AMD_EXPO_18742?cate=15"><!----><div _ngcontent-ng-c1896830227="" class="medium product-card__image"><cgw-item-image _ngcontent-ng-c1896830227="" style="display: flex; align-items: center; justify-content: center;"><div class="tw:relative tw:size-full"><img loading="lazy" class="tw:border-2 tw:border-solid tw:border-white tw:block tw:rounded-xl tw:object-contain tw:size-full ng-lazyloaded" src="https://imagenes.compragamer.com/productos/compragamer_Imganen_general_49037_Memoria_Kingston_DDR5_64GB__2x32GB__6000MHz_Fury_Beast_Black_RGB_CL30_AMD_EXPO_22b16e0f-med.jpg" alt="Memoria Kingston DDR5 64GB (2x32GB) 6000MHz Fury Beast Black RGB CL30 AMD EXPO"><!----></div></cgw-item-image><cgw-liquidation-logo _ngcontent-ng-c1896830227="" class="product-card__promoLogo ng-star-inserted" _nghost-ng-c4174197458=""><!----></cgw-liquidation-logo><!----><!----></div><div _ngcontent-ng-c1896830227=""><!----><!----><h3 _ngcontent-ng-c1896830227="" class="cg__fw-400 mb-2 product-card__title ng-star-inserted"> Memoria Kingston DDR5 64GB (2x32GB) 6000MHz Fury Beast Black RGB CL30 AMD EXPO </h3><!----></div><div _ngcontent-ng-c1896830227="" class="product-card__cart tw:grid-cols-[auto] ng-star-inserted"><div _ngcontent-ng-c1896830227="" class="product-card__cart__price tw:relative"><span _ngcontent-ng-c1896830227="" class="product-card__cart__price--current txt_button cg__fw-600"><span _ngcontent-ng-c1896830227="" class="txt_button">$</span><span _ngcontent-ng-c1896830227="" class="txt_price">1.236.800</span></span><!----></div><div _ngcontent-ng-c1896830227="" class="product-card__cart__button ng-star-inserted"><cgw-action-button _ngcontent-ng-c1896830227="" _nghost-ng-c2361252851="" class="ng-star-inserted"><a _ngcontent-ng-c2361252851="" cgwthrottletime="" class="align-items-center cg__button cg__button--primary product-card__button px-3 tw:justify-center tw:mt-[17.5px] tw:w-full"><mat-icon _ngcontent-ng-c2361252851="" role="img" fontset="material-symbols-outlined" class="mat-icon notranslate material-symbols-outlined tw:block tw:md:hidden tw:lg:block tw:flex tw:items-center mat-icon-no-color ng-star-inserted" aria-hidden="true" data-mat-icon-type="font" data-mat-icon-namespace="material-symbols-outlined" style="font-size: 16px; width: 16px; height: 16px;"> shopping_cart </mat-icon><!----><span _ngcontent-ng-c2361252851="" class="ng-star-inserted" style="font-size: 14px; font-weight: 500;">Sumar al carrito</span><!----></a></cgw-action-button><!----><!----></div><!----></div><!----><!----><!----><!----></a><!----></cgw-product-card> """
import re
import requests
from bs4 import BeautifulSoup #El que va a recorrer el html de la pagina
class busqueda_contenido:

    # def fetcher(self):
    #     url = 'https://compragamer.com/productos?cate=15'
    #     response = requests.get(url)
    #     html_content = response.content
    #     soup = BeautifulSoup(html_content, 'html.parser')
    #     return soup
    #pasador = errores_HTML.ingreso_errores #esto lo saque para hacerlo mas comodo en el main. Cuando llame esta clase y el metodo, voy a tener que poner el parametro que me quede mas comodo. ASi es mas reutilizable y el codigo es mas comodo para  correguir
    def parser(self, pasador):
        contenido = []
        if pasador != None:
            elementos_con_clase_especifica = pasador.find_all('cgw-product-card')
            for producto in elementos_con_clase_especifica:
                titulo = "Sin título" # Valor por defecto
                precio = "Sin precio"
                clase_titulo = producto.find('h3', class_='product-card__title')
                clase_precio = producto.find('span', class_='txt_price')
                if clase_titulo != None:
                    titulo = clase_titulo.get_text(strip=True)
                if clase_precio != None:
                    precio = clase_precio.get_text(strip=True)
                contenido.append([titulo, precio])
        return contenido