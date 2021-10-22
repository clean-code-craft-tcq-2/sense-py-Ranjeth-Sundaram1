import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



class StatsAlerter():
  def __init__(self, maxThreshold, objects):
    self.maxThreshold = maxThreshold
    self.emailAlert = objects[0]
    self.ledAlert = objects[1]
    
  def checkAndAlert(self,values):
    for val in values:
      if val > self.maxThreshold:
        self.emailAlert.send_mail()
        self.ledAlert.make_led_on()
    

      
      
      
