import smtplib
from email.mime.text import MIMEText

def send_followup_email(name, email, product):
    sender_email = "yourcompany@example.com"
    app_password = "your-app-password"

    message_body = f"Hi {name},\n\nThank you for your interest in our {product}. We'll be in touch shortly.\n\n- Sales Team"

    msg = MIMEText(message_body)
    msg['Subject'] = f"Thanks for your interest in our {product}"
    msg['From'] = sender_email
    msg['To'] = email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, [email], msg.as_string())
        print(f"📧 Email sent to {email}")
    except Exception as e:
        print("Error sending email:", e)
