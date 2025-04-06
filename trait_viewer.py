import streamlit as st

def show_trait_viewer(df):
    species_list = sorted(df["taxon_name"].dropna().unique())
    selected_species = st.selectbox("Select a species", species_list)

    filtered_data = df[df["taxon_name"] == selected_species]

    st.subheader(f"Traits for {selected_species}")
    st.dataframe(filtered_data.T)
