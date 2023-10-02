import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Sales Analysis App",
    page_icon=":sales:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define styles for the app
styles = """
<style>
img {
    max-width: 50%;
}
.sidebar .sidebar-content {
    background-color: #f5f5f5;
}
</style>
"""

# Render styles
st.markdown(styles, unsafe_allow_html=True)

image2 = Image.open(r"C:\Users\ericf\Desktop\Desktop\AssistenteDigital\Projects-main\Learn\sales-prediction.jpg")

# Define header
header = st.container()
with header:
    st.title("Assistente Digital")
    st.write("")

# Define main content
content = st.container()
with content:
    # Load sales dataset
    sale_file = st.file_uploader('Selecione a base de dados')
    if sale_file is not None:
        sale_df = pd.read_excel(sale_file)
    else:
        st.stop()

    sidebar = st.sidebar

    st.subheader("O que deseja?")
    prompt = st.text_input("Escreva aqui:")
    if prompt:
        # Initialize PandasAI and OpenAI
        llm = OpenAI(api_token="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")
        pandas_ai = PandasAI(llm)
        
        # Run PandasAI with user input prompt
        result = pandas_ai.run(sale_df, prompt=prompt)
        
        # Display result
        if result is not None:
            st.write("### Sua resposta está aqui:")
            st.write(result)
