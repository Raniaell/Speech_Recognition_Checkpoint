import streamlit as st
import speech_recognition as sr
import pyaudio
import io
import wave

def transcribe_speech():
    # Initialize recognizer class
    r = sr.Recognizer()
    # Reading Microphone as source
    with sr.Microphone() as source:
        st.info('Speak now...')
        print("This is only available for english speakers! Thanks for understanding!")
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        print("this is your recording: ",audio_data)
        
        try:
            text = r.recognize_google(audio_data)
            print(audio_data.get_wav_data(), text)
            st.write("Transcription:", text)
        except:
            print("Sorry I didn't get that or you run out of time")
            st.write("Sorry I didn't get that/You run out of time")
       
    save_audio(audio_data)   
      
def save_audio(audio_data):
    with st.echo(code_location="below"):
        # Save recorded audio to WAV file
        with io.BytesIO() as wav_buffer:
            with wave.open(wav_buffer, "wb") as wav_file:
                wav_file.setnchannels(1)
                wav_file.setsampwidth(audio_data.sample_width)
                wav_file.setframerate(audio_data.sample_rate)
                wav_file.writeframes(audio_data.frame_data)
            wav_bytes = wav_buffer.getvalue()
        
        # Save audio bytes to a file
        audio_filename = "recorded_audio.wav"
        with open(audio_filename, "wb") as audio_file:
            audio_file.write(wav_bytes)
        st.success(f"Audio recording saved as '{audio_filename}'")

def main():
    st.title("Speech Recognition App")
    st.write("Click on the microphone to start speaking:")

    # add a button to trigger speech recognition
    if st.button("Start Recording"):
        audio_data=transcribe_speech()
        if audio_data is not None:
            st.audio(audio_data, format="audio/wav")
            


if __name__ == "__main__":
    main()