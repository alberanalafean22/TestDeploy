import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import soundfile as sf
import os

# Menyisipkan HTML eksternal (index.html) ke dalam aplikasi Streamlit
html_file_path = "index.html"

# Memastikan file HTML ada, kemudian membacanya
if os.path.exists(html_file_path):
    with open(html_file_path, 'r') as f:
        html_code = f.read()
    components.html(html_code, height=600, scrolling=True)

# Streamlit UI untuk upload file audio
st.title("Upload and Process Audio File")

uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3", "flac"])

if uploaded_file is not None:
    # Menyimpan file audio yang di-upload ke direktori sementara
    file_path = f"./uploads/{uploaded_file.name}"
    
    if not os.path.exists('./uploads'):
        os.makedirs('./uploads')

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Memproses file audio dengan soundfile
    data, samplerate = sf.read(file_path)
    audio_array = np.array(data)

    # Menampilkan beberapa informasi tentang audio
    st.write(f"Audio File: {uploaded_file.name}")
    st.write(f"Sample Rate: {samplerate} Hz")
    st.write(f"Audio Shape: {audio_array.shape}")

    # Menampilkan audio yang di-upload
    st.audio(file_path)

    # Menampilkan sebagian kecil dari audio array untuk debugging
    st.write("Audio Array (first 100 samples):")
    st.write(audio_array[:100])  # Hanya menampilkan 100 sample pertama
