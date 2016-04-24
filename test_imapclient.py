from imapclient import IMAPClient

notification_folder = IMAPClient("imap-mail.outlook.com", use_uid=True, ssl=True)
notification_folder.login("paul_h555@outlook.com", "s3rQee!2")
notification_folder.select_folder("INBOX")
messages = notification_folder.search('NOT DELETED')
response = notification_folder.fetch(messages, 'FLAGS RFC822.SIZE')

# Loop through email in notification folder
for msgid, data in response.items():
    msgid_ = notification_folder.fetch(msgid, "INTERNALDATE BODY RFC822")[msgid]
    print("keys " + str(msgid_.keys()))
    rfc822content = msgid_['RFC822']

