from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL = "raspmail18@gmail.com"  
PASSWORD = "ypwt novt bcgt rfhq" 


@app.route('/')
def home():
    return "Flask Backend is Running", 200

@app.route('/favicon.ico')
def favicon():
    return '', 204



@app.route('/send-contact-email', methods=['POST'])
def send_contact_email():
    try:
        print("POST request received")
        data = request.json
        name = data.get('name')
        surname = data.get('surname')
        tc_id = data.get('id')
        message = data.get('message')
        oksijen = data.get('spo2')
        pulse = data.get('pulse')
        temp = data.get('temperature')

        if not all([name, surname, tc_id, message]):
            return jsonify({"error": "All fields are required"}), 400

        email_subject = f"Ayakta Giren {name} Adlı Hasta Triyaj Bilgileri "
        email_body = f"""
        Hasta İsmi Soyismi      : {name} 
        Hasta Yaşı              : {surname}
        Hasta TC                : {tc_id}
        Hasta Şikayeti          :{message}
        Hasta Vücut Sıcaklığı   :{temp}
        Hasta Nabzı(bpm)        :{pulse}
        Hasta Satürasyonu       :{oksijen}
        """

       
        msg = MIMEText(email_body)
        msg['Subject'] = email_subject
        msg['From'] = EMAIL
        msg['To'] = "eneskarci243@gmail.com"  

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, msg['To'], msg.as_string())
        server.quit()

        return jsonify({"message": "Email sent successfully"}), 200
    except smtplib.SMTPAuthenticationError:
        return jsonify({"error": "Authentication failed. Check email and password."}), 401
    except smtplib.SMTPException as smtp_error:
        return jsonify({"error": f"SMTP error: {smtp_error}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {e}"}), 500
    except smtplib.SMTPException as smtp_error:
        print(f"SMTP error: {smtp_error}")
        return jsonify({"error": f"SMTP error: {smtp_error}"}), 500



if __name__ == '__main__':
    app.run(debug=True)
