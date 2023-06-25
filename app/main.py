import streamlit as st


# Define la función main donde se muestra la página principal de tutoriales de streamlit
def main():
    st.title("Tutoriales de streamlit")
    # Colocar un enlace al intro de streamlit
    st.markdown("[Intro de streamlit](http://localhost:8501/Intro)")
    st.markdown("[Diagrama de Venn](http://localhost:8501/diagram_venn)")



if __name__ == "__main__":
    main()