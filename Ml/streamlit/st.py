##streamlit
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import time 

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

st.header("5.Widgets")
with st.form("input form"):
    name = st.text_input("enter your name")
    age = st.number_input("enter your age")
    mod = st.radio("select your mode",("happy","sad","neutral"))
    language=st.multiselect("select your language",("english","hindi","gujarati"))
    submit = st.form_submit_button("submit")
    if submit:
        st.write("name:",name)
        st.write("age:",age)
        st.write("mode:",mod)
        st.write("language:",language)


col1 ,col2, col3 = st.columns((4,1,1))
with col1:
    st.text_input("enter your name")
    st.number_input("enter your age")
with col2:
    st.radio("select your mode",("happy","sad","neutral"))
    st.multiselect("select your language",("english","hindi","gujarati"))
with col3:

    st.title("Output")


#with st.form("input form"):
#    col1, col2 = st.columns(2)
#    with col1:
#        name = st.text_input("enter your name")
#       age = st.number_input("enter your age")
#    with col2:
#        mod = st.radio("select your mode",("happy","sad","neutral"))
#        language=st.multiselect("select your language",("english","hindi","gujarati"))
#    submit = st.form_submit_button("submit")
#   if submit:
#

col1,col2 = st.columns(2)
with col1:
    number = st.slider("select a number",0,100)
with col2:
    colour = st.color_picker("select a colour","#00FF00")



st.text_area("Enter your message")
st.date_input("Select a date")
st.time_input("Select a time")
st.file_uploader("Upload a file")


st.header("6. Media")
st.image("https://picsum.photos/400",caption="random image")
st.video("https://w3schools.com/html/mov_bbb.mp4")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")



st.sidebar.header("Sidebar header")
st.sidebar.write("this is a sidebar text")
st.sidebar.button("click me")
option = st.sidebar.selectbox("select an option",("option 1","option 2","option 3"))


##
tab1,tab2,tab3 = st.tabs(["tab1","tab2","tab3"])
with tab1:
    st.write("this is a tab1")
with tab2:
    st.write("this is a tab2")
with tab3:
    st.write("this is a tab3")




with st.container():
    st.write("this is a container")

with st.expander("expander"):
    st.write("this is an expander")

with st.spinner("loading data..."):
    time.sleep(2)

st.toast("toast message",icon="😃")

st.page_link("http://streamlit.io",label="streamlit website",icon="☠️")
