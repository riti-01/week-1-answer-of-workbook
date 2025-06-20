def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def speak(style_func, message):
    return style_func(message)

print(speak(shout, "hello"))
print(speak(whisper, "HELLO"))
