import streamlit as st
from gtts import gTTS
import io

st.set_page_config(page_title="ECD Smart Reading Coach", page_icon="📚")
st.title("📚 My ECD Smart Reading Coach 🇿🇼")
st.write("ECD A - Teacher Melody Zindoga - Now with Correction!")

letters_data = {
    "A": {"word": "A for Apple - Apuro", "say": "A for Apple, Apuro"},
    "B": {"word": "B for Ball - Bhora", "say": "B for Ball, Bhora"},
    "C": {"word": "C for Cat - Katsi", "say": "C for Cat, Katsi"},
    "D": {"word": "D for Dog - Imbwa", "say": "D for Dog, Imbwa"},
    "E": {"word": "E for Elephant - Nzou", "say": "E for Elephant, Nzou"},
    "F": {"word": "F for Fish - Hove", "say": "F for Fish, Hove"},
    "G": {"word": "G for Grapes - Mazambiringa", "say": "G for Grapes, Mazambiringa"},
    "H": {"word": "H for House - Imba", "say": "H for House, Imba"},
}

letter = st.selectbox("Sarudza Bhii / Choose Letter:", list(letters_data.keys()))
data = letters_data[letter]
st.success(f"## {data['word']}")

st.subheader("1️⃣ Teerera - Correct Pronunciation")
if st.button(f"🔊 Hear Correct: {data['word']}"):
    tts = gTTS(text=data['say'], lang='en', slow=True)
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    st.audio(fp, format='audio/mp3')
    st.info(f"Correct: **{data['say']}**")

st.divider()
st.subheader("2️⃣ Verenga Iwe - Your Turn")
audio = st.audio_input("Tap to record child")

if audio:
    st.audio(audio)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Correct"):
            st.balloons()
            st.success(f"Basa rakanaka! Excellent! 🌟 You said: {data['word']}")
    with col2:
        if st.button("❌ Mistake - Correct Me"):
            st.error("Hazvina mhosva! Let's correct:")
            tts2 = gTTS(text=f"Correct is {data['say']}. Say {data['say']}", lang='en', slow=True)
            fp2 = io.BytesIO()
            tts2.write_to_fp(fp2)
            fp2.seek(0)
            st.audio(fp2, format='audio/mp3')
            st.info(f"🗣️ Say: **{data['say'].upper()}** - Repeat 3 times!")

st.caption("Made by Teacher Melody V2 with Correction")