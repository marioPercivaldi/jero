from typing import Optional

import pandas as pd
from fastapi import FastAPI

import servicios as srv

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "hola mundo"}


@app.get("/mes/{mes}")
def cantidad_filmaciones_mes(mes: str):
    # importar el dataframe
    df = srv.open_movies()
    # convertir la columna de release date a fecha
    df_convertido = srv.df_format_date(df=df)
    # contabilizar la cantidad de peliculas estrenadas en el mes
    dict_respuesta_cliente: dict = {
        "ruta": "ejercicio 1",
        "resultado": srv.cant_pelic(df=df_convertido, mes=mes),
    }
    # retornar un mensaje con el resultado.
    return dict_respuesta_cliente


@app.get("/dia/{dia}")
def cantidad_filmaciones_dia(dia: int):
    # importar el dataframe
    df = srv.open_movies()
    # convertir la columna de release date a fecha
    df_convertido = srv.df_format_date(df=df)
    # contabilizar la cantidad de peliculas estrenadas en el mes
    dict_respuesta_cliente: dict = {
        "ruta": "ejercicio 2",
        "resultado": srv.cant_pelic(df=df_convertido, dia=dia),
    }
    # retornar un mensaje con el resultado.
    return dict_respuesta_cliente


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=5001)
