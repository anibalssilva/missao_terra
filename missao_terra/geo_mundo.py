import geopandas as gpd
from babel import Locale

# 1) Lê do repositório público
url = "https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson"
world = gpd.read_file(url)

# 2) Renomeia coluna 'name' → 'NAME' (para manter compatibilidade com D3)
world = world.rename(columns={'name': 'NAME'})

# 3) Prepara o Locale para Português do Brasil
pt = Locale('pt', 'BR')

# 4) Função de tradução: pega o código alpha-2 e busca o nome em pt-BR
def traduzir_pt_br(row):
    code = row['ISO3166-1-Alpha-2']  # coluna exata do GeoJSON
    # se não encontrar no dicionário, mantém o nome original em inglês
    return pt.territories.get(code, row['NAME'])

# 5) Sobrescreve a coluna NAME com o nome em Português
world['NAME'] = world.apply(traduzir_pt_br, axis=1)

# 6) Salva localmente
world.to_file("world_ptbr.geojson", driver="GeoJSON")
print("world_ptbr.geojson gerado com sucesso!")
