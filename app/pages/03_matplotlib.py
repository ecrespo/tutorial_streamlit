import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import random
import calendar
import datetime
import math

import pylab

from matplotlib.sankey import Sankey
from matplotlib.patches import Circle

import quandl

from Graphs.linear_char import load_data


def button_manager(body):
    if st.button('Show code'):
        st.subheader("code")
        st.code(body, language='python')
        if st.button("Hide code"):
            st.container()


def line_char():
    st.header("Matplotlib - Line char")
    df = load_data()
    # Define title and size
    plt.rcParams['figure.figsize'] = (40, 30)
    plt.plot(df)
    plt.title('prices vs dates')
    plt.xlabel('Dates')
    plt.ylabel('Prices')
    st.pyplot(plt)
    st.subheader('Code:')
    body = '''
            #imports
            import random
            import radar
            import datetime
            import numpy as np
            import pandas as pd
            def generateData(n:int,start:datetime,end:datetime):
                listdata = []
                str_start = start.strftime('%Y-%m-%d')
                str_end = end.strftime('%Y-%m-%d')
                delta = end - start
                for _ in range(n):
                    date = radar.random_datetime(start=str_start, stop=str_end).strftime("%Y-%m-%d")
                    price = round(random.uniform(900, 1000), 4)
                    listdata.append([date, price])

                # Create dataframe from listdata add columns date and price
                df = pd.DataFrame(listdata, columns = ['Date', 'Price'])
                # Convert date in type datetime
                df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
                df = df.groupby(by='Date').mean()

                return df

            start = datetime.datetime(2019, 8, 1)
            end = datetime.datetime(2019, 8, 30)

            df = generateData(50,start,end)

            # Define title and size
            plt.rcParams['figure.figsize'] = (40, 30)
            plt.plot(df)
            plt.title('prices vs dates')
            plt.xlabel('Dates')
            plt.ylabel('Prices')
            plt.show()
            '''
    button_manager(body)


def time_series():
    st.subheader('Semilogarithm Graph')
    start = pd.to_datetime("2012-01-01")
    end = pd.to_datetime("2018-03-27")
    delta = quandl.get("WIKI/DAL", start_date=start, end_date=end)
    jb = quandl.get("WIKI/JBLU", start_date=start, end_date=end)
    sw = quandl.get("WIKI/LUV", start_date=start, end_date=end)
    delta["Adj. Close"].plot(label="Delta", figsize=(16, 8), title="Precio de cierre ajustado")
    jb["Adj. Close"].plot(label="Jet Blue")
    sw["Adj. Close"].plot(label="Southwest")
    plt.title("Stock market")
    plt.legend();
    st.pyplot(plt)
    body = '''
    # Code:
    st.subheader('Semilogarithm Graph')
    start = pd.to_datetime("2012-01-01")
    end = pd.to_datetime("2018-03-27")
    delta = quandl.get("WIKI/DAL", start_date=start, end_date=end)
    jb = quandl.get("WIKI/JBLU", start_date=start, end_date=end)
    sw = quandl.get("WIKI/LUV", start_date=start, end_date=end)
    delta["Adj. Close"].plot(label="Delta", figsize=(16, 8), title="Precio de cierre ajustado")
    jb["Adj. Close"].plot(label="Jet Blue")
    sw["Adj. Close"].plot(label="Southwest")
    plt.title("Stock market")
    plt.legend();
    plt.show()
    '''
    button_manager(body)


def semilog_graph():
    st.subheader('Semilogarithm Graph')
    plt.rcParams['font.size'] = 10.
    plt.rcParams['figure.figsize'] = (24, 20)

    x = np.arange(0., 20, 0.01)
    fig = plt.figure()
    ax2 = fig.add_subplot(311)
    y2 = np.sin(np.pi * (x ** (1.0 / 2.0)))
    ax2.semilogx(x, y2);
    ax2.set_xlim([0, 10]);
    ax2.grid(True)
    ax2.set_ylabel('log X')
    st.pyplot(fig)
    body = '''
    # Code:
    plt.rcParams['font.size'] = 10.
    plt.rcParams['figure.figsize'] = (24, 20)

    x = np.arange(0., 20, 0.01)
    fig = plt.figure()
    ax2 = fig.add_subplot(311)
    y2 = np.sin(np.pi * (x ** (1.0 / 2.0)))
    ax2.semilogx(x, y2);
    ax2.set_xlim([0, 10]);
    ax2.grid(True)
    ax2.set_ylabel('log X')
    plt.show()
    '''
    button_manager(body)


def polar_coordinates():
    st.subheader('Polar coordinates')
    st.write('r = 2 cosine(pi*t) 0<t <2')
    theta = np.arange(0., 2., 0.005) * np.pi

    r = 2 * np.abs(np.cos(theta))

    plt.polar(theta, r)
    plt.thetagrids(range(45, 360, 90))
    plt.rgrids(np.arange(0.2, 3.1, .7), angle=0);
    st.pyplot(plt)
    body = '''
    #
    st.subheader('Polar coordinates')
    st.write('r = 2 cosine(pi*t) 0<t <2')
    theta = np.arange(0., 2., 0.005) * np.pi

    r = 2 * np.abs(np.cos(theta))

    plt.polar(theta, r)
    plt.thetagrids(range(45, 360, 90))
    plt.rgrids(np.arange(0.2, 3.1, .7), angle=0);
    plt.show()
    '''
    button_manager(body)


def graph_sin():
    st.subheader('Graph sin')
    st.write('sine(pi*t) 0<t <10')
    t = np.linspace(0, 10, 30)
    y = np.sin(t)
    plt.plot(t, y, 'o', color='purple')
    plt.plot(t, y, '-ok')
    st.pyplot(plt)
    body = '''
    #Code:
    t = np.lin-space(0, 10, 30)
    y = np.sin(t)
    plt.plot(x, y, 'o', color='purple')
    plt.plot(x, y, '-ok')
    st.pyplot(plt)
    plt.show()
    '''
    button_manager(body)


def bar_chart():
    """
The bar_chart function creates a bar chart using the matplotlib library.
It takes no arguments and returns nothing.

:return: A bar chart
:doc-author: Trelent
"""
    st.subheader('Bar chart')
    months = list(range(1, 13))
    sold_quantity = [round(random.uniform(100, 200)) for _ in range(1, 13)]
    figure, axis = plt.subplots()
    plt.xticks(months, calendar.month_name[1:13], rotation=20)

    # plot graph
    plot = axis.bar(months, sold_quantity)

    for rectangle in plot:
        height = rectangle.get_height()
        axis.text(rectangle.get_x() + rectangle.get_width() / 2., 1.002 * height, '%d' % int(height), ha='center',
                  va='bottom')

    plt.title('Sold quantities monthly')
    plt.xlabel('Months')
    plt.ylabel('Sold quantities')
    st.pyplot(plt)
    body = '''
        #Code:
        months = list(range(1, 13))
        sold_quantity = [round(random.uniform(100, 200)) for _ in range(1, 13)]
        figure, axis = plt.subplots()
        plt.xticks(months, calendar.month_name[1:13], rotation=20)

        # plot graph
        plot = axis.bar(months, sold_quantity)

        for rectangle in plot:
            height = rectangle.get_height()
            axis.text(rectangle.get_x() + rectangle.get_width() / 2., 1.002 * height, '%d' % int(height), ha='center',
                    va='bottom')


        plt.title('Sold quantities monthly')
        plt.xlabel('Months')
        plt.ylabel('Sold quantities')
        plt.show()
        '''
    button_manager(body)


def scatter_plot():
    st.subheader('Scatter plot')
    x = np.random.rand(100)
    girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
    boys_grades = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
    grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    plt.scatter(grades_range, girls_grades, color='r')
    plt.scatter(grades_range, boys_grades, color='g')
    plt.xlabel('Grades Range')
    plt.ylabel('Grades Scored')
    st.pyplot(plt)
    body = '''
    #Code:
    x = np.random.rand(100)
    girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
    boys_grades = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
    grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    plt.scatter(grades_range, girls_grades, color='r')
    plt.scatter(grades_range, boys_grades, color='g')
    plt.xlabel('Grades Range')
    plt.ylabel('Grades Scored')
    plt.show()
    '''
    button_manager(body)


def bubble_plot():
    st.subheader('Bubble plot')
    sheet_df_dictonary = pd.read_excel(r'pages/resources/Canada.xlsx',
                                       engine='openpyxl', sheet_name=['Canada by Citizenship (2)'], skiprows=0)
    df = sheet_df_dictonary['Canada by Citizenship (2)']
    df = df.drop(columns=[
        'Type',
        'Coverage',
        'AREA',
        'AreaName',
        'REG',
        'RegName',
        'DEV',
        'DevName',
    ]).set_index('OdName')
    venezuela = df.loc['Venezuela (Bolivarian Republic of)']
    brasil = df.loc['Brazil']
    # Normalize data
    v_normal = venezuela / venezuela.max()
    b_normal = brasil / brasil.max()
    years = list(range(1980, 2014))
    plt.figure(figsize=(12, 8))
    plt.scatter(years, brasil,
                color='darkblue',
                alpha=0.5,
                s=b_normal * 2000)
    plt.scatter(years, venezuela,
                color='purple',
                alpha=0.5,
                s=v_normal * 2000,
                )
    plt.xlabel("Years", size=14)
    plt.ylabel("Number of immigrants", size=14)
    st.pyplot(plt)
    body = '''
    #Code:
    sheet_df_dictonary = pd.read_excel(r'./data/Canada.xlsx',
                                       engine='openpyxl', 
                                       sheet_name=['Canada by Citizenship (2)'], 
                                       skiprows=0)
    df = sheet_df_dictonary['Canada by Citizenship (2)']
    df = df.drop(columns=[
        'Type',
        'Coverage',
        'AREA',
        'AreaName',
        'REG',
        'RegName',
        'DEV',
        'DevName',
    ]).set_index('OdName')
    venezuela = df.loc['Venezuela (Bolivarian Republic of)']
    brasil = df.loc['Brazil']
    # Normalize data
    v_normal = venezuela / venezuela.max()
    b_normal = brasil / brasil.max()
    years = list(range(1980, 2014))
    plt.figure(figsize=(12, 8))
    plt.scatter(years, brasil,
                color='darkblue',
                alpha=0.5,
                s=b_normal * 2000)
    plt.scatter(years, venezuela,
                color='purple',
                alpha=0.5,
                s=v_normal * 2000,
                )
    plt.xlabel("Years", size=14)
    plt.ylabel("Number of immigrants", size=14)
    '''
    button_manager(body)


def area_plot():
    st.subheader('Area and stacked plot')
    days = [1, 2, 3, 4, 5]
    sleeping = [7, 8, 6, 11, 7]
    eating = [2, 3, 4, 3, 2]
    working = [7, 8, 7, 2, 2]
    playing = [8, 5, 7, 8, 13]
    plt.plot([], [], color='m', label='Sleeping', linewidth=5)
    plt.plot([], [], color='c', label='Eating', linewidth=5)
    plt.plot([], [], color='r', label='Working', linewidth=5)
    plt.plot([], [], color='k', label='Playing', linewidth=5)
    plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'c', 'r', 'k'])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Stack Plot')
    plt.legend()
    st.pyplot(plt)
    body = '''
        #Code:
    days = [1, 2, 3, 4, 5]
    sleeping = [7, 8, 6, 11, 7]
    eating = [2, 3, 4, 3, 2]
    working = [7, 8, 7, 2, 2]
    playing = [8, 5, 7, 8, 13]
    plt.plot([], [], color='m', label='Sleeping', linewidth=5)
    plt.plot([], [], color='c', label='Eating', linewidth=5)
    plt.plot([], [], color='r', label='Working', linewidth=5)
    plt.plot([], [], color='k', label='Playing', linewidth=5)
    plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'c', 'r', 'k'])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Stack Plot')
    plt.legend()
    st.pyplot(plt)
        '''
    button_manager(body)


def pie_chart():
    st.subheader('Pie chart')
    labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
    sizes = [15, 30, 45, 10]
    explode = (0, 0, 0.1, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.tight_layout()
    st.pyplot(plt)
    body = '''
    #Code:
    labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
    sizes = [15, 30, 45, 10]
    explode = (0, 0, 0.1, 0)  
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  
    plt.tight_layout()
    plt.show()
    '''
    button_manager(body)


def circle_graph():
    st.subheader('Circle chart')
    # Pie chart
    labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
    sizes = [15, 30, 45, 10]
    # colors
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90)
    # draw circle
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    # Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')
    plt.tight_layout()
    st.pyplot(plt)
    body = '''
    #Code:
    # Pie chart
    labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
    sizes = [15, 30, 45, 10]
    # colors
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, colors=colors, labels=labels, autopct='%1.1f%%', startangle=90)
    # draw circle
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    # Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')
    plt.tight_layout()
    st.pyplot(plt)
    '''
    button_manager(body)


def main():
    st.set_page_config(
        page_title='Matplotlib graphs',
        page_icon='👨‍🔬',
        layout='centered',
        initial_sidebar_state='auto',
        menu_items={
            'Get Help': 'https://streamlit.io/',
            'Report a bug': 'https://github.com',
            'About': 'About your application: **Hello world**'
        }
    )
    st.sidebar.title('Matplotlib graphs')
    st.title('Matplotlib graphs')

    graphs = "Line chart,Semilogarithm Graph,Polar coordinates,Time series,Graph Sin,Bar chart,Scatter plot,Bubble plot,Area plot and stacked plot,Pie chart,Circle chart,Table chart,Treemap chart,The Sankey class,Polar chart,Histogram,Lollipot chart,Heatmap chart,Radial bar chart".split(
        ",")

    option_graph = st.sidebar.selectbox(
        "graph", graphs
    )

    st.sidebar.write("Option:", option_graph)
    graph_options = {
        'Line chart': line_char,
        'Semilogarithm Graph': semilog_graph,
        'Polar coordinates': polar_coordinates,
        'Time series': time_series,
        'Graph Sin': graph_sin,
        'Bar chart': bar_chart,
        'Scatter plot': scatter_plot,
        'Bubble plot': bubble_plot,
        'Area plot and stacked plot': area_plot,
        'Pie chart': pie_chart,
        'Circle chart': circle_graph
    }
    if option_graph in graph_options:
        graph_options[option_graph]()


if __name__ == "__main__":
    main()
