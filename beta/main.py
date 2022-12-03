import os
import streamlit as st
import pandas as pd
from pymongo import MongoClient

mongo_uri = os.environ["MONGO_URI"]

client = MongoClient(mongo_uri)
stats = client.dashboards.container_status

results = stats.aggregate(
    [
        {
            "$group": {
                "_id": {"host": "$hostname", "container": "image"},
                "status": {"$last": "is_running"},
            }
        },
        {
            "$project": {
                "_id": 0,
                "host": "$_id.host",
                "container": "$_id.container",
                "status": "$status",
            }
        },
    ]
)

df = pd.DataFrame(results)
df.container = df.container.str[-20:]
df = df.pivot(index="host", columns="container", values="status")

st.set_page_config(layout="wide")
st.image(
    "https://www.aggbusiness.com/sites/ropl-ab/files/2022-07/CEMEX%20USA_CA%20CNG%20Trucks.%20Southern%20California_Pic%20-%20CEMEX%20USA.jpg",
    width=300,
)
st.markdown("# CEMEX - Image Recognition Container Status")
st.table(
    df.style.apply(
        lambda row: [
            "background-color: green" if cell in [True] else "background-color: red"
            for cell in row
        ],
        axis=1,
    )
)
