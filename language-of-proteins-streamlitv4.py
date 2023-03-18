import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import streamlit as st
import streamlit.components.v1 as components
import numpy as np
from utils import splitchain,contains_specific_letters,TransformACP,TransformAMP
import platform
from packaging import version
if version.parse(platform.python_version()) < version.parse("3.8.0"):
    import pickle5 as pickle
else:
   import pickle

# save the model called exported_pipeline with
# filename = 'xgb_acp_model.sav'
# pickle.dump(exported_pipeline, open(filename, 'wb'))

# load the models

acp_model = pickle.load(open('xgb_acp_model.sav', 'rb'))
amp_model = pickle.load(open('xgb_amp_model.sav', 'rb'))
dna_model = pickle.load(open('xgb_acp_model.sav', 'rb'))

# initialize test results
resultsacp = ''
resultsamp = ''
resultsdna = '' 

# Display Wal-Mart Labs logo.
st.image("instadeep.jpeg" )
st.markdown("<h1 style='text-align: center; color: black;'></h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: black;'>Learning The Language of Proteins</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: black;'></h1>", unsafe_allow_html=True)

user_input = st.text_input(
    "Copy/Paste your amino acid sequence here: ex:     'ATFCHCRRSCYSTEYSYGTCTVMGINWRFCCL (ACP)',  'AVKDTYSCFIMRGKCRHECHDFEKPIGFCTKLNANCYM'")
# Print out the values entered by the user

x = user_input.upper()

if contains_specific_letters(x):
    st.write("The sequence you entered contains letters not used in ACP/APM/DNA_Binding Proteins")
else:
    if len(x)>1:
        st.markdown("<h1 style='text-align: center; color: black;'></h1>", unsafe_allow_html=True)

        # ACP
        # Transform to numbers
        acp_sample = TransformACP(x)
        # code to take the variable and run the predictions on it
        resultsacp = acp_model.predict(acp_sample)
        
        #AMP
        amp_sample = TransformAMP(x)
        resultsamp = amp_model.predict(amp_sample)
        
        st.write("The sequence you entered is:", x)
        if resultsacp == 0: 
            st.write("Not an Anticancer Peptide")
        elif resultsacp == 1:   
            st.write("It is an Anticancer Peptide")
        else:
            st.write('Undetermined ACP ') 
        if resultsamp == 0: 
            st.write("Not an Antimicriobial Peptide")
        elif resultsamp == 1:   
            st.write("It is an Antimicrobial Peptide")
        else:
            st.write('Undetermined AMP ') 


