from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL = "raspmail18@gmail.com"  
PASSWORD = "lfsm gfxo qmza ivrw"      

@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        
        data = request.json
        name = data.get('name')
        surname = data.get('surname')
        patient_id = data.get('id')
        temperature = data.get('temperature')
        spo2 = data.get('spo2')
        pulse = data.get('pulse')

        
        subject = f"Patient Health Data: {name} {surname}"
        body = f"""
        Patient Name: {name} {surname}
        Patient ID: {patient_id}
        
        Temperature: {temperature}
        SpO2: {spo2}
        Pulse: {pulse}
        """

       
        msg = MIMEMultipart()
        msg['From'] = EMAIL
        msg['To'] = "eneskarci243@gmail.com" 
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

      
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
