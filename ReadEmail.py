import win32com.client
import csv


MessageFound = False
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
#accounts = win32com.client.Dispatch("Outlook.Application").Session.Accounts

folder = outlook.Folders.Item("UAT Talk 2 Us")
inbox=folder.Folders.Item("Inbox")
messages= inbox.items
#msg = msg.GetLast()

def rowMessage(row):
    for column in range(0,5):
        for message in messages:
            if row[column] in message.body or row[column] in message.subject:
                MessageFound = True
                returnMessage = message
                break
            else
        if MessageFound:
            break
    return MessageFound, returnMessage

def forwardMessage(msg):
    try:
        NewMsg = msg.Forward()
        NewMsg.Body = msg.Body
        NewMsg.subject = msg.Subject
        NewMsg.To = DocInsureMailbox
        NewMsg.Send()
        MsgSent = True

    except:
        MsgSent = False

    return MsgSent


file = "C:/Users/jbateman/Documents/TestCSV.csv"
with open(file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count =0
for row in csv_reader:
    found, msg = rowMessage(row)
    if found:
        Sent = forwardMessage(msg)
        if Sent:
            row[5] = "Mail Moved"
        else:
            row[5] = "Failed to Move"
    else:
        row[5] = "Requires Chaser"







#for account in accounts:
#    global inbox
#    inbox = outlook.Folders(account.DeliveryStore.DisplayName)
#    print(account.DisplayName)
    
#outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

#inbox = outlook.GetDefaultFolder(6)
#messages =inbox.items
#message= messages.GetLast()
#body_content = message.body
#print(body_content)