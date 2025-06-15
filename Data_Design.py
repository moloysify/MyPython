import streamlit as st
import pandas as pd

st.title("Data Model Designer")

if 'tables' not in st.session_state:
    st.session_state.tables = {}

table_name = st.text_input("Enter table name:")

if table_name:
    st.subheader(f"Design table: {table_name}")

    num_fields = st.number_input("Number of fields", min_value=1, step=1)

    fields = []
    for i in range(int(num_fields)):
        col1, col2 = st.columns(2)
        with col1:
            field_name = st.text_input(f"Field {i+1} name", key=f"fname_{table_name}_{i}")
        with col2:
            field_type = st.selectbox(f"Field {i+1} type", ["INT", "VARCHAR", "DATE", "FLOAT"], key=f"ftype_{table_name}_{i}")
        fields.append((field_name, field_type))

    if st.button("Save table"):
        st.session_state.tables[table_name] = fields
        st.success(f"Saved table {table_name}")

if st.session_state.tables:
    st.subheader("Current Data Model")
    for tname, tfields in st.session_state.tables.items():
        st.write(f"**{tname}**")
        df = pd.DataFrame(tfields, columns=["Field", "Type"])
        st.table(df)

    if st.button("Export Model (JSON)"):
        st.download_button("Download", pd.Series(st.session_state.tables).to_json(), file_name="data_model.json")
