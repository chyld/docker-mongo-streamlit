import streamlit as st
import pandas as pd
from pymongo import MongoClient

client = MongoClient('172.17.0.1', 27017)
events = client.eventdb.events

st.markdown('# Global Container Status')

results = events.aggregate([
    {
        '$match': {
            'Type': 'container'
        }
    }, {
        '$group': {
            '_id': {
                'host': '$hostname', 
                'container': '$Actor.Attributes.name'
            }, 
            'status': {
                '$last': '$status'
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
df = df.pivot(index='host', columns='container', values='status')
st.dataframe(df.style.apply(lambda row: ["background-color: green" if cell in ['start'] else "background-color: red" for cell in row], axis=1))

