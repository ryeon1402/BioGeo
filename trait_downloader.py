import streamlit as st

def show_trait_downloader(df):
    species_list = sorted(df["taxon_name"].dropna().unique())
    selected_species = st.selectbox("Select a species to download", species_list)

    filtered_data = df[df["taxon_name"] == selected_species]
    csv = filtered_data.to_csv(index=False)

    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name=f"{selected_species}_traits.csv",
        mime="text/csv"
    )
