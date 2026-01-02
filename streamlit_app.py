# Import python packages
import streamlit as st
#from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(f"Customize Your Smoothie :cup_with_straw: {st.__version__}")
st.write("""Choose the fruits you want in your custom smoothie"""
  """Replace this example with your own code!
  **And if you're new to Streamlit,** check
  out our easy-to-follow guides at
  [docs.streamlit.io](https://docs.streamlit.io).
  """
)


#import streamlit as st
#title = st.text_input("Movie title", "Life of Brian")
#st.write("The current movie title is", title)
name_on_order = st.text_input("Name on Smoothie:")
st.write("The name on your smoothie will be:", name_on_order)


#import streamlit as st
"""
option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)
st.write("You selected:", option)

option = st.selectbox(
    "What is your favorite fruit?",
    ("Banana", "Strawberries", "Peaches"),
)
st.write("Your favourite fruit is:", option)
""" 
cnx = st.connection("snowflake")
session=cnx.session()
#session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list=st.multiselect('Choose up to 5 ingredients:'
                               , my_dataframe
                               , max_selections=5)
if ingredients_list:
    #if ingredients_list is not null: then do everything below this line that is indented.
    #!!!4spaces not tab
    #st.write(ingredients_list)
    #st.text(ingredients_list)
    
    ingredients_string=''
    
    for fruit_chosen in ingredients_list: 
        ingredients_string += fruit_chosen + ' ' #+= operator means "add this to what is already in the variable"
        
    #st.write(ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)           
        values ('""" + ingredients_string + """','"""+name_on_order+ """')"""
        #values ('""" + ingredients_string """')"""
    
    st.write(my_insert_stmt)
    #st.stop()
    
    time_to_insert = st.button('Submit Order')

#if ingredients_string:
#if time_to_insert:
#    session.sql(my_insert_stmt).collect()
#    st.success('Your Smoothie is ordered!', icon="✅")


#New section to display smoothiefroot nutrition information
import requests
smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
st.text(smoothiefroot_response)

























    
    
