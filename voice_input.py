import speech_recognition as sr

class VoiceInput:
    def __init__(self, timeout=5, phrase_time_limit=5):
        """
        :param timeout: max seconds to wait for user speech
        :param phrase_time_limit: max seconds to capture speech
        """
        self.recognizer = sr.Recognizer()
        self.timeout = timeout
        self.phrase_time_limit = phrase_time_limit

    def listen(self):
        """
        Captures audio from microphone and converts to text.
        :return: recognized text (string) or None
        """
        with sr.Microphone() as source:
            print("🎤 Say something...")

            # Adjust mic noise threshold
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)

            try:
                audio = self.recognizer.listen(
                    source,
                    timeout=self.timeout,
                    phrase_time_limit=self.phrase_time_limit
                )
            except sr.WaitTimeoutError:
                print("⏱️ Timeout: No speech detected")
                return None

        try:
            # Use Google Web Speech API
            text = self.recognizer.recognize_google(audio)
            print("✅ You said:", text)
            return text
        except sr.UnknownValueError:
            print("❌ Could not understand audio")
        except sr.RequestError as e:
            print("⚠️ Could not request results; check your internet connection", e)

        return None
