import streamlit as st

st.set_page_config(page_title="ECD Reading Coach", page_icon="📚")

st.title("📚 My ECD Reading Coach 🇿🇼")
st.write("ECD A - Teacher Melody Zindoga - Harare")

letters = {
    "A": "🍎 A for Apple - Apuro",
    "B": "⚽ B for Ball - Bhora",
    "C": "🐱 C for Cat - Katsi",
    "D": "🐶 D for Dog - Imbwa",
    "E": "🐘 E for Elephant - Nzou",
    "F": "🐟 F for Fish - Hove",
    "G": "🍇 G for Grapes - Mazambiringa",
    "H": "🏠 H for House - Imba"
}

letter = st.selectbox("Sarudza Bhii / Choose Letter:", list(letters.keys()))

if letter:
    st.success(f"## {letters[letter]}")
    st.balloons()

st.divider()
st.subheader("🎤 Verenga / Read Aloud")
audio = st.audio_input("Rekodha mwana achiverenga / Record child")

if audio:
    st.success("Basa rakanaka! Good job! 🌟")

st.caption("Made with love for ECD learners in Zimbabwe")
