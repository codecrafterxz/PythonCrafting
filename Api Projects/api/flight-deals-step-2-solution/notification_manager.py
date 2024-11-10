import smtplib

USERNAME = "zhackerx3@gmail.com"
PASSWORD = "fzsiksvtnsfdajjm"

class NotificationManager:

   def make_notification(self,msessage):
       connection = smtplib.SMTP("smtp.gmail.com",587)
       connection.ehlo()
       connection.starttls()
       connection.ehlo()
       connection.login(USERNAME,PASSWORD)
       connection.sendmail(from_addr = USERNAME,to_addrs= "pv8920034911@gmailcom" , msg= msessage)
       print("its finally worked good job and keep going|")
 



   
  