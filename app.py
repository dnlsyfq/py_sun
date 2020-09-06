import streamlit as st 
import pandas as pd 
import numpy as np 
import datetime as dt



# st.title('Hello World')

# with st.echo():
#     x = 10
    
# with st.echo():
#     y = 42
    
# with st.echo():
#     z = x + y 
#     st.write(z)

###########################

DATE_TIME = 'date/time'
DATA_URL =  'uber-raw-data-sep14.csv'

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL,nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase,axis=1,inplace=True)
    data[DATE_TIME] = pd.to_datetime(data[DATE_TIME])
    return data

data = load_data(1000)

# hour = 9

# data = data[data[DATE_TIME].dt.hour == hour]

hour = st.selectbox('Select Hour',range(0,24),1)

hour = st.slider('Select Hour',0,0,23,1)

data = data[data[DATE_TIME].dt.hour == hour]

if st.checkbox('view_data'):
    st.subheader('Raw Data at %sh' %hour)
    st.write(data)

st.subheader('Data by Minute at %sh' %hour)
st.bar_chart(np.histogram(data[DATE_TIME].dt.minute,bins=60,range=(0,60))[0])

st.map(data)

