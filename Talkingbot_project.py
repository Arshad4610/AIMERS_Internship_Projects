import os
import pyttsx3
import google.generativeai as genai
import speech_recognition as sr


genai.configure(api_key="AIzaSyB4ag4TCtAc72QfwEffoclTM806aaoAZyo")
recognizer = sr.Recognizer()
# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)

# response = chat_session.send_message("ISRO Chandrayan 3 limit only 200 words  each like consists of 30 words.")
#
# print(response.text)

def recognize_speech_from_mic():
# Initialize the recognizer


  # Use the microphone as the source of the audio
  with sr.Microphone() as source:
    print("Please wait. Calibrating microphone...")
    # Listen for 5 seconds and create the ambient noise energy level
    recognizer.adjust_for_ambient_noise(source, duration=5)
    print("Microphone calibrated. Start speaking.")

    # Capture the audio
    audio = recognizer.listen(source)

    try:
      # Recognize speech using Google Web Speech API
      print("Recognizing...")
      text = recognizer.recognize_google(audio)

      print("You said: " + text)
      ins = " give response,limit to 100 words Every line has 30 words"
      qfromuser=ins+text

      response = chat_session.send_message(qfromuser)
      print(response.text)

      engine = pyttsx3.init()
      rate = engine.getProperty('rate')  # Speed of speech
      engine.setProperty('rate', rate - 50)  # Reduce the speed

      # Set properties (optional)
      # Convert text to speech
      engine.say(response.text)

      # Wait for the speech to finish
      engine.runAndWait()

    except sr.UnknownValueError:
      print("Google Web Speech API could not understand the audio")
    except sr.RequestError as e:
      print("Could not request results from Google Web Speech API; {0}".format(e))

recognize_speech_from_mic()
