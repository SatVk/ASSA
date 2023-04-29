# Import necessary libraries
#!/usr/bin/env python

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random
import requests
import cgi

# Generate a 6-digit OTP
otp = str(random.randint(100000, 999999))

# Separate the first 3 digits and the last 3 digits of the OTP
otp_mobile = otp[:3]
otp_email = otp[3:]

# Send the first 3 digits of the OTP to a mobile number via SMS message using TextMagic API
api_key = 'your_textmagic_api_key'
phone_number = '8073373016'

response = requests.post('https://rest.textmagic.com/api/v2/messages',
    auth=('api', api_key),
    data={
        'text': 'Your OTP is ' + otp_mobile,
        'phones': phone_number
    }
)

# Send the last 3 digits of the OTP to an email address
sender_email = 'satwikkul2002@gmail.com'
sender_password = 'lzakqyobchxkvlyd'
recipient_email = 'solomonbhaskar712@gmail.com'

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = 'OTP for validation'

msg.attach(MIMEText('Your OTP is ' + otp_email, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, sender_password)
text = msg.as_string()
server.sendmail(sender_email, recipient_email, text)
server.quit()

form=cgi.FieldStorage()
otp = form.getvalue('otp')

# Print the complete OTP for verification
print('OTP sent to respective mobile number for Successful registration:' + otp_mobile)
print('OTP sent to '+recipient_email+' for Successful registration     :' + otp_email)
