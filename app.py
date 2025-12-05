from flask import Flask, render_template, request
from hesaplayici import hesaplari_denklestir

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def anasayfa():
    sonuclar = []
    hata = None

    if request.method == 'POST':
        try:
            # Formdan gelen listeleri al
            isimler = request.form.getlist('isim[]')
            harcamalar = request.form.getlist('harcama[]')
            
            # Verileri hesaplayici.py'nin anlayacağı sözlük formatına çevir
            veri_sozlugu = {}
            
            for i in range(len(isimler)):
                isim = isimler[i].strip() # Boşlukları temizle
                tutar_str = harcamalar[i].strip()
                
                # İsim boşsa atla
                if not isim:
                    continue
                    
                # Tutar girilmediyse 0 kabul et
                if not tutar_str:
                    tutar = 0.0
                else:
                    tutar = float(tutar_str)
                
                veri_sozlugu[isim] = tutar
            
            # En az 2 kişi var mı kontrol et
            if len(veri_sozlugu) < 2:
                hata = "Hesaplama yapmak için en az 2 kişi girmelisiniz."
            else:
                # MANTIĞI ÇALIŞTIR VE SONUCU AL
                sonuclar = hesaplari_denklestir(veri_sozlugu)
                
        except ValueError:
            hata = "Lütfen harcama kutularına sadece sayı girin (Örn: 100 veya 100.50)"

    return render_template('index.html', sonuclar=sonuclar, hata=hata)

if __name__ == '__main__':
    app.run(debug=True)