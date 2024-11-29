## Instalación

Para configurar el entorno de desarrollo, sigue estos pasos:

1. **Clona el repositorio:**

    ```bash
    git clone https://github.com/tuusuario/el-repositorio.git
    cd el-repositorio
    ```

2. **Crea un entorno virtual (no obligatorio, pero recomendado):**

    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `venv/Scripts/activate`
    ```

3. **Instala las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

## Ejecuciones de Herramientas de Extraccion de Data con Scraping Tools

## UI.Vision: Ejecutar el macro con la extension UI.Vision desde la terminal

1. Asegurate de tener instalado Google Chrome.
2. Descarga e instala la extensión de UI.Vision en Chrome.
3. Ingresar a google > Extension > Gestionar Extensiones > Ubicar UI.Vision y dar click en detalles > Habilitar la opcion: Permitir acceso a URL de archivo.
4. Asegurarse de utilizar una distro WSL de Ubuntu y confirmar la existencia de los archivos con: \\wsl$\Ubuntu-22.04\home\tu-usuario\web-scraping-tools\data\tools_json_files\ui.vision en el navegador.
5. La direccion varia dependiendo de donde tengas ubicado la distribucion WSL de Ubuntu
6. Iniciar sesion previamente en LinkedIn.
7. Para ejecutar el macro desde la terminal, utiliza el siguiente comando:

### Windows (CMD)
El macro solo tiene acciones despues de iniciar sesion, la persona que lo ejecute debe iniciar sesion previamente en LinkedIn.
Puede que ocurran errores en la ejecucion de UI.Vision, porque no ubica las acciones que realiza en el macro (Dado que la pagina de LinkedIn se Actualiza frecuentemente).

```shell
start chrome.exe --app="file://wsl$/Ubuntu-22.04/home/tu-usuario/web-scraping-tools/data/tools_json_files/ui.vision/ui.vision.html?direct=1&macro=linkedin"
```

## BeautifulSoup

Extraccion de data mediante un archivo.html:
```bash
./tools/beautifulsoup/beautiful_test.py
```

## MechanicalSoup

Extraccion de data
```bash
./tools/mechanicalsoup/mechanical_test.py
```

## WebHarvy

1. Asegurate de tener instalado WebHarvy.
2. Inicia la aplicación WebHarvy en tu sistema.
3. Haz clic en File > Load Mining Configuration (Archivo > Cargar configuración de minería (harvy.xml en la carpeta tools del proyecto)).
4. Haz clic en el botón Start Mining para comenzar la secuencia.
5. Una vez que la extracción haya terminado, exporta los datos en el formato que prefieras (CSV, Excel, JSON, etc.).
6. En la carpeta tools se encuentra un ejemplo del JSON que el proceso dejara.

## Scrapy

1. Asegurarte de estar usando el entorno virtual (ejemplo env).
2. Dirijirte a la siguiente ruta: cd tools/scrapy/linkedin_scraper/linkedin_scraper/
3. Ejecutar el siguiente comando para extraer datos de la pagina (Ubicado en CONTENIDO)

```bash
scrapy crawl wikipedia
```

## Diffbot

1. Logearse, usando un correo de empresa (requerido)
2. Al ser un servicio, solo debes ingresar a: https://app.diffbot.com/ .
3. Dirijirte a la parte de Extract y colocar la URL de la Pagina a extraer
4. En el boton, listar las diferentes opciones: Analyze Article Product Discussion List Event Job Image Video
5. En data/tools_json_files/diffbot/jsonfile.json, el archivo jsonfile.json es un ejemplo de los datos de una URL extraida

## Selenium

Al no poder integrar el codigo y ejecucion de selenium desde un archivo.py por errores de integracion de chromedriver,
use un archivo.ipynb (test-selenium.ipynb) de otro proyecto, en el cual no estan los errores con chromedrive, y asi mostrar las ejecuciones de los codigos y su respuesta.
El archivo se encuentra en /tools/selenium/test-selenium.ipynb.
Sí no se muestran las ejecuciones, tambien hay un archivo.html en el cual las lineas 7556 y 7701 muestran los datos extraidos de las paginas.