import os
import PyPDF2
import streamlit as st
import tempfile

st.write('99msijxsc')
st.markdown("""
            # PDF to Audio File App
            
            ### Created By: Noah Rubin
            📊 [LinkedIn](https://www.linkedin.com/in/noah-rubin1/)  
            
            🧑🏽‍💻 [GitHub](https://github.com/noahrubin989)
            """)

pdf_file = st.file_uploader('Upload a PDF file', type=['pdf'])
if pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    text_list = [reader.pages[p].extract_text().strip().replace('\n', ' ') for p in range(len(reader.pages))]
    text = ''.join(text_list)

    # Set the voice to use (optional)
    voice_dict = {
        'United States': 'Samantha',
        'Australia': 'Karen',
        'India': 'Rishi',
        'South Africa': 'Tessa',
        'Ireland': 'Moira',
        'Scotland': 'Fiona',
        'England': 'Daniel'
    }
    
    voice = st.selectbox('Select a voice', list(voice_dict.keys()))
    
    # Add a slider to adjust the word speed
    word_speed = st.slider('Speed', min_value=100, max_value=500, step=10, value=160)

    # Add a preview button to hear the selected voice and speed
    if st.button('Preview Accent & Convert Text'):
        os.system(f"say -v {voice_dict[voice]} -r {word_speed} Hello my name is {voice_dict[voice]} from {voice} and I am speaking at a speed set to {word_speed}")

    # Add a button to generate and download the audio file
    with tempfile.TemporaryDirectory() as temp_dir:
        output_file_path = os.path.join(temp_dir, "audio.aiff")
        os.system(f"say -v {voice_dict[voice]} -r {word_speed} -o {output_file_path} {text}")
        with open(output_file_path, 'rb') as f:
            st.download_button(label='Download Audio', data=f.read(), file_name='audio.aiff', mime='audio/aiff')


