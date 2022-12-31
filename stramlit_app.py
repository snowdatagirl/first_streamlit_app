import streamlit

streamlit.title('my parent new healthy dinner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text(' Hard-Boiled Free-Range Egg')
streamlit.title('my mom s new healthy dinner')
streamlit.header('Breakfast favorite')
streamlit.text('🥣🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥬🥬Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🥑🧇avocado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# Display the table on the page.
#streamlit.multiselect("pick some of the fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
streamlit.dataframe(my_fruit_list) 
fruits_selected = streamlit.multiselect("pick some of the fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc(fruits_selected)
streamlit.dataframe(fruits_to_show) 
