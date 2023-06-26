# Import the required Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import plotly.express as px



# Functions for each of the pages
def home(uploaded_file):
    if uploaded_file:
        st.header('Begin exploring the data using the menu on the left')
    else:
        st.header('To begin please upload a file')


def data_summary(df):
    st.header('Statistics of Dataframe')
    st.write(df.describe())


def data_header(df):
    st.header('Header of Dataframe')
    st.write(df.head())


def displayplot(df):
    st.header('Plot of Data')

    fig, ax = plt.subplots(1, 1)
    ax.scatter(x=df['Depth'], y=df['Magnitude'])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitude')

    st.pyplot(fig)


def interactive_plot(df):
    col1, col2 = st.columns(2)

    x_axis_val = col1.selectbox('Select the X-axis', options=df.columns)
    y_axis_val = col2.selectbox('Select the Y-axis', options=df.columns)

    fig = px.scatter(df, x=x_axis_val, y=y_axis_val)
    #st.plotly_chart(plot, use_container_width=True)
    st.pyplot(fig)



def main():
    st.set_page_config(layout="wide")
    # Add a title and intro text
    st.title('Earthquake Data Explorer')
    st.text('This is a web app to allow exploration of Earthquake Data')

    # Sidebar setup
    st.sidebar.title('Sidebar')
    upload_file = st.sidebar.file_uploader('Upload a file containing earthquake data')
    # Sidebar navigation
    st.sidebar.title('Navigation')
    options = st.sidebar.radio('Select what you want to display:',
                               ['Home', 'Data Summary', 'Data Header', 'Scatter Plot', 'Fancy Plots'])

    # Check if file has been uploaded
    if upload_file is not None:
        df = pd.read_csv(upload_file)

    # Navigation options
    if options == 'Home':
        home(upload_file)
    elif options == 'Data Summary':
        data_summary(df)
    elif options == 'Data Header':
        data_header(df)
    elif options == 'Scatter Plot':
        displayplot(df)
    elif options == 'Interactive Plots':
        interactive_plot(df)

if __name__ == '__main__':
    main()
