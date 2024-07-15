import smtplib
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
import os

# Email credentials and server configuration
EMAIL_ADDRESS = 'your_email@example.com'
EMAIL_PASSWORD = 'your_password'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587

# Email sending function
def send_email():
    # Create the email content
    subject = "Daily Report"
    body = "Please find the attached daily report."

    # Create email message
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'recipient@example.com'
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Attach a file (optional)
    filename = 'report.pdf'
    attachment_path = os.path.join('path_to_reports', filename)
    
    if os.path.isfile(attachment_path):
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={filename}')
            msg.attach(part)

    # Connect to the SMTP server and send email
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Schedule the task
schedule.every().day.at("09:00").do(send_email)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)