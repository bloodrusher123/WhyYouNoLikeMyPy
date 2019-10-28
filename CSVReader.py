import csv
import win32com.client
import win32com
import os
import sys

DocInsureMailbox = "jbateman@markerstudy.com"
SearchMailbox = "UATTalk2us@insurancefactory.co.uk"
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
#----Testing----
#inbox = outlook.GetDefaultFolder(6)
#messages =inbox.items


folder = outlook.Folders.Item("UAT Talk 2 Us")
inbox=folder.Folders.Item("Inbox")
messages= inbox.items

file = "C:/Users/jbateman/Documents/TestCSV.csv"

with open(file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count =0
    for row in csv_reader:
        for message in messages:
            if row[0] in message.Body or row[0] in message.Subject:
                NewMsg = message.Forward()
                NewMsg.Body = message.Body
                NewMsg.subject = message.Subject
                NewMsg.To = DocInsureMailbox
                NewMsg.Send()
                row[5] = "Moved Mail"
                print("Sent")
            elif row[1] in message.Body or row[1] in message.Subject:
                NewMsg = message.Forward()
                NewMsg.Body = message.Body
                NewMsg.subject = message.Subject
                NewMsg.To = DocInsureMailbox
                NewMsg.Send()
                row[5] = "Moved Mail"
                print("Sent")
            elif row[2] in message.Body or row[2] in message.Subject:
                NewMsg = message.Forward()
                NewMsg.Body = message.Body
                NewMsg.subject = message.Subject
                NewMsg.To = DocInsureMailbox
                NewMsg.Send()
                row[5] = "Moved Mail"
                print("Sent")
            elif row[3] in message.Body or row[3] in message.Subject:
                NewMsg = message.Forward()
                NewMsg.Body = message.Body
                NewMsg.subject = message.Subject
                NewMsg.To = DocInsureMailbox
                NewMsg.Send()
                row[5] = "Moved Mail"
                print("Sent")
            elif row[4] in message.Body or row[4] in message.Subject:
                NewMsg = message.Forward()
                NewMsg.Body = message.Body
                NewMsg.subject = message.Subject
                NewMsg.To = DocInsureMailbox
                NewMsg.Send()
                row[5] = "Moved Mail"
                print("Sent")
            else:
                row[5] = "Chaser Required"
                print("Not Found")
            
                
