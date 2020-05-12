import pyzmail
import imapclient

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('brandon.christopher1@gmail.com', 'Soraya*1986')

conn.select_folder('INBOX', readonly=True)

# this error'd out. Video 47 and a nice boomark link as well.
UIDs = conn.search(['SINCE 01-Jan-2020'])
