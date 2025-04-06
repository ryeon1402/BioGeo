import streamlit as st
import pandas as pd

# 🔧 Helper: Get all trait columns except 'taxon_name'
def get_trait_filter_columns(df):
    trait_columns = list(df.columns)
    if "taxon_name" in trait_columns:
        trait_columns.remove("taxon_name")
    return trait_columns

# 🔍 View Traits Page
def trait_viewer(df):
    st.subheader("🔍 View Traits")

    species_list = sorted(df["taxon_name"].dropna().unique())
    selected_species = st.selectbox("Select a species (optional)", [""] + species_list)

    traits = get_trait_filter_columns(df)
    selected_traits = st.multiselect("Select traits to view (optional)", traits)

    # Filter by species
    if selected_species:
        filtered_df = df[df["taxon_name"] == selected_species]
    else:
        filtered_df = df.copy()

    # Filter by traits
    if selected_traits:
        result = filtered_df[["taxon_name"] + selected_traits]
    else:
        result = filtered_df

    st.subheader("Trait Table")
    st.dataframe(result)

# 📤 Download Traits Page
def trait_downloader(df):
    st.subheader("📤 Download Traits")

    species_list = sorted(df["taxon_name"].dropna().unique())
    selected_species = st.selectbox("Select a species", [""] + species_list)

    traits = get_trait_filter_columns(df)
    selected_traits = st.multiselect("Select traits to download", traits)

    if selected_species:
        filtered_df = df[df["taxon_name"] == selected_species]
    else:
        filtered_df = df.copy()

    if selected_traits:
        result = filtered_df[["taxon_name"] + selected_traits]
    else:
        result = filtered_df

    st.subheader("Preview")
    st.dataframe(result)

    if not result.empty:
        csv = result.to_csv(index=False)
        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name="selected_traits.csv",
            mime="text/csv"
        )

# 🔬 Compare Species Page
def trait_comparer(df):
    st.subheader("🔬 Compare Species")

    species_list = sorted(df["taxon_name"].dropna().unique())
    selected_species = st.multiselect("Select species to compare", species_list)

    traits = get_trait_filter_columns(df)
    selected_traits = st.multiselect("Select traits to compare (optional)", traits)

    # ✅ If no trait selected, show all traits
    if not selected_traits:
        selected_traits = traits

    if selected_species:
        result = df[df["taxon_name"].isin(selected_species)][["taxon_name"] + selected_traits].set_index("taxon_name")

        st.subheader("Comparison Table")
        st.dataframe(result.T)

        # Download
        csv = result.reset_index().T.to_csv(index=False)
        st.download_button(
            label="📥 Download Comparison as CSV",
            data=csv,
            file_name="species_comparison.csv",
            mime="text/csv"
        )
    else:
        st.info("Please select at least one species to compare.")
