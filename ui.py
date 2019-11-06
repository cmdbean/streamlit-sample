import streamlit as st
import pandas
import pandas as pd
import numpy
st.title('UI Parts Sample')

st.subheader('Slider')
x = st.slider('x')
st.write(x, 'squared is', x * x)

st.subheader('Slider With Default Value')
hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h

st.subheader('Checkbox')
if st.checkbox('Show hidden text'):
    st.text('Checked!')


df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

chart_data = pandas.DataFrame(
     numpy.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

if st.checkbox('Show dataframe'):
    chart_data = pandas.DataFrame(
       numpy.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option