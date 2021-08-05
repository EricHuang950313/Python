from email.message import EmailMessage
import smtplib
msg = EmailMessage()
msg["From"] = "Sender"
msg["To"] = "Recipient"
msg["Subject"] = "Title"

# Choose one
msg.set_content("NormalDocument")
msg.add_alternative("<h1>HTML-Code:DocumentTypeH1</h1>",subtype="html")

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("Account", "Password")
server.send_message(msg)
server.close()