import streamlit as st

st.title("🌍 Unit Converter App")
st.markdown("### Converts Length, Weight, and Time Instantly")
st.write("Welcome! Select a category, enter a value, and get the converted result in real-time")


category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
    elif category == "Weight":
        if unit == "kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to kilograms":
            return value / 2.20462
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Kilometers to miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("⚖ Select Conversion", ["kilograms to Pounds", "Pounds to kilograms"])
elif category == "Time":
    unit = st.selectbox("⏰ Select Conversion", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])


value = st.number_input("Enter the value to convert")



if st.button("convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is: {result:.2f}")
else:
    st.warning("Please enter a value greater than zero.")

