##streamlit
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

##page configuration
st.set_page_config(
    page_title="streamlit function demo",
    page_icon="😃",
    layout="centered"
)
##title or text elements

st.title("Hello World")
st.header("1.Text elements")
st.subheader("markdown,code,latex")
st.markdown("**bold text**,*italic text*,code text")
st.code("print('hello everyone')",language="python")
st.latex(r"a^2+b^2=c^2")

st.divider()

##metrices and messages
st.header("2.metrices and messages")
st.metric(label="Revenue",value=1234,delta="10%",delta_color="inverse")
st.error("this is an error message")
st.warning("this is a warning message")
st.info("this is an info message")
st.success("this is a success message")
st.exception(ValueError("this is an exception message"))

st.divider()

##data display
st.header("3.data display")
df=pd.DataFrame(np.random.rand(10,2),columns=["a","b"])
st.dataframe(df)
st.table(df.head())
st.json(df.to_dict())

st.divider()

##charts
st.header("4.charts")
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)
chart = alt.Chart(df.reset_index()).mark_line().encode(x="index",y="a")
st.altair_chart(chart,use_container_width=True)
fig , ax = plt.subplots()
ax.plot(df.index,df.a)
st.pyplot(fig)
st.divider()