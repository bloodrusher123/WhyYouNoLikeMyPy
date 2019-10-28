import csv
import win32com.client
import win32com
import os
import sys

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

inbox = outlook.GetDefaultFolder(6)
messages =inbox.items

file = "C:/Users/jbateman/Documents/TestCSV.csv"

with open(file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count =0
    for row in csv_reader:
        for message in messages:
            if row[1] in message.body:
                NewMsg = message.Forward()
                NewMsg.body = message.body
                NewMsg.subject = message.subject
                NewMsg.To = DocInsureMailbox
                NewMsg.send()
                print("Yeah")
            else:
                print("")
