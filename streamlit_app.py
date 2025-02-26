import streamlit as st

def click_func(col):
    speechContainer.audio(speeches[col], format="audio/mpeg")

st.title("Soundboard App")
st.subheader(
    "Click on a person's name to hear the speech"
)


names = ["Kamala", "Martin", "Brown"]
images = ["assets/kamalaharris.png", "assets/mlk.jpg", "assets/brownjackson.jpg"]
speeches = ["assets/kamala.mp3", "assets/mlk.mp3", "assets/brownjackson.mp3"]

cols = st.columns(len(names))

for a in range(0, len(names)):
    cols[a].image(images[a])
    cols[a].button(names[a], on_click=click_func, args=(a,), use_container_width=True)

speechContainer = st.container(border=True)
speechContainer.write("Audio: ")