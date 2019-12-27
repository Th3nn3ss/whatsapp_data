import datetime
import os

def read_file(file):
    ''' Reads Whatsapp text file into a list of strings'''
    x = open(file, 'r', encoding = 'utf-8') #Opens the text file into variable x but the variable cannot be explored yet
    y = x.read() #By now it becomes a huge chunk of string that we need to separate line by line
    content = y.splitlines() #The splitline method converts the chunk of string into a list of strings
    return content

chat = read_file('whatsappFile.txt')

print(len(chat))

for i in range(len(chat)):
    try:
        datetime.datetime.strptime(chat[i].split(',')[0], '%d/%m/%Y') #Converts string date
    except ValueError: #Returns an error if the string is not a datetime object
        chat[i-1] = chat[i-1] + ' ' + chat[i] #Appends the next line to the previous line
        chat[i] = "NA" #Replace the unwanted text element with 'NA'

#Handle more than double-line texting
for i in range(len(chat)):
    if chat[i].split(' ')[0] == 'NA':
        chat[i] = 'NA'
while True:
    try:
        chat.remove("NA")
    except ValueError:
        break

date = [chat[i].split(',')[0] for i in range(len(chat))]
