
import streamlit 

streamlit.header('ππ₯­ Build Your Own Fruit Smoothie π₯π')

streamlit.header('Breakfast Menu')

streamlit.text('π₯£ Omega 3 & Blueberry Oatmeal')
streamlit.text('π₯ Kale, Spinach & Rocket Smoothie')
streamlit.text('πHard-Boiled Free-Range Egg')
streamlit.text('π₯π Avacado Toast')

import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

