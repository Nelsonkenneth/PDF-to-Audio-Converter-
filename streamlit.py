import streamlit as st
import time
#import pdf_test

col1, col2, col3 = st.columns([1, 2 ,3])

col1.markdown(" # Welcome to my Innovative App! ")
col1.markdown(" Here is some info on the app. ")

def change_pdf_state():
    st.sessions_state["pdf"]="done"
    
uploaded_pdf = col2.file_uploader("Uplaod a Pdf file" , on_change=change_pdf_state)

if st.session_state["pdf"] == "done":
    progress_bar = col2.progress(0)
    
    for perc_completed in range(100):
        time.sleep(0.05)
        progress_bar.progress(perc_completed+1)
        
    col2.sucess("Pdf uploaded sucessfully!")
    
    col3.metric(label="Tempearture", value="-1 °C", delta="0 °C")
    
    with st.expender("Click to read more"):
        st.write("Hello, this programm helps convert PDF files to Audio file and translate them too. It is helpful for guy with disabilities and ease Multi-tasking.")
        


