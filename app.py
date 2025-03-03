import streamlit as st
import pandas as pd
import duckdb

st.write("Première app")

df = pd.DataFrame({
    "a" : [1,2,3],
    "b" : [4,5,6]
})

st.write("df:")
st.dataframe(df)

code = st.text_area("Ecrivez votre code ici:")

resultat = duckdb.sql(code).df()

st.write(f"votre résultat: {resultat}")
st.dataframe(resultat)