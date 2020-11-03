# Audiobook Speaker
# Author: Tyler Thompson
import pyttsx3
import PyPDF2
# Get the book info
name = input("Please enter a pdf file location")
book = open(name, 'rb')
# Read the book
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
# Ask what page the user wants to start on
print("There are {0} pages in this book".format(pages))
start = int(input('What page would you like to start on?'))
# Voice Rate of speaker
voiceRate = int(input("What rate of speech would you want? 1-200"))
# Create the speaker
speaker = pyttsx3.init()
speaker.setProperty('rate', voiceRate)
# Start reading through the lines
for num in range(start, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
