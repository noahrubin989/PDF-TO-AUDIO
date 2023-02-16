import streamlit as st
import pyttsx3
import PyPDF2


class PdfSpeaker:
    def __init__(self, voice_id='com.apple.speech.synthesis.voice.samantha', rate=180):
        self.voice_id = voice_id
        self.rate = rate

    def get_clean_text(self, reader: PyPDF2.PdfReader) -> str:
        text_list = [reader.pages[p].extract_text().strip().replace('\n', ' ') for p in range(len(reader.pages))]
        clean_text = ''.join(text_list)
        return clean_text

    def save_audio(self, clean_text, output_path):
        speaker = pyttsx3.init(driverName='nsss')
        speaker.setProperty('voice', self.voice_id)
        speaker.setProperty('rate', self.rate)  # words per minute
        speaker.save_to_file(clean_text, output_path)
        speaker.runAndWait()
        speaker.stop()


def main():
    st.markdown("""
            # PDF to Audio File App
            
            ### Created By: Noah Rubin
            📊 [LinkedIn](https://www.linkedin.com/in/noah-rubin1/)  
            
            🧑🏽‍💻 [GitHub](https://github.com/noahrubin989)
            """)

    # Upload a PDF file
    pdf_file = st.file_uploader('Upload a PDF file', type=['pdf'])
    if pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Select a voice
        voice_dict = {
            'United States': 'com.apple.speech.synthesis.voice.samantha',
            'Australia': 'com.apple.speech.synthesis.voice.karen.premium',
            'India': 'com.apple.speech.synthesis.voice.rishi',
            'South Africa': 'com.apple.speech.synthesis.voice.tessa',
            'Ireland': 'com.apple.speech.synthesis.voice.moira',
            'Scotland': 'com.apple.speech.synthesis.voice.fiona',
            'England': 'com.apple.speech.synthesis.voice.daniel'
        }
        
        voice = st.selectbox('Select a voice', list(voice_dict.keys()))
        rate = st.slider('Select speed', min_value=100, max_value=500, value=180)

        if st.button('Preview Accent'):
            engine = pyttsx3.init()
            engine.setProperty('voice', voice_dict[voice])
            engine.setProperty('rate', rate)
            engine.say(f'Hi! I am from {voice}. Here is me with the current audio settings applied')
            engine.runAndWait()
        
        
        speaker = PdfSpeaker(voice_dict[voice], rate)      
        clean_text = speaker.get_clean_text(pdf_reader)
        path = "audio.mp3"
        speaker.save_audio(clean_text,path)
        with open(path, 'rb') as f:
            st.download_button(label='Download Audio', 
                               data=f, 
                               file_name=path, 
                               mime='audio/mp3')


if __name__ == '__main__':
    main()
