import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
df=pd.read_csv("steam.csv")
df_clean=pd.read_csv("stream cleaning.csv")
df_eda=df_clean.copy()
st.set_page_config(page_title="Steam store analysis",layout="wide")

st.title("Steam Store Games Dataset Analysis , By [Ahmed Ramadan](https://www.linkedin.com/in/ahmed-ramadan-18b873230/)")
st.header("About Dataset:")
st.markdown("I wanted to create a dataset from scratch based around games on the Steam Store. Using data  [gathered from the Steam Store and SteamSpy APIs](https://nik-davis.github.io/posts/2019/steam-data-collection/), this dataset provides information about various aspects of games on the store, such as its genre and the estimated number of owners.Gathered around May 2019, it contains most games on the store released prior to that date. Unreleased titles were removed as well as many non-games like software, though some may have slipped through .")
st.markdown("------------------------")


col1,col2=st.columns(2)

with col1:
    st.markdown("This is the sample of original dataframe without do any cleaning or preprocessing :")
    sample=st.dataframe(df.sample(10))
    btn=st.button("Display another sample")
    if btn:
        print(sample)

with col2:
    st.markdown("This is the sample of dataframe after clean , preprocessing and add some columns:")
    st.dataframe(df_clean.sample(10))
st.markdown("------------------------")
st.header("EDA and visualization")
st.subheader("In Exploratory data analysis (EDA) we have 3 type")
st.markdown("1) Univarate")
st.markdown("2) Bivarate")
st.markdown("3) Multivarate")

sb=st.selectbox("__Select what type to show visualization it__",["Univarate","Bivarate","Multivarate"])

#####################################################################################################################################

if sb=="Univarate":
    st.subheader("Define Univariate :")
    st.markdown("__**In statistics**__ : Univariate statistics summarize only one variable at a time.")
    st.markdown("**__In visualization__**: Univariate visualization summarize only to display distribution or how many repeat same value in data.")
    st.markdown("- __Frist__ Display distribution of only numercial columns: ")
    sb_uni=st.selectbox("Select column to show distribution it ",["required_age","price","achievement","positive or negative ratings","average or median playtime"])
    if sb_uni=="required_age":
        col1,col2=st.columns(2)
        with col1:
            fig=px.histogram(data_frame=df_eda,x=["required_age"])
            st.plotly_chart(fig)
        with col2:
            fig=px.box(data_frame=df_eda,x=["required_age"])
            st.plotly_chart(fig)

    if sb_uni=="achievement":
        col1,col2=st.columns(2)
        with col1:
            fig=px.histogram(data_frame=df_eda,x=["achievements"])
            st.plotly_chart(fig)
        with col2:
            fig=px.box(data_frame=df_eda,x=["achievements"])
            st.plotly_chart(fig)
        st.markdown("- note : we have outliers in achievements")
    
    if sb_uni=="price":
        col1,col2=st.columns(2)
        with col1:
            fig=px.box(data_frame=df_eda,x="price")
            st.plotly_chart(fig)
        with col2:
            fig=px.histogram(data_frame=df_eda,x="price")
            st.plotly_chart(fig)
        st.markdown("- note : we have outliers in price")
    
    if sb_uni=="positive or negative ratings":
        fig=px.box(data_frame=df_eda,x=["positive_ratings","negative_ratings"])
        st.plotly_chart(fig)
        st.markdown("- note : we have many outliers in positive_ratings and negative_ratings")
   
    if sb_uni=="average or median playtime":
        fig=px.box(data_frame=df_eda,x=["average_playtime","median_playtime"])
        st.plotly_chart(fig)
        st.markdown("- note : we have many outliers in average_playtime and median_playtime")
    
    st.markdown("--------")
    st.markdown("__Second__ Display some question and answer it with visualization ")
    st.markdown("\n")

    #######Q1
    col1,col2=st.columns(2)
    with col1:
        st.subheader("What is the 5 most frequent games?")
        
        fig=px.bar(data_frame=df_eda["name"].value_counts().head(5).reset_index(),
                x="name",
                y="index",
                labels={"name":"frequency","index":"name"},
                text_auto="0.2s")
        fig.update_traces(textfont_size=12,textposition="outside")
        st.plotly_chart(fig)
    with col2:
        st.subheader("What is the 5 most frequent developer ?")

        fig=px.bar(data_frame=df_eda["developer"].value_counts().head(5).reset_index(),
                x="developer",
                y="index",
                labels={"developer":"frequency","index":"developer"},
                text_auto="0.2s")
        fig.update_traces(textfont_size=12,textposition="outside")
        st.plotly_chart(fig)
    
    #######Q2
    col1,col2=st.columns([1.2,1])
    with col1:
        st.subheader("What is the 5 most frequent of publisher ?")
        
        fig=px.pie(data_frame=df_eda["publisher"].value_counts().head(5).reset_index(),
                names="index",
                values="publisher",
                labels={"index":"publisher","publisher":"frequency"})
        st.plotly_chart(fig)

    with col2:
        
        st.subheader("What is the 5 most categories are played?")
        fig=px.bar(data_frame=df_eda["categories"].value_counts().head(5).reset_index(),
                x="categories",
                y="index",
                labels={"categories":"frequency","index":"categories"},
                text_auto="0.2s")
        fig.update_traces(textfont_size=12,textposition="outside")
        st.plotly_chart(fig)

    #######Q3
    col1,col2=st.columns(2)
    with col1:
        st.subheader("How many games are english or not ?")
 
        fig=px.bar(data_frame=df_eda["english"].value_counts(),
                    x=df_eda["english"].value_counts().index,
                    y=df_eda["english"].value_counts().values,
                labels={"x":"english","y":"count"},
                text_auto="0.2s")
        fig.update_traces(textfont_size=12,textposition="outside")
        fig.update_layout(title_text="How many games are english or not",title_x=0.5)
        st.plotly_chart(fig)
    with col2:

        st.subheader("How many value count of each required age?")
        fig=px.bar(data_frame=df_eda["required_age"].value_counts().reset_index().sort_values(by="index"),
                x="index",
                y="required_age",
                labels={"required_age":"frequency","index":"required_age"},
                text_auto="0.2s")
        fig.update_traces(textfont_size=12,textposition="outside")
        st.plotly_chart(fig)

#######################################################################################################################

elif sb=="Bivarate":
    st.subheader("Define Bivarate :")
    st.markdown("Bivariate analysis is the analysis of exactly two variables.")
    st.markdown("__Now__ Display some question and answer it with visualization ")
    st.markdown("--------")

    #######Q1
    col1,col2=st.columns(2) 
    with col1:
        st.subheader(" What is the 5 most expensive games? (name/price)")
        d=df_eda.sort_values(by="price",ascending=False).head(5)[["name","price"]]
        fig=px.bar(data_frame=d,
                x="price",
                y="name",
                text_auto="0.2s",
                )
        fig.update_traces(textfont_size=12,textposition="outside")
        fig.update_layout(title_text="the 5 most expensive games",title_x=0.3)
        st.plotly_chart(fig)
    
    with col2:
        d=df_eda.groupby("year_of_released")["price"].mean().reset_index().round(2)
        st.subheader("What is average  price games  that are published for each years ?(year_of_released/price)")
        fig=px.bar(data_frame=d,
                x="year_of_released",
                y="price",
                text_auto="0.2s",
                )
        fig.update_traces(textfont_size=12,textposition="outside")
        fig.update_layout(title_text="Average  price games  that are published for each years",title_x=0.2)
        st.plotly_chart(fig)
        st.markdown("- Note : we note that in 2013 this is the year has a maximum average of price")
    st.markdown("------")

    #######Q2
    col1,col2,col3=st.columns(3)
    with col1:
        d=df_eda[df_eda["platforms_windows"]==1] #this data for windows

        d2=d.groupby(["developer"]).agg({"developer":"count"}).rename(columns={"developer":"count"}).reset_index().sort_values(by="count",ascending=False).head(5)
        st.subheader("What is the 5 most developer for windows?(platforms_windows/developer)")
        fig=px.pie(data_frame=d2,
                names="developer",
                values="count",
                hole=0.3)
        fig.update_layout(title_text="The 5 most developer for windows",title_x=0.2)
        st.plotly_chart(fig)

    with col2:
        st.subheader("What is the 5 most developer for Mac?(platforms_mac/developer)")
        #pandas
        d=df_eda[df_eda["platforms_mac"]==1] #this data for mac
        d2=d.groupby(["developer"]).agg({"developer":"count"}).rename(columns={"developer":"count"}).reset_index().sort_values(by="count",ascending=False).head(5)
        
        #ploty
        fig=px.pie(data_frame=d2,
                names="developer",
                values="count",
                hole=0.3)
        fig.update_layout(title_text="The 5 most developer for mac",title_x=0.2)
        st.plotly_chart(fig)

    with col3:
        st.subheader("What is the 5 most developer for Linux?(platforms_linux/developer)")
        #pandas
        d=df_eda[df_eda["platforms_linux"]==1] #this data for linux
        d2=d.groupby(["developer"]).agg({"developer":"count"}).rename(columns={"developer":"count"}).reset_index().sort_values(by="count",ascending=False).head(5)
        #ploty
        fig=px.pie(data_frame=d2,
                names="developer",
                values="count",
                hole=0.3)
        fig.update_layout(title_text="The 5 most developer for linux",title_x=0.4)
        st.plotly_chart(fig)
    st.markdown("-  - we note that for last 3 questions ; __Choice of Games company__ is __the top__ developer company for all platforms and most developer company for mac and linux is __same__")
    st.markdown("------")

    #######Q3
    col1,col2=st.columns(2)
    with col1:
        st.subheader("What is the 5 most developer which have positive ratings?(developer/positive_ratings)")
        #pandas
        d=df_eda.groupby("developer")["positive_ratings"].mean().sort_values(ascending=False).head(5).reset_index()
        #ploty
        fig=px.bar(data_frame=d,
                x="positive_ratings",
                y="developer",
                text_auto="0.2s",
                )
        fig.update_traces(textfont_size=12,textposition="outside")
        fig.update_layout(title_text="The 5 most developer which have positive ratings",title_x=0.2)
        st.plotly_chart(fig)
    
    with col2:
        st.subheader("What is the 5 most developer which have negative ratings ?(developer/negative_ratings)")
        #pandas
        d=df_eda.groupby("developer")["negative_ratings"].mean().sort_values(ascending=False).head(5).reset_index()
        #ploty
        fig=px.bar(data_frame=d,
                x="negative_ratings",
                y="developer",
                text_auto="0.2s",
                )
        fig.update_traces(textfont_size=12,textposition="outside")
        fig.update_layout(title_text="The 5 most developer which have negative ratings",title_x=0.2)
        st.plotly_chart(fig)
    st.markdown("we note that top developer company have negative ratings is __PUBG Corporation__ , and __Valve company and Hidden Path Entertainment company__ aslo is in top 5 company have negative ratings ,Although they are in top 5 company have __positive ratings__")
    st.markdown("------------")

    #######Q4
    col1,col2=st.columns(2)
    with col1:
        st.subheader("What is the 5 highest genres have average play time?(genres/average_playtime)")
        #pandas
        d=df_eda.groupby("genres")["average_playtime"].mean().sort_values(ascending=False).head(5).reset_index()
        #ploty
        fig=px.bar(data_frame=d,
                x="average_playtime",
                y="genres",
                text_auto="0.2s",
                )
        fig.update_traces(textfont_size=12,textposition="outside")
        fig.update_layout(title_text="The 5 highest genres have average play time",title_x=0.5)
        st.plotly_chart(fig)
        st.markdown("- we note that any games is __[Free to Play / Indie / Massively Multiplayer / Action / Adventure]__ have largest average_playtime")

    with col2:
        st.subheader("What is the 5 lowerest genres have average play time?(genres/average_playtime)")
        #pandas
        d=df_eda.groupby("genres")["average_playtime"].mean().sort_values(ascending=True).head(5).reset_index()
        st.write(d)
        st.markdown("- we note that almost games is __[Gore]__ have lowest average_playtime")
    st.markdown("------------")

##############################################################################################################################
else:
    st.subheader("Define Multivarate :")
    st.markdown("Multivarate analysis is the analysis of more than two variables.")
    st.markdown("__Now__ Display some question and answer it with visualization ")
    st.markdown("--------")

    #######Q1
    col1,col2,col3=st.columns(3)
    with col1:
        st.subheader("What is the 5 most expensive develpoer for windows ? (platforms_windows/ developer /price)")
        #pandas 
        d=df_eda[df_eda["platforms_windows"]==1] #to select all platforms of windows
        data1=d.groupby("developer")["price"].mean().sort_values(ascending=False).head(5).reset_index()
        #ploty
        fig=px.bar(data_frame=data1,
                x="developer",
                y="price",
                text_auto="0.2s",
                )
        fig.update_traces(textfont_size=12,textposition="outside")
        fig.update_layout(title_text=" What is the 5 most expensive develpoer for windows",title_x=0.3)
        st.plotly_chart(fig)
        st.markdown("- we note that top delelpoer companies have expensive games for platform windows are __[Suomen Kuljetusturva Oy , SideFX ,YoYo Games Ltd ,Capt McCay Soft]__.")

    with col2:
        st.subheader("What is the 5 most expensive develpoer for mac? (platforms_mac /developer /price)")
        #pandas 
        d=df_eda[df_eda["platforms_mac"]==1] #to select all platforms of mac
        data2=d.groupby("developer")["price"].mean().sort_values(ascending=False).head(5).reset_index()
        #ploty
        fig=px.bar(data_frame=data2,
                x="developer",
                y="price",
                text_auto="0.2s",
                )
        fig.update_traces(textfont_size=12,textposition="outside")
        fig.update_layout(title_text=" What is the 5 most expensive develpoer for mac",title_x=0.3)
        st.plotly_chart(fig)
        st.markdown("- we note that top developer companies have expensive games for platform mac are __[YoYo Games Ltd , Capt. McCay Soft ,Matt Workman ,The Game Creators	]__.")

    with col3:
        st.subheader("What is the 5 most expensive develpoer for linux ?(platforms_linux/developer/price)")
        #pandas 
        d=df_eda[df_eda["platforms_linux"]==1]
        data3=d.groupby("developer")["price"].mean().sort_values(ascending=False).head(5).reset_index()
        #ploty
        fig=px.bar(data_frame=data3,
                x="developer",
                y="price",
                text_auto="0.2s",
                )
        fig.update_traces(textfont_size=12,textposition="outside")
        fig.update_layout(title_text=" What is the 5 most expensive develpoer for linux",title_x=0.3)
        st.plotly_chart(fig)
        st.markdown("- we note that top developer companies have expensive games for platform linux are __[The Game Creators , Wingware , KADOKAWA , Yoji Ojima , Laminar Research	 , BrashMonkey]__.")
    st.markdown("--------")

    #######Q2
    st.subheader("What is the average price of reach year if english or not ? (year_of_released / english / price )")

    col1,col2,col3=st.columns(3)#to make igure in center
    
    with col2:
        
        #pandas
        d=df_eda.groupby(["year_of_released","english"])["price"].mean().reset_index().round(2)
        #ploty
        fig=px.bar(data_frame=d,
                x="year_of_released",
                y="price",
                text_auto="0.2s",
                color="english"
                )
        fig.update_traces(textfont_size=12,textposition="outside")
        fig.update_layout(title_text=" What is the average price of reach year if english or not ?",title_x=0.2)
        st.plotly_chart(fig)
    st.markdown("- we note that max average price if games are not engish were __2015__ and min average price if games are not engish were __2019__")
    st.markdown("- we note that max average price if games are yes engish were __2013__ and min average price if games are not engish were __2001__")    
    st.markdown("---------")

    #######Q3
    col1,col2,col3=st.columns(3)
    with col1:
        st.subheader("What is the average playtime for required age to platform's windows ?(platforms_window s/ required_age / average_playtime)")
        #pandas
        d=df_eda[df_eda["platforms_windows"]==1]
        data=d.groupby("required_age")["average_playtime"].mean().round(2).reset_index()
        #ploty
        fig=px.pie(data_frame=data,
                names="required_age",
                values="average_playtime",
                hole=0.2)
        fig.update_layout(title_text="What is the average playtime for required age to platform's windows",title_x=0.1)
        st.plotly_chart(fig)

    with col2:
        st.subheader("What is the average playtime for required age to platform's mac ?(platforms_mac / required_age / average_playtime)")
        #pandas
        d=df_eda[df_eda["platforms_mac"]==1]
        data=d.groupby("required_age")["average_playtime"].mean().round(2).reset_index()
        #ploty
        fig=px.pie(data_frame=data,
                names="required_age",
                values="average_playtime",
                hole=0.2)
        fig.update_layout(title_text="what is the average playtime for required age to platform's mac",title_x=0.1)
        st.plotly_chart(fig)
    
    with col3:
        st.subheader("What is the average playtime for required age to platform's linux ?(platforms_linux / required_age / average_playtime)")
        #pandas
        d=df_eda[df_eda["platforms_linux"]==1]
        data=d.groupby("required_age")["average_playtime"].mean().round(2).reset_index()
        #ploty
        fig=px.pie(data_frame=data,
                names="required_age",
                values="average_playtime",
                hole=0.2)
        fig.update_layout(title_text="what is the average playtime for required age to platform's linux",title_x=0.1)
        st.plotly_chart(fig)
    st.markdown("- we note that some how  in mac almost games which required age in __18 age and 16 age__ have max average play time and required age in __7 age__ have min average play time ")
    st.markdown("- we conclude from last 3 question that almost activity aged are 18 age and 16 age and who have 7 age not activated")
    st.markdown("- I suggest that if any company need to success or increase profits it should care who has 16 or 18 age and publish games suitable for ages from 7")
    st.markdown("---------")

    #######Q4
    col1,col2=st.columns(2)
    with col1:
        st.subheader("What is the top 10 developer have positive ratings and what is it genres ? (developer / genres /positive_ratings)")
        #pandas
        data=df_eda.groupby(['developer','genres'])["positive_ratings"].sum().sort_values(ascending=False).reset_index().head(10)
        #ploty
        fig=px.bar(data_frame=data,
                x="developer",
                y="positive_ratings",
                text_auto="0.2s",
                color="genres"
                )
        fig.update_traces(textfont_size=12,textposition="outside")
        fig.update_layout(title_text="What is the top 10 developer have positive ratings and what is it genres",title_x=0.2)
        st.plotly_chart(fig)
        st.markdown("- We note that most genres have the highest positive ratings __[Action/ Free to Play / RPG ]__ from developer compaies like __[Valve / Hidden Path Entertainment / PUBG Corporation	]__")
    
    with col2:
        st.subheader("What is the top 10 developer have negative ratings and what is it genres?(developer / genres / negative_ratings)")
        #pandas
        data=df_eda.groupby(['developer','genres'])["negative_ratings"].sum().sort_values(ascending=False).reset_index().head(10)
        #ploty
        fig=px.bar(data_frame=data,
                x="developer",
                y="negative_ratings",
                text_auto="0.2s",
                color="genres"
                )
        fig.update_traces(textfont_size=12,textposition="outside")
        fig.update_layout(title_text="What is the top 10 developer have negative ratings and what is it genres",title_x=0.2)
        st.plotly_chart(fig)
        st.markdown("- We note that most genres have the highest negative ratings __[Action/ Free to Play / RPG ]__ from developer compaies like __[Valve / Hidden Path Entertainment / PUBG Corporation	]__")
    st.markdown("\n")
    st.markdown("\n")
    st.markdown("\n")
    st.markdown("- We conclude that despite these genres and the same developer compaies, they have a very large number of positive ratings and negative ratings, which indicates that they are very popular companies and genres.")
    st.markdown("---------")
##############################################################################################################################
st.markdown("--------")

st.header("Conclusions:")
st.subheader("__My Conclusions after analysis this data__")
st.markdown("- I suggest that if any company need to success or increase profits it should care who has 16 or 18 age and publish games suitable for ages from 7")
st.markdown("- I suggest that if any company need to success or increase profits it should care with genres  __[Action/ Free to Play / RPG ]__")
st.markdown("- I recommend if you publish any games you shound support windows platform and language is english")