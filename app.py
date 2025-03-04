import streamlit as st
import pandas as pd
import duckdb

st.write("Première app")

data = {
    "a" : [1,2,3],
    "b" : [4,5,6]
}

df = pd.DataFrame(data)

st.write("df:")
st.dataframe(df)

code = st.text_area("Ecrivez votre code ici:")
resultat = duckdb.query(code).df()
st.write(f"votre résultat: {code}")
st.dataframe(resultat)