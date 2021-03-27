import smtplib, ssl
from email.mime.text import MIMEText
import psycopg2

receivers = 'tiphaine.minguet@gmail.com'

def sendmail(receivers):

    host="23.96.93.237"
    dbname="postgres"
    user="postgres"
    password="123"

    conn_string = "host={0} dbname={1} user={2} password={3}".format(host, dbname, user, password)
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM carpet LIMIT 5")
    output = cursor.fetchall()
    conn.commit()

    sender = "tminguet.simplon@gmail.com"
    body_of_email = "".join(str(output))

    msg = MIMEText(body_of_email, "html")
    msg["Subject"] = "Scrapping Text"
    msg["From"] = sender
    msg["To"] = receivers

    s = smtplib.SMTP_SSL(host = "smtp.gmail.com", port = 465)
    s.login(user="tminguet.simplon@gmail.com", password="simplon2021")
    s.sendmail(sender, receivers, msg.as_string())
    s.quit()

sendmail(receivers)