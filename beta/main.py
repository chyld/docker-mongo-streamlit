import streamlit as st
import pandas as pd
from pymongo import MongoClient

client = MongoClient("mongodb+srv://smartlogisticsMDB:Memento1@cluster0.nusmy.mongodb.net/admin?authSource=admin&replicaSet=atlas-s0y3vi-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
stats = client.dashboards.container_stats

results = stats.aggregate([
    {
        '$group': {
            '_id': {
                'host': '$hostname', 
                'container': '$Config.Image'
            }, 
            'status': {
                '$last': '$State.Running'
            }
        }
    }, {
        '$project': {
            '_id': 0, 
            'host': '$_id.host', 
            'container': '$_id.container', 
            'status': '$status'
        }
    }
])

df= pd.DataFrame(results)
df.container = df.container.str[-20:]
df = df.pivot(index='host', columns='container', values='status')

st.set_page_config(layout="wide")
st.image("https://www.aggbusiness.com/sites/ropl-ab/files/2022-07/CEMEX%20USA_CA%20CNG%20Trucks.%20Southern%20California_Pic%20-%20CEMEX%20USA.jpg", width=300)
st.markdown('# CEMEX - Image Recognition Container Status')
st.table(df.style.apply(lambda row: ["background-color: green" if cell in [True] else "background-color: red" for cell in row], axis=1))

