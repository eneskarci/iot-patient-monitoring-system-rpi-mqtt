# IoT Temelli Hasta Takip Sistemi (Raspberry Pi 4 + MQTT)

⚠ Akademik Uyarı

Bu proje Mühendislik Tasarımı 3 dersi kapsamında tarafımdan geliştirilmiştir.

İzinsiz kopyalanması veya akademik amaçla teslim edilmesi yasaktır.
Lütfen kendi emeğinizle çalışın. Kullanmak isterseniz önce benimle iletişime geçiniz.


============================================================
🇹🇷 TÜRKÇE
============================================================

## Proje Özeti

Bu proje Raspberry Pi 4 üzerinde çalışan IoT tabanlı bir hasta takip sistemidir.

Sistem sağlık verilerini (örneğin nabız, SpO2, sıcaklık vb.)
MQTT protokolü üzerinden alır ve yerel web arayüzünde gerçek zamanlı olarak görüntüler.

Belirlenen eşik değerlerin aşılması durumunda sistem,
Flask backend üzerinden e-posta bildirimi gönderir.


## Kullanılan Teknolojiler

- Raspberry Pi 4
- MQTT (Publish / Subscribe mimarisi)
- Local Web Dashboard (HTML / JavaScript)
- Flask (Python backend)
- SMTP ile e-posta bildirimi


## Sistem Mimarisi

1. Sensör verileri MQTT broker üzerinden publish edilir.
2. Web arayüz bu verileri subscribe ederek canlı gösterim sağlar.
3. Kritik eşiklerde backend tetiklenir.
4. Backend üzerinden ilgili kişiye e-posta gönderilir.


## Proje Yapısı

- frontend/  → Web dashboard
- backend/   → Flask uygulaması ve mail servisleri
- Images/    → Proje görselleri


============================================================
🇬🇧 ENGLISH
============================================================

## Project Overview

This project is an IoT-based Patient Monitoring System running on Raspberry Pi 4.

Health telemetry data (e.g., heart rate, SpO2, temperature) is received via MQTT
and displayed in real time on a local web dashboard.

When critical thresholds are exceeded, a Flask backend service
triggers an email notification.


## Technologies Used

- Raspberry Pi 4
- MQTT (Publish/Subscribe architecture)
- Local Web Dashboard (HTML/JavaScript)
- Flask (Python backend)
- SMTP email notification system


## System Architecture

1. Sensor data is published to an MQTT broker.
2. The web dashboard subscribes and displays live data.
3. Threshold violations trigger backend logic.
4. Email alerts are sent to designated recipients.


