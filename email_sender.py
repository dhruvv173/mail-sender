import smtplib
from email.message import EmailMessage
import csv
import os
DRY_RUN = False  # Set to False to send real emails

EMAIL_ADDRESS = os.environ['EMAIL_ADDRESS']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']
RESUME_LINK = "https://drive.google.com/file/d/1a2b3cXYZ/view?usp=sharing"

def send_email(to_email, recruiter_name, company_name):

    subject = f"Exploring SDE-1 Opportunities at {company_name}"

    body = f"""Hi {recruiter_name},

I hope you're doing well! My name is Dhruv Parmar, and I'm currently a Software Engineer at Jio, specializing in backend development.

I have 19 months of experience working on backend systems, where I've led API migrations, improved performance, and ensured maintainability without compromising functionality.

I'm interested in applying for SDE-1 roles at {company_name} and would love to connect to explore potential opportunities.

I have attached my resume to this email. Alternatively, you can also view it here: {RESUME_LINK}  
Please let me know if you'd be open to a quick chat.

Looking forward to your response!

Best regards,  
Dhruv Parmar  
+91-8169409129  
https://linkedin.com/in/dhruvv173/
"""

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    msg.set_content(body)
    if DRY_RUN:
        print(f"[DRY RUN] Would send email to {recruiter_name} ({to_email}) at {company_name}")
    else:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print(f"✅ Sent email to {recruiter_name} at {company_name}")

def main():
    with open('recruiters.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            send_email(row['Email'], row['FirstName'], row['Company'])

if __name__ == "__main__":
    main()
