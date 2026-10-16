import streamlit as st
from gtts import gTTS
import io

st.set_page_config(page_title="ECD Reading Coach", layout="centered")

st.title("📚 ECD Reading Coach")
st.caption("Teacher Melody - Harare - With Correction")
st.divider()

letters = {
    "A": "A for Apple - Apuro",
    "B": "B for Ball - Bhora",
    "C": "C for Cat - Katsi",
    "D": "D for Dog - Imbwa",
    "E": "E for Elephant - Nzou",
    "F": "F for Fish - Hove",
    "G": "G for Grapes",
    "H": "H for House - Imba"
}

letter = st.selectbox("Choose Letter:", list(letters.keys()))
word = letters[letter]

st.header(word)

st.write("1. Listen Correct")
if st.button(f"Hear {word}"):
    tts = gTTS(text=word, lang='en', slow=True)
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    st.audio(fp, format='audio/mp3')

st.divider()
st.write("2. Your Turn - Record Child")
audio = st.audio_input("Tap to record")

if audio:
    st.audio(audio)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("✅ Good"):
            st.balloons()
            st.success("Basa rakanaka! Excellent!")
    with c2:
        if st.button("❌ Wrong - Fix"):
            st.error(f"Correct is: {word}")
            tts2 = gTTS(text=f"Correct is {word}", lang='en', slow=True)
            fp2 = io.BytesIO()
            tts2.write_to_fp(fp2)
            fp2.seek(0)
            st.audio(fp2, format='audio/mp3')