import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from pandasai.llm.openai import OpenAI # type: ignore
from pandasai import SmartDataframe

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

#Function for pandas ai to query a CSV file
def chat_with_csv(df, prompt):
    llm = OpenAI()
    pandas_ai = SmartDataframe(df, config={"llm": llm})
    result = pandas_ai.chat(prompt)
    print(result)
    return result


st.set_page_config(layout='wide')

st.title('ChatCSV powered by LLM')

input_csv = st.file_uploader('Upload your CSV file', type = ['csv'])

if input_csv is not None:
    
    col1, col2 = st.columns([1,1])

    with col1:
        st.info('CSV Uploaded successfully')
        data = pd.read_csv(input_csv)
        st.dataframe(data)

    with col2:
        st.info("Chat with your CSV")

        input_text = st.text_area('enter your query')
        if input_text is not None:
            if st.button('Chat with CSV'):
                st.info('You are a ChatBot assisting the Bridge Officers at Nebraska. You are given a CSV file as an input giving various information about the bridges present in Nebraska. You are supposed to fetch the exact information asked in the query from the CSV file and answer to it. Your query: '+input_text)
                result = chat_with_csv(data, input_text)
                st.success(result)