import streamlit as st
import pandas as pd
import duckdb

st.write("""
#SQL SRS - Speed Repetition System SQL pratice
""")

option = st.selectbox(
    "Que voulez-vous réviser?",
    ("Joins", "GroupBy", "Windows Functions"),
    index=None,
    placeholder="Sélectionner un thème..."
)

st.write("Vous avez sélectionné:", option)

data = {
    "a" : [1,2,3],
    "b" : [4,5,6]
}

df = pd.DataFrame(data)

st.write("df:")
st.dataframe(df)

code = st.text_area(
    "Ecrivez votre code ici:",
    placeholder="Saisissez votre code..."
)
resultat = duckdb.query(code).df()
st.write(f"votre résultat: {code}")
st.dataframe(resultat)