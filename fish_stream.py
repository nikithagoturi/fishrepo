import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('Fish.csv')
species = df['Species']
height= df['Height']
plt.bar(species, height)
plt.title('Species and their Avg Height')
plt.xlabel('Species')
plt.ylabel('Height')
st.pyplot(plt)