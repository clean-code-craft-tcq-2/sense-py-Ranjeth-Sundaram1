import unittest
import statistics
import math
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class LEDAlert():
  def __init__(self):
    self.AlertValue = 1
  def make_led_on():
    print('led is turned ON')
    
class EmailAlert():
  def __init__(self):
    self.sendto = ["ranjethsudhakar@gmail.com"]
    self.sendfrom = "ranjethsundaram@gmail.com"
    self.password = 'in.bosch.com11'
     
  def send_mail(self):
    msg = MIMEMultipart()
    msg['subject'] = "Alert: values exceeds"
    mail_content = "The sensor values exceeds the maximum threshold value. Please take necessary actions to avoid problems."
    msg.attach(MIMEText(mail_content,'plain'))
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login(self.sendfrom, self.password)
    server.sendmail(self.sendfrom, self.sendto, msg.as_string())
    server.close()
        
class StatsAlerter():
  def __init__(self, maxThreshold, objects):
    self.maxThreshold = maxThreshold
    self.emailAlert = objects[0]
    self.ledAlert = objects[1]
    
  def checkAndAlert(self,values):
    for val in values:
      if val > self.maxThreshold:
        self.emailAlert.send_mail()
        self.emailSent = True
        self.ledAlert.make_led_on()
        self.ledGlows = True
          
class StatsTest(unittest.TestCase):
  def test_report_min_max_avg(self):
    computedStats = statistics.calculateStats([1.5, 8.9, 3.2, 4.5])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 4.525, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 8.9, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)

  def test_avg_is_nan_for_empty_input(self):
    computedStats = statistics.calculateStats([])
    # All fields of computedStats (average, max, min) must be
    # nan (not-a-number), as defined in the math package
    # Design the assert here.
    self.assertTrue((math.isnan(computedStats["avg"]) and math.isnan(computedStats["max"]) and math.isnan(computedStats["min"])), "The given list is not empty")
    # Use nan and isnan in https://docs.python.org/3/library/math.html

  def test_raise_alerts_when_max_above_threshold(self):
    emailAlert = EmailAlert()
    ledAlert = LEDAlert()
    maxThreshold = 10.5
    statsAlerter = StatsAlerter(maxThreshold, [emailAlert, ledAlert])
    statsAlerter.checkAndAlert([22.6, 12.5, 3.7])
    self.assertTrue(emailAlert.emailSent)
    self.assertTrue(ledAlert.ledGlows)

if __name__ == "__main__":
  unittest.main()
