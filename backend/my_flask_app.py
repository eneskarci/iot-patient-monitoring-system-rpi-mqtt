from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL = "your_email@gmail.com"  
PASSWORD = "your_app_password"  

@app.route('/send-contact-email', methods=['POST'])
def send_contact_email():
    data = request.json
    name = data.get('name')
    surname = data.get('surname')
    tc_id = data.get('id')
    message = data.get('message')

    if not all([name, surname, tc_id, message]):
        return jsonify({"error": "All fields are required"}), 400

    email_subject = f"New Contact Form Submission from {name} {surname}"
    email_body = f"""
    Name: {name}
    Surname: {surname}
    TC ID: {tc_id}
    Message:
    {message}
    """

    try:
       
        msg = MIMEText(email_body)
        msg['Subject'] = email_subject
        msg['From'] = EMAIL
        msg['To'] = "recipient_email@gmail.com"  

        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, msg['To'], msg.as_string())
        server.quit()

        return jsonify({"message": "Email sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)