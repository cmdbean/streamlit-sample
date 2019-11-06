from pathlib import Path
import streamlit as st
import pandas as pd

file_paths = sorted([p.as_posix() for p in Path('data').iterdir()], reverse=True)

file_path = st.selectbox('target_file', file_paths)

df = pd.read_csv(file_path)
st.dataframe(df)

group_keys = [c for c in df.columns if c in ['Pclass', 'Sex', 'Age', 'Parch', 'Embarked']]
selected_group_key = st.multiselect('group_key', group_keys, default=['Sex'])

agg_funcs = ['sum', 'mean', 'count']
selected_func = st.multiselect('agg_func', agg_funcs, default=['sum'])

pivot = pd.pivot_table(df, index=selected_group_key, values=['Survived'], aggfunc=selected_func)

st.dataframe(pivot)

