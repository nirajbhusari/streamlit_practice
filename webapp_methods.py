import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time
import altair as alt

st.title("Streamlit Example App")
st.markdown("This is a simple Streamlit web app.")

st.header("1. Basic Widgets")

st.subheader("Text")
st.text("This is a text element")

st.subheader("Markdown")
st.markdown("You can use **Markdown** to format text.")

#displaying data using Panda
st.subheader("2. Displaying Data")
data = pd.DataFrame({"Name": ["Alice", "Bob", "Charlie", "David"],
                     "Age": [25, 30, 35, 40]})
data.index=[1, 2, 3, 4]
"""if you want Name as first column"""
"""data.set_index("Name", inplace=True)"""
st.dataframe(data)

#plotting using matplotlib
st.subheader("3.Plotting")
st.write("You can create plots too.")
x = np.linspace(0, 15, 220)
y = np.cos(x)
fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)

#widgets
st. subheader("4. Interactive Widgets")
st.subheader("Slider")
slide_value = st.slider("Select a value:", 0, 100, 50)

st.subheader("Select Box")
options = ["1.Option1", "2.Option2", "3. Option3"]
selected_option = st.selectbox("Choose an option:", options)

st.subheader("Button")
if st.button("Click Me"):
    st.success("Button Clicked!")

st.subheader("Checkbox")
checkbox = st.checkbox("Check this box.")

#sidebar functionality
st.sidebar.header("5.Sidebar")
st.sidebar.markdown("This is the sidebar where you can add extra content.")

st.sidebar.subheader("Sidebar functionality")

user_input = st.sidebar.text_input("Enter text:")
st.sidebar.write("You entered:", user_input)

number_input = st.sidebar.number_input("Enter a number", 0, 100, 50)
st.sidebar.write("Selected number:", number_input)

file = st.sidebar.file_uploader("Upload a file:", type=["txt","csv","jpeg","jpg"])
if file is not None:
    st.subheader("File uploaded.")

#image uploading
st.title("Streamlit Image/Camera Example.")
st.markdown("Display images in your Streamlit app")

uploaded_image = st.file_uploader("Upload Image:")

camera_started = st.button("Start Camera")

if camera_started:
    with st.expander("Start camera."):
        camera_image = st.camera_input("Camera")

    if camera_image:
        img = Image.open(camera_image)
        gray_camera_img = img.convert("L")
        st.image(gray_camera_img)

if uploaded_image:
    img = Image.open(uploaded_image)
    gray_uploaded_img = img.convert('L')
    st.image(gray_uploaded_img)


#progress bar
st.title("Progress Bar example")
st.markdown("Show a progress bar in your Streamlit App")

progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.1)
    progress_bar.progress(i+1)


#interactive plot
st.title("Interactive Plot")
st.markdown("Create interactive plot")

data = pd.DataFrame({"x": range(10), "y": [x ** 2 for x in range(10) ]})

scatter_chart = alt.Chart(data).mark_circle().encode(x="x", y="y", tooltip=["x", "y"])
st.altair_chart(scatter_chart, use_container_width=True)