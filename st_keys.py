from _plotly_utils.basevalidators import FlaglistValidator
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(layout="wide")

#IMPORTS 
labs = pd.read_csv('labs_cards.csv')
shoreline = pd.read_csv('shoreline.csv')
reserve = pd.read_csv('reserve.csv')
interchange = pd.read_csv('interchange.csv')


st.write('   ')
st.write('   ')
st.write('    ')
st.markdown("<h1 style='text-align: center; color: rgb(215,208,149); font=Lucida Console'>ESCAPE FROM TARKOV</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: rgb(215,208,149); font=Lucida Console'>12.12 KEYS - MARKET PRICING HISTORY</h6>", unsafe_allow_html=True)
st.write('     ')

col1,col2 = st.columns(2)

with col1:
    #LABS
    fig = px.area(labs,facet_col=labs['name'].str.upper(),x=labs['timestamp'],y=labs['price'],facet_col_wrap=2,labels=dict(timestamp='',price=''))
    fig.update_yaxes(matches=None)
    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    fig.for_each_trace(lambda trace: trace.update(fillcolor = 'rgb(215,208,149)'))
    fig.for_each_trace(lambda trace: trace.update(line_color = 'rgb(215,208,149)'))
    fig.update_xaxes(showgrid=False,color='rgb(215,208,149)',zeroline=False)
    fig.update_yaxes(showgrid=False,color='rgb(215,208,149)',zeroline=False)   

    fig.update_layout(
        font_family="Lucida Console",
        font_color="rgb(215,208,149)",
        title_font_family="Lucida Console",
        title_font_color="rgb(215,208,149)",
    )

    fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })

    st.markdown("<h1 style='text-align: center; color: rgb(215,208,149); font=Lucida Console'>LABS</h1>", unsafe_allow_html=True)
    st.plotly_chart(fig,use_container_width=True)
    #END LABS

    
    #SHORELINE
    fig = px.area(shoreline,facet_col=shoreline['name'].str.upper(),x=shoreline['timestamp'],y=shoreline['price'],facet_col_wrap=10,labels=dict(timestamp='',price=''))
    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    fig.for_each_trace(lambda trace: trace.update(fillcolor = 'rgb(215,208,149)'))
    fig.for_each_trace(lambda trace: trace.update(line_color = 'rgb(215,208,149)'))
    fig.update_xaxes(showgrid=False,color='rgb(215,208,149)',zeroline=False)
    fig.update_yaxes(showgrid=False,color='rgb(215,208,149)',zeroline=False)

    fig.update_layout(
        font_family="Lucida Console",
        font_color="rgb(215,208,149)",
        title_font_family="Lucida Console",
        title_font_color="rgb(215,208,149)",
    )

    fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })

    st.markdown("<h1 style='text-align: center; color: rgb(215,208,149);'>SHORELINE</h1>", unsafe_allow_html=True)
    st.plotly_chart(fig,use_container_width=True)
    #END SHORELINE

with col2:
    #RESERVE
    fig = px.area(reserve,facet_col=reserve['name'].str.upper(),x=reserve['timestamp'],y=reserve['price'],facet_col_wrap=8,labels=dict(timestamp='',price=''))
    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    fig.for_each_trace(lambda trace: trace.update(fillcolor = 'rgb(215,208,149)'))
    fig.for_each_trace(lambda trace: trace.update(line_color = 'rgb(215,208,149)'))
    fig.update_xaxes(showgrid=False,color='rgb(215,208,149)',zeroline=False)
    fig.update_yaxes(showgrid=False,color='rgb(215,208,149)',zeroline=False)

    fig.update_layout(
        font_family="Lucida Console",
        font_color="rgb(215,208,149)",
        title_font_family="Lucida Console",
        title_font_color="rgb(215,208,149)",
        font_size=13
    )

    fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)'
    })

    st.markdown("<h1 style='text-align: center; color: rgb(215,208,149);'>RESERVE</h1>", unsafe_allow_html=True)
    st.plotly_chart(fig,use_container_width=True)
    #END RESERVE

        #INTERCHANGE
    fig = px.area(interchange,facet_col=interchange['name'].str.upper(),x=interchange['timestamp'],y=interchange['price'],facet_col_wrap=3,labels=dict(timestamp='',price=''))
    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    fig.for_each_trace(lambda trace: trace.update(fillcolor = 'rgb(215,208,149)'))
    fig.for_each_trace(lambda trace: trace.update(line_color = 'rgb(215,208,149)'))
    fig.update_xaxes(showgrid=False,color='rgb(215,208,149)',zeroline=False)
    fig.update_yaxes(showgrid=False,color='rgb(215,208,149)',zeroline=False)

    fig.update_layout(
        font_family="Lucida Console",
        font_color="rgb(215,208,149)",
        title_font_family="Lucida Console",
        title_font_color="rgb(215,208,149)",
    )

    fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)'
    })

    st.markdown("<h1 style='text-align: center; color: rgb(215,208,149);'>INTERCHANGE</h1>", unsafe_allow_html=True)
    st.plotly_chart(fig,use_container_width=True)
    #END INTERCHANGE


st.markdown("<h6 style='text-align: center; color: rgb(215,208,149);'>DATA PROVIDED BY TARKOV-TOOLS.COM</h6>", unsafe_allow_html=True)