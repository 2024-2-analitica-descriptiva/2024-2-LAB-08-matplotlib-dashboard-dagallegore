# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """

    if not os.path.exists("docs"):
        os.makedirs("docs")
        
    df = pd.read_csv("files/input/shipping-data.csv")
    
    df = df.copy()
    plt.figure()
    counts = df.Warehouse_block.value_counts()
    counts.plot.bar(
        title="Shipping per Warehouse",
        xlabel="Warehouse block",
        ylabel="Record Count",
        color="tab:blue",
        fontsize=8
    )
    
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.savefig("docs/shipping_per_warehouse.png")

    plt.figure()
    counts2 = df.Mode_of_Shipment.value_counts()
    counts2.plot.pie(
        title="Mode of Shipment",
        wedgeprops=dict(width=0.35),
        ylabel="",
        colors=["tab:blue","tab:orange","tab:green"]
    )
    plt.savefig("docs/mode_of_shipment.png")

    plt.figure()
    df1 = (
        df[["Mode_of_Shipment","Customer_rating"]]
        .groupby("Mode_of_Shipment")
        .describe()
    )
    df1.columns = df1.columns.droplevel()
    df1 = df1[["mean","min","max"]]
    plt.barh(
        y=df1.index.values,
        width=df1["max"].values - 1,
        left=df1["min"].values,
        height=0.9,
        color="lightgray",
        alpha=0.8
    )
    colors = [
        "tab:green" if value >= 3.0 else "tab:orange" for value in df1["mean"].values
    ]
    plt.barh(
        y=df1.index.values,
        width=df1["mean"].values - 1,
        left=df1["min"].values,
        color=colors,
        height=0.5,
        alpha=1.0
    )
    plt.title("Average Customer Rating")
    plt.gca().spines["left"].set_visible("gray")
    plt.gca().spines["bottom"].set_visible("gray")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.savefig("docs/average_customer_rating.png")

    plt.figure()
    df.Weight_in_gms.plot.hist(
        title="Shipped Weight Distribution",
        color="tab:orange",
        edgecolor="white"
    )
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.savefig("docs/weight_distribution.png")

    return df

pregunta_01()