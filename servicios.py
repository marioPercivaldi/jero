import ast
from datetime import datetime

import pandas as pd


def openCsv(ruta):
    df_movies = pd.read_csv("csvs/movies_dataset.csv")
    df_credits = pd.read_csv("csvs/credits.csv")
    print(df_credits)
    print(df_movies)
    return (df_credits, df_movies)


def open_movies() -> pd.DataFrame:
    df = pd.read_csv("csvs/movies_dataset.csv")
    return df


def get_genre_info(row):
    genres = row["genres"]
    info = []
    for index, genre in enumerate(genres):
        info.append(
            {
                "index": index,
            }
        )


def get_mes_esp(mes: str) -> int:
    "funcion que devuelve el numero de mes al recibir el nombre del mes"
    dict_mes: dict = {
        "enero": 1,
        "febrero": 2,
        "marzo": 3,
        "abril": 4,
        "mayo": 5,
        "junio": 6,
        "julio": 7,
        "agosto": 8,
        "septiembre": 9,
        "octubre": 10,
        "noviembre": 11,
        "diciembre": 12,
    }
    if mes is None:
        return "Debe ingresar un mes en texto obligatoriamente"
    else:
        return dict_mes.get(mes.lower(), None)


def cant_pelic(df: pd.DataFrame, mes: str = None, dia: str = None) -> str:
    if mes and dia:
        return "error, la funcion solo admite un mes o un dia"
    if mes:
        mes_numero = get_mes_esp(mes=mes)
        if mes_numero is None:
            return "Error, el mes no existe"
        entregas_mes = df[df["release_date"].dt.month == mes_numero]
        cantidad_pelic = entregas_mes.shape[0]
        return f"{cantidad_pelic} peliculas fueron estrenadas en el mes de {mes}"
    elif dia:
        if dia > 31:
            return "error no hay meses con mas de 31 dias"
        entregas_mes = df[df["release_date"].dt.day == dia]
        cantidad_pelic = entregas_mes.shape[0]
        return f"{cantidad_pelic} peliculas fueron estrenadas con el dia {dia}"


def df_format_date(df: pd.DataFrame):
    df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
    return df
