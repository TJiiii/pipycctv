import time, datetime
from subprocess import call
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from email.header import Header
import os

def sendMail():
	sender = "test@test.com"
	receivers = ["test@test.com"]
	subject = "test for smtp mail!"
	msg = MIMEMultipart()

	msg['From'] = sender
	msg['To'] = ", ".join(receivers)
	msg['Subject'] = Header(subject, 'utf8')
	body = """\
	this is test line.
	line 2
	line 3
	"""
	msg.attach(MIMEText(body, 'plain'))

	try:
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.starttls() #secure connection
		server.login(sender, "test")

		server.sendmail(sender, receivers, msg.as_string())
		print("Successfully sent email.")
		server.quit()
	except smtplib.SMTPException:
		print ("Error: Unable to send email.")


#	attach = "/home/pi/Videos/mp4/"+filename+".mp4"
#	print("file:" + attach)

#	if (os.path.exists(attach)):
#		msg.attach(MIMEText(body, 'html', _charset="utf8"))

		#attachFilename = filename+".png"
#		attachFilename = filename+".mp4"
#		attachment = open(attach, "rb")
#		part = MIMEBase('application', 'octet-stream', _charset="utf8")
#		part.set_payload((attachment).read())
#		encoders.encode_base64(part)
#		part.add_header('Content-Disposition', "attachment; filename= %s" % attachFilename)
#		msg.attach(part)

#		try:
#			server = smtplib.SMTP("smtp.gmail.com", 587)
#			server.starttls() #secure connection
#			server.login(sender, "ghost1004")

#			server.sendmail(sender, receivers, msg.as_string())
#			print("Successfully sent email.")
#			server.quit()
#		except smtplib.SMTPException:
#			print ("Error: Unable to send email.")

#	else:
#		print ("no file.")

sendMail()
