#!/usr/bin/env python
# coding: utf-8

# In[22]:


import streamlit as st
import sys
import requests



def main():
    st.header("Chaimi Lee")
    st.subheader("Data Science and Mathematics Enthusiast")
    with st.container():
        image_col, text_col = st.columns((1,2))
    with image_col:
        st.image("Lee_Chaimi_Photo.png")

    with text_col:
        st.subheader("Hi! My name is Chaimi")
        st.write("""I am a data science and mathematics enthusiast currently pursuing a Masters degree in Applied Data Science at the University of Southern California. I received my Bachelors degree in Mathematics with a minor in Physics from Santa Clara University. My technical skills include proficiency in Python and I am knowledgeable in statistical/machine learning.\n
In my previous internship at Intel Corporation, I developed and implemented automated solutions to improve workflow efficiency as a software technical consulting engineer. \n
I am seeking opportunities to utilize my skills and experience to make a positive impact in the data science field. \n
Feel free to connect with me to learn more about my background and how I can contribute to your organization!\n
During my free time, I like to go to CorePower yoga, try new restaurants, read about horoscopes, go on hikes, or go for a drive (I finally got my license this year 😎)
            """)

    st.markdown("[Feel free to connect with me on Linkedin](https://www.linkedin.com/in/chaimi-lee/)")
    st.markdown("[Check out my projects on Github](https://github.com/chaimilee)")
    st.markdown("[Reach out to me via email](mailto:chaimilee1@gmail.com)")
    
    #st.write('You selected: ', interests)
if __name__ == '__main__':
    main()

    
