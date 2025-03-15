# import streamlit as st

# st.title("UNIT CONVERTER APP")
# st.markdown("### convert LENGTH ,WEIGHT AND TIME instantly")
# st.write("select and enter the value to be converted")
# category=st.selectbox("choose a category",["Length","Weight","Time"]) #this is a set
# def convert_unit(category,value,unit):
#     #length converting
#     if category=="Length":
#         if unit == "kilometer to miles":
#             return value * 0.621371
#         elif unit =="miles to kilometer":
#              return value / 0.621371
        
#         #weight converting
#     elif category=="Weight":
#         if unit == "kilogram to Pounds":
#             return value * 2.20462
#         elif unit=="Pounds to kilogram":
#             return value / 2.20462
#     #time converting
#     elif category=="Time":
#         if unit== "Seconds to Minutes":
#             return value /60
#         elif unit=="Minutes to Seconds":
#             return value * 60
#         elif unit== "Minutes to Hours":
#             return value/60
#         elif unit=="Hours to Minutes":
#             return value*60
#         elif unit =="Hours to Days":
#             return value / 24
#         elif unit =="Days to Hours":
#             return value * 24
        
#     if category == "Length" :
#         unit=st.selectbox("Select conversion",["kilometer to Miles","Miles to kilometer"])  
#     elif category == "Weight":
#         unit=st.selectbox("Select conversion",["kilogram to Pounds","Pounds to kilogram"])   
#     elif category =="Time":
#         unit=st.selectbox("select conversion",["Seconds to Minutes","Minutes to Seconds","Minutes to Hours","Hours to Minutes","Hours to Days","Days to Hours"])        
#         value=st.number_input("enter the value to convert") 
#     if st.button("Convert"):
#         rezult = convert_unit(category ,value,unit)
#         st.success(f"the rezult is {rezult}")
        

import streamlit as st

# App title and description
st.title("💎UNIT CONVERTER APP💎")
st.markdown("### Convert LENGTH, WEIGHT, AND TIME instantly")
st.write("Select a category and enter the value to be converted")

# Dropdown to select category
category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

# Function to handle conversions
def convert_unit(category, value, unit):
    # Length conversion
    if category == "Length":
        if unit == "kilometer to miles":
            return value * 0.621371
        elif unit == "miles to kilometer":
            return value / 0.621371

    # Weight conversion
    elif category == "Weight":
        if unit == "kilogram to pounds":
            return value * 2.20462
        elif unit == "pounds to kilogram":
            return value / 2.20462

    # Time conversion
    elif category == "Time":
        if unit == "seconds to minutes":
            return value / 60
        elif unit == "minutes to seconds":
            return value * 60
        elif unit == "minutes to hours":
            return value / 60
        elif unit == "hours to minutes":
            return value * 60
        elif unit == "hours to days":
            return value / 24
        elif unit == "days to hours":
            return value * 24

# Selecting units based on category
if category == "Length":
    unit = st.selectbox("Select conversion "
    "", ["kilometer to miles", "miles to kilometer"])
elif category == "Weight":
    unit = st.selectbox("Select conversion", ["kilogram to pounds", "pounds to kilogram"])
elif category == "Time":
    unit = st.selectbox("Select conversion", 
        ["seconds to minutes", "minutes to seconds", 
         "minutes to hours", "hours to minutes", 
         "hours to days", "days to hours"]
    )

# Input value for conversion
value = st.number_input("Enter the value to convert", min_value=0.0)

# Convert button and result display
if st.button("Convert"):
    result = convert_unit(category, value, unit)
    st.success(f"The result is: {result}")
