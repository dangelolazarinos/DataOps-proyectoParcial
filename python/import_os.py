import os

###carpeta dataset###

location= "C:/Users/dlaza/Escritorio/certus/proyecto_parcial_dataops/dataset"

### validaciónde carpeta###
if not os.path.exists(location): ##si no esiste la carpeta
    ## creo carpeta
    os.makedirs(location)##mkdirs o makedirs
else: ##si existe la carpeta
    ##borramos contenido
    for root , dirs, files in os.walk(location ,topdown=False):
        for name in files:
            os.remove(os.path.join(root,name))##eliminar archivos
        for name in dirs:
            os.rmdir(os.path.join(root,name))

### descargar dataset###

from kaggle.api.kaggle_api_extended import KaggleApi

### credenciales###
api = KaggleApi()
api.authenticate()

#print(api.dataset_list(search=''))

api.dataset_download_files('youssefismail20/olympic-games-1994-2024', path=location, force= True, quiet=False, unzip=True)