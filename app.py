import os
import PyPDF2
import streamlit as st

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
    # Set the output file name (optional)
    output_file_path = "audio.aiff"
    # os.system(f"say -v {voice_dict[voice]} -r {word_speed} -o {output_file_path} {text}")
    # with open(output_file_path, 'rb') as f:
        # st.download_button(label='Download Audio', data=f, file_name=output_file_path, mime='audio/aiff')


# import streamlit as st
# import pyttsx3
# import PyPDF2


# class PdfSpeaker:
#     def __init__(self, voice_id='com.apple.speech.synthesis.voice.samantha', words_per_minute=180):
#         self.voice_id = voice_id
#         self.words_per_minute = words_per_minute

#     def get_clean_text(self, reader: PyPDF2.PdfReader) -> str:
#         text_list = [reader.pages[p].extract_text().strip().replace('\n', ' ') for p in range(len(reader.pages))]
#         clean_text = ''.join(text_list)
#         return clean_text

#     def save_audio(self, clean_text, output_path):
#         speaker = pyttsx3.init(driverName='nsss')
#         speaker.setProperty('voice', self.voice_id)
#         speaker.setProperty('rate', self.words_per_minute)  # words per minute
#         speaker.save_to_file(clean_text, output_path)
#         speaker.runAndWait()
#         speaker.stop()


# def main():
#     st.title('PDF Speaker')

#     # Upload a PDF file
#     pdf_file = st.file_uploader('Upload a PDF file', type=['pdf'])
#     if pdf_file:
#         pdf_reader = PyPDF2.PdfReader(pdf_file)

#         # Select a voice
#         voice_dict = {
#             'United States': 'com.apple.speech.synthesis.voice.samantha',
#             'Australia': 'com.apple.speech.synthesis.voice.karen.premium',
#             'India': 'com.apple.speech.synthesis.voice.rishi',
#             'South Africa': 'com.apple.speech.synthesis.voice.tessa',
#             'Ireland': 'com.apple.speech.synthesis.voice.moira',
#             'Scotland': 'com.apple.speech.synthesis.voice.fiona',
#             'England': 'com.apple.speech.synthesis.voice.daniel'
#         }
#         voice = st.selectbox('Select a voice', list(voice_dict.keys()))

#         # Set words per minute
#         words_per_minute = st.slider('Words per minute', min_value=100, max_value=500, value=180)

#         speaker = PdfSpeaker(voice_dict[voice], words_per_minute)
                
#         clean_text = speaker.get_clean_text(pdf_reader)
#         path = "audio.mp3"
#         speaker.save_audio(clean_text,path)
#         with open(path, 'rb') as f:
#             st.download_button(label='Download Audio', data=f, file_name=path, mime='audio/mpeg')


# if __name__ == '__main__':
#     main()
