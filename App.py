import pyttsx3

synthesizer = pyttsx3.init()
#my_text = input("Enter the text: ")
# synthesizer.save_to_file("Hello World", 'test.mp3')

voices = synthesizer.getProperty('voices')
# for voice in voices:
#     print("Voice:") 
#     print("ID: %s" %voice.id) 
#     print("Name: %s" %voice.name) 
#     print("Age: %s" %voice.age) 
#     print("Gender: %s" %voice.gender) 
#     print("Languages Known: %s" %voice.languages)

fhand = open('text.txt')
for line in fhand:
    print(line)
    print(synthesizer.getProperty('voice'))
    synthesizer.setProperty('voice', voices[1].id)
    synthesizer.setProperty('rate', 150)
    synthesizer.setProperty('volume', 0.5)
    synthesizer.say(line) 
    synthesizer.runAndWait() 
    synthesizer.stop()
