import pyttsx3

msg = '''盼望着，盼望着，东风来了，春天的脚步...'''
teacher = pyttsx3.init()
teacher.say(msg)
teacher.runAndWait()