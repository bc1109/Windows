import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
# type(conn)
conn.ehlo()
conn.starttls()
conn.login('brandon.christopher1@gmail.com', 'Soraya*1986')
conn.sendmail('brandon.christopher1@gmail.com', 'brandon.christopher1@gmail.com',
              'Subject: I learned something new today... \n\n Kate, \n I sent this email via a script. \n\n I love you and hope your day is going well! \n\n Love, \n\n Brandon')
conn.quit()
