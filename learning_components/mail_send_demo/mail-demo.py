import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage
import os

load_dotenv()

EMAIL_ADDRESS: str = os.getenv("MY_USER")
EMAIL_PASSWORD: str = os.getenv("MY_PASS")

stock: str = 'AAPL'
target: float = 224.59
current_price: float = 224.05
email_to: str = 'emailto@gmail.com'

msg = EmailMessage()
msg['Subject'] = f'{stock} just hit ${target}'
msg['From'] = EMAIL_ADDRESS
msg['To'] = email_to
msg.set_content('This is a plain text email')

# Load the HTML content from the file
with open("templates/email_template.html", "r") as f:
    html_content = f.read().format(stock=stock, current_price=current_price)

msg.add_alternative(html_content, subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: # Note Class & port
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)


