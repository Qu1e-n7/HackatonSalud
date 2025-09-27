from geopy.geocoders import Nominatim
import pandas as pd
import time

dfSedes = pd.read_csv("data/Prestadores_SedesServiciosSalud.csv", dtype=str, low_memory=False)

# Geolocalizador
geolocator = Nominatim(user_agent="hackathon_app")

# Función para filtrar prestadores solo en Boyacá
def dataframePrestadoresSedes(dfSedes):
    dfSedes = dfSedes[dfSedes["DepartamentoPrestadorDesc"].str.upper() == "BOYACÁ"].copy()
    
    dfSedes.loc[:, "MunicipioSedeDesc"] = (
        dfSedes["MunicipioSedeDesc"].str.strip().str.upper()
    )
    
    dfSedes = dfSedes.groupby("MunicipioSedeDesc").head().reset_index(drop=True)

    return dfSedes
# Función para obtener coordenadas de las direcciones
def coordenadasmap(dfSedes):
    df_filtrado = dfSedes[
        dfSedes["ClasePrestadorDesc"].str.strip() != "Objeto Social Diferente a la Prestación de Servicios de Salud"
    ].copy()
    
    df_filtrado = (
        df_filtrado.groupby(["MunicipioSedeDesc", "ClasePrestadorDesc"], group_keys=False)
        .head(2)
        .reset_index(drop=True)
    )

    coords = []
    total = len(df_filtrado)

    for i, row in df_filtrado.iterrows():
        direccion = f"{row['DireccionSede']}, {row['MunicipioSedeDesc']}, Boyacá, Colombia"
        try:
            location = geolocator.geocode(direccion)
            if location:
                coords.append((location.latitude, location.longitude))
            else:
                coords.append((None, None))
        except Exception as e:
            print(f"❌ Error en fila {i}: {e}")
            coords.append((None, None))

        print(f"📍 Procesando {i+1}/{total}: {direccion}")

        time.sleep(1)  

    df_filtrado.loc[:, "Latitud"], df_filtrado.loc[:, "Longitud"] = zip(*coords)
    df_filtrado.to_csv("data/sedes_geocodificadas.csv", index=False, encoding="utf-8-sig")
    
    return df_filtrado

# Bloque principal
if __name__ == "__main__":
    df_filtrado = dataframePrestadoresSedes(dfSedes)
    df_final = coordenadasmap(df_filtrado)
    print("✅ Archivo 'data/sedes_geocodificadas.csv' generado con éxito")
