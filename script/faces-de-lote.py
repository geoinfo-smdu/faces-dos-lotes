import geopandas as gpd
from shapely.geometry import Point, LineString, MultiPoint, MultiLineString
from shapely.ops import nearest_points
import pandas as pd
import glob

gdf_distritos = gpd.read_file('download/SIRGAS_SHP_distrito/SIRGAS_SHP_distrito/SIRGAS_SHP_distrito_polygon.shp')
print(gdf_distritos[["ds_codigo", "ds_nome"]])

## Para cada distrito
folder = 'download/lotes'
for path in glob.iglob(f"{folder}/*"):
    print(path.replace(f"{folder}\SIRGAS_SHP_LOTES_", ''))


    ## Recorta NBL apenas do Distrito considerando um buffer de 20m

    ## Dissolve a NBL por CODLOG

    ## Abre o arquivo de lotes do distrito

    ## Dissolve o arquivo de lotes por Setor, Quadra, Tipo e talvez Subquadra

    ## Calcula-se o centroide de cada segmento de linha de cada quadra

    ## Relaciona cada centroide de segmento de linha ao lote

    ## Conecta-se o centroide de cada segmento de linha ao segmento de logradouro mais próximo

    ## Relaciona-se essa conexão criada ao CODLOG e Lote

    ## Dissolve-se os segmentos de linha das faces dos lotes em testadas por CODLOG agrupadas por Lote fiscal

    ## Exporta os resultados para um arquivo contendo as testadas dos lotes do distrito selecionado

