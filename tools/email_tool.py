import smtplib
from email.mime.text import MIMEText
from langchain.tools import tool
from config import EMAIL_USER, EMAIL_PASS

@tool("email")
def email_tool(data: str) -> str:
    """
    Send an email.
    Format: recipient | subject | message
    """
    try:
        to, subject, message = data.split("|")

        msg = MIMEText(message)
        msg["From"] = EMAIL_USER
        msg["To"] = to.strip()
        msg["Subject"] = subject.strip()

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, to, msg.as_string())
        server.quit()

        return "Email sent successfully!"
    except:
        return "Failed to send email."
