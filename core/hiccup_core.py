import speech_recognition as sr

class Hiccup:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.running = True

    def listen(self):
        with sr.Microphone() as source:
            print("Say a command (e.g., 'open explorer')...")
            audio = self.recognizer.listen(source)
            try:
                command = self.recognizer.recognize_google(audio).lower()
                print(f"You said: {command}")
                return command
            except sr.UnknownValueError:
                print("Sorry, I didn’t catch that.")
                return None

    def run(self):
        print("Hiccup is listening! Say 'stop' to quit.")
        while self.running:
            command = self.listen()
            if command:
                if "stop" in command:
                    self.running = False
                    print("Hiccup shutting down.")
                else:
                    self.execute_command(command)

    @staticmethod
    def execute_command(self, command):
        print(f"Processing: {command}")  # Placeholder until terminator is ready

if __name__ == "__main__":
    hiccup = Hiccup()
    hiccup.run()