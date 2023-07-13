import time
from STTPipeline.homecube import VoiceAssistant
from STTPipeline.recording_thread import RecordingThread

# Use your classes
voice_assistant = VoiceAssistant('/home/marco/mycroft-precise/homecube.tflite')
voice_assistant.start()

recording_thread = RecordingThread(voice_assistant.get_wake_word_event())
recording_thread.start()

# Sleep forever
while True:
    time.sleep(1)