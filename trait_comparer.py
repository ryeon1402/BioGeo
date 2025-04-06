import streamlit as st

def show_trait_comparer(df):
    species_list = sorted(df["taxon_name"].dropna().unique())
    selected_species = st.multiselect("Select species for comparison", species_list)

    if selected_species:
        comparison_data = df[df["taxon_name"].isin(selected_species)].set_index("taxon_name")
        st.dataframe(comparison_data.T)
