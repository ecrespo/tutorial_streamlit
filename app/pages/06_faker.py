# streamlit_app.py
from streamlit_faker import get_streamlit_faker

def main():

    st_faker = get_streamlit_faker()
    st_faker.subheader()
    st_faker.markdown()
    st_faker.selectbox()
    st_faker.slider()
    st_faker.map()


if __name__ == "__main__":
    main()