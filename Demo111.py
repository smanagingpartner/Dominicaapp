import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


st.set_page_config(page_title = 'My Webpage', page_icon = 'tada', layout = 'wide')

def load_lottieurl(url): 
    r = requests.get(url)
    if r.status_code!= 200:
          return None
    return r.json()
# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)
        
local_css('style_css.py')
        
#------Loading Assets--ew
lottie_coding = load_lottieurl('https://assets5.lottiefiles.com/private_files/lf30_8zaahewg.json')

image = Image.open('images_dom3.png')
img_lottie_animation = Image.open('images.dom11.png')

#------Header Section----

with st.container():
   
    st.subheader('Hi, I am Dominica :wave:')
    st.title('Where Did You Sleep Last Night?(>Desired Info)')
    st.write('Filling out these documents will save time and stream line the entire process. Please See below for Application(>Desired Info)')                   
    st.write('[Learn More>](https://fns1llc.com)')
    
    
    # What We do
#-----PROJECTS----
    
    with st.container():
        st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('What We Do...(>Desired Info)')
        st.write('##')
        st.write(
            """
            On my youtube channel I explain the application and documentation process:(>desired Info)
            - Easy to fill out documents saves you time and streamlines the entire process.(>desired Info)
            - Just fill out the documents and submit them to get the process started.(>desired Info)
            - You have any questions feel free to contact me via email, text or call Phone#.(>desired Info)
            - " It has to be a better way(>desired Info)
            
            If this sounds interesting to you please fill out the forms below!(>desired info)
            """)
            
    with right_column:        
            st_lottie(lottie_coding, height = 300, key = 'coding')

#-----PROJETS----------------            
            
with st. container():
    st.write('---')
    st.header('Applications and Forms....(>Desired Info)')
    st.write('##')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(image, caption ='We are working together to enable a better of life for veterens')
        st.image(img_lottie_animation)
        st.image('images.dom11.png')
        #add image
        with text_column:
            st.subheader('We are Ready To Serve Our Veterans')
            st.write("""
                 About Us(>desired info)
                 Notes and News Letters for the fall(>desired info)
                 Questions and Concerns(>desired info)
                 What's your next step??(>desired info)
                 Learn about your options(>desired info)
                 FORMS(>desired info)
                 """
                )
            st.markdown('[Watch the video>](https://youtu.be/EIw8SO6dadQ')
        
with st. container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
        st.subheader('How to fill out your forms')
        
        st.write(
            """
            Our contact form helps our clients reach us with ease.(>desired info)
        
            """)
        
        st.markdown('[Watch the video>](https://youtu.be/nRrhI3yTc9w')
        
 #-----Contact Info----
with st.container():
    st.write('---')
    st.header('Get in touch with me if you have any questions!!!')
    
    
    #contact submit.co  !!!CHANGE EMAIL !!
    
    contact_form = """
    <form action="https://formsubmit.co/dominica.newett@uwforsyth.org" method="POST" />
    <input type="hidden" name="_captcha" value="false">
         <input type='hidden' = name '_capthca' value = 'false'> 
         <input type="text" name="name" Placeholder = 'Your Name' required>
         <input type="email" name="email" Placeholder = 'Your Email' required>
         <input text area name = "message" Placeholder = 'Your Message Here' required></textarea>
         <button type="submit">Send</button>
    </form> 
"""
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html = True)
    with right_column:
         st.empty()
