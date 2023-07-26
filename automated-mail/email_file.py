import yagmail

email = yagmail.SMTP(user="developertools.cool@gmail.com", password="pxhlbhwbbzthodrb")

email.send(to="e8czcmmg@freeml.net",
           subject="Hi there!",
           contents="Hi, this is the body of the email!\nErhan",
           attachments="design.txt")