class StatsAlerter():
  def __init__(self, maxThreshold, [emailAlert, ledAlert]):
    self.maxThreshold = maxThreshold
    self.emailAlert = emailAlert
    selft.ledAlert = ledAlert
    

    
class EmailAlert():
  def __init__(self):
    pass()
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
      sendto = "maintainer@gmail.com"
      subject = "Alert: values exceeds"
      sendfrom = "StatsAlerter@gmail.com"
      port = 587  
      smtp_server = "smtp.gmail.com"
      password = "password"
      context = ssl.create_default_context()
      with smtplib.SMTP(smtp_server, port) as server:
          server.ehlo()
          server.starttls(context=context)
          server.ehlo()
          server.login(sender_email, password)
          server.sendmail(sendfrom, sendto, mail_content)
      
      
      
