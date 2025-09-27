import pandas as pd

def dataframePrestadoresSedes():
    dfSedes = pd.read_csv('data/Prestadores_SedesServiciosSalud.csv')
    dfSedes = dfSedes[dfSedes["DepartamentoPrestadorDesc"].str.upper() == 'BOYACÁ']
    # dfSedes.columns = (dfSedes.columns.str.strip())
    # dfSedes.columns = (dfSedes.columns.str.lower())
    # convertir a lista de diccionarios para Jinja2
    data = dfSedes.head(50).to_dict(orient="records")
    return data