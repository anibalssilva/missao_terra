import geopandas as gpd

# 1) URL do GeoJSON público
url = "https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson"

# 2) Carrega tudo
world = gpd.read_file(url)

# 3) Descobre qual coluna guarda o nome
for col in ("ADMIN", "admin", "NAME", "name", "Country", "COUNTRY"):
    if col in world.columns:
        name_col = col
        break
else:
    raise RuntimeError(f"Não achei coluna de nome de país em {list(world.columns)}")

# 4) Mapeamento Inglês→Português dos 12 países
nome_map = {
    "Guatemala": "Guatemala",
    "El Salvador": "El Salvador",
    "Honduras": "Honduras",
    "Costa Rica": "Costa Rica",
    "Belize": "Belize",
    "Panama": "Panamá",
    "Mexico": "México",
    "Canada": "Canadá",
    "United States of America": "Estados Unidos da América",
    "Greenland": "Groenlândia",
    "Iceland": "Islândia",
    "Nicaragua": "Nicarágua"
}

# 5) Filtra e renomeia para o field que seu D3 espera: properties.NAME
sel = world[world[name_col].isin(nome_map)].copy()
sel["NAME"] = sel[name_col].map(nome_map)

# 6) Exporta só geometria + NAME
sel[["NAME", "geometry"]].to_file("north_america.geojson", driver="GeoJSON")
print("north_america.geojson gerado com sucesso!")
