"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", 
                    sep=";")
    df = df.drop('Unnamed: 0', axis=1)

    df['sexo'] = df['sexo'].str.lower()


    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower()

    df['idea_negocio'] = df['idea_negocio'].str.lower()
    df['idea_negocio'] = df['idea_negocio'].str.replace("-"," ")
    df['idea_negocio'] = df['idea_negocio'].str.replace("_"," ")


    df['barrio'] = df['barrio'].str.lower()
    df['barrio'] = df['barrio'].str.replace("-"," ")
    df['barrio'] = df['barrio'].str.replace("_"," ")


    df['estrato'] = df['estrato'].astype(int)

    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(int)

    df['fecha_de_beneficio']= pd.to_datetime(df['fecha_de_beneficio'],
                                            dayfirst= True,
                                            format='mixed')

    df['monto_del_credito'] = df['monto_del_credito'].str.strip("$")
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(" ","")
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(".00","")
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(",","")

    df['línea_credito'] = df['línea_credito'].str.lower()
    df['línea_credito'] = df['línea_credito'].str.replace("-"," ")
    df['línea_credito'] = df['línea_credito'].str.replace("_"," ")


    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    return df


