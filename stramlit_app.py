import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
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
#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(my_fruit_list)
#create the repeatable code block
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
   
#new section to display
streamlit.header("Fruityvice Fruit Advice!")
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
        streamlit.error("please select a fruit toget information.")
   else:
       back_from_function = get_fruityvice_data(fruit_choice)
       streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()
  
#streamlit.stop()   #dont run anything past here while we troubleshoot
#import snowflake.connector




streamlit.header("The fruit load list contains:")
#snowflake related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("select * from fruit_load_list")
         return my_cur.fetchall()
 #add a button to load the fruit
if streamlit.button('get fruit load list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)
    
#allow the end user to add a fruit to the list
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
         a="insert into fruit_load list values('"+new_fruit+"')"
         print(a)
         my_cur.execute(a)
         ##my_cur.execute("insert into fruit_load list values('"+new_fruit+"')")
         ##return "insert into fruit_load list values('"+new_fruit+"')"
            
         return "thanks for adding" + new_fruit
    
add_my_fruit = streamlit.text_input('what fruit would you like to add?')
if streamlit.button('add a fruit to the list'):
    my_cnx =snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_function)
    


