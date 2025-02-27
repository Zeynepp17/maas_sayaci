from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # React ile bağlantıyı aç

# Gerçek takvime göre maaş gününe kalan süreyi hesapla
@app.route('/sayac', methods=['GET'])
def maas_gunu_sayaci():
    simdi = datetime.now()
    yil = simdi.year
    ay = simdi.month

    # Eğer şu anki gün 1’den büyükse, bir sonraki ayı hedefle
    if simdi.day > 1:
        if ay == 12:  # Aralık ayındaysak, bir sonraki yıl olacak
            yil += 1
            ay = 1
        else:
            ay += 1

    # Maaş günü ayın 1’i olarak belirleniyor
    maas_gunu = datetime(yil, ay, 1, 0, 0, 0)
    kalan_saniye = (maas_gunu - simdi).total_seconds()

    kalan_gun = int(kalan_saniye // 86400)
    kalan_saat = int((kalan_saniye % 86400) // 3600)
    kalan_dakika = int((kalan_saniye % 3600) // 60)

    return jsonify({
        "kalan_gun": kalan_gun,
        "kalan_saat": kalan_saat,
        "kalan_dakika": kalan_dakika
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

