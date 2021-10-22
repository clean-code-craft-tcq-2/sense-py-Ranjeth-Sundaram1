import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



class StatsAlerter():
  def __init__(self, maxThreshold, objects):
    self.maxThreshold = maxThreshold
    self.emailAlert = objects[0]
    selft.ledAlert = objects[1]
    

    
class EmailAlert():
  def __init__(self):
    self.sendto = "ranjethsudhakar@gmail.com" 
    self.sendfrom = "ranjethsundaram@gmail.com"
    self.password = str(input("Enter the password"))
    
  def construct_message():
    message = '''
          <html>
            <body>
                <p>Hi,<br/><br/>
                   The sensor values exceeds the maximum threshold value. Please take necessary actions to avoid problems.
                <br/>
                Thank you.<br/>
                <p>******************* This is an auto generated email. Please do not reply to this mail *******************</p>
                <br/>
            <p>Regards,<br/>statsAlerterTeam</p>
            </body>
        </html>
        '''
    return message
  
    def send_mail():
      mail_content = construct_message()
      subject = "Alert: values exceeds"
      port = 587  
      smtp_server = "smtp.gmail.com"
      context = ssl.create_default_context()
      with smtplib.SMTP(smtp_server, port) as server:
          server.ehlo()
          server.starttls(context=context)
          server.ehlo()
          server.login(self.sendfrom, self.password)
          server.sendmail(self.sendfrom, self.sendto, mail_content)
      
      
      
