import streamlit as st
import pandas as pd
from pymongo import MongoClient

client = MongoClient('172.17.0.1', 27017)
events = client.eventdb.events

statuses = set([e.split(':')[0] for e in events.distinct('status')])

st.markdown('# Global Event Viewer')

option = st.selectbox(
    'Select an event?', statuses)

st.write('You selected:', option)

results = events.aggregate([
    {
        '$match': {
            'status': option
        }
    }, {
        '$group': {
            '_id': '$Actor.Attributes.name', 
            'count': {'$sum': 1}
        }
    }
])

df  = pd.DataFrame(results)
df = df.set_index('_id')
st.write(pd.DataFrame(df))
