import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time
# import file
sub=open('subject.txt',"r").read()
base=open('Body_base.txt',"r").read()

# Load the CSV file
csv_file = '500+hrs.csv'
data = pd.read_csv(csv_file)
data.fillna(0)
# Email credentials
your_email = 'vwadhwa02@gmail.com'
your_password = 'njsw xryy cssc cfon'  # Use the App Password generated from Gmail

# Email content
subject=sub
body_base=base

resume_filename = 'VaibhavWadhwa_CV.pdf'

# Setup the server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(your_email, your_password)

# Iterate over the rows in the CSV file and send emails
for index, row in data.iterrows():
    if type(row['Email'])!="nan":
        recipient_email = row['Email']
    elif type(row['Work email'])!="nan":
        recipient_email = row['Work email']
    elif type(row['Direct email'])!="nan":
        recipient_email = row['Direct email']
    elif type(row['Email'])!="nan":
        recipient_email = row['Email']
    else:
        continue
            # Create a message

    #recipient_email = row['Work email']
    #recipient_name=row['First name']+" "+row["Last name"]
    recipient_name=row["Name"]
    recipient_company=row['Company']

    body=body_base.format(re_name=recipient_name,Company=recipient_company)
    
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = your_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    #body = body.format(recruiter_name=recruiter_name)
    msg.attach(MIMEText(body, 'plain'))
    
    # Attach the resume
    attachment = open(resume_filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename= {resume_filename}')
    msg.attach(part)
    print(type(your_email))
    print((recipient_email))
    print(type(subject))
    print(type(body))
    # Send the email
    server.sendmail(your_email, [recipient_email]+["wadhwa.vaibhav11@gmail.com"],msg.as_string())
    print(f'Email sent to {recipient_email}')
    
    # except Exception as e:
    # print(f"Failed to send email: {e}")
    # # Optional: wait for some time before sending the next email to avoid being flagged as spam
    time.sleep(0.5)
    
    # except:
    #     print("Error in sending email")
    #     pass

    
    # except Exception as e:
    # print(f"Failed to send email: {e}")
    # # Optional: wait for some time before sending the next email to avoid being flagged as spam
    time.sleep(1)
# Quit the server 
server.quit()
