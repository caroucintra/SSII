import smtplib
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


def send_email(recipients):
    subject = "Resumen mensual de los resultados diarios del HIDS"
    body = "Señoras y señores,\n\nadjunto a este correo electrónico encontrarán el resumen mensual de los resultados diarios del HIDS.\n\n"
    sender = "testpurpose364@gmail.com"
    password = "pzyn gppw msrb wtnm"
    with open("log.log", "rb") as attachment:
    # Add the attachment to the message
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= 'log.log'",
)
    
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    html_part = MIMEText(body)
    msg.attach(html_part)
    msg.attach(part)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())