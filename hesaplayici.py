def hesaplari_denklestir(harcamalar):
    # 1. ADIM: Toplam harcamayı ve kişi başı düşen payı bul
    toplam_harcama = sum(harcamalar.values())
    kisi_sayisi = len(harcamalar)
    ortalama_pay = toplam_harcama / kisi_sayisi

    # 2. ADIM: Kimin ne kadar Artıda (+) veya Ekside (-) olduğunu bul (Net Bakiye)
    bakiyeler = {}
    for isim, harcanan in harcamalar.items():
        net_durum = harcanan - ortalama_pay
        bakiyeler[isim] = net_durum

    # 3. ADIM: Alacaklıları ve Borçluları iki ayrı listeye ayır
    alacaklilar = []
    borclular = []

    for isim, bakiye in bakiyeler.items():
        if bakiye > 0:
            alacaklilar.append({"isim": isim, "tutar": bakiye})
        elif bakiye < 0:
            # Borcu pozitif sayı olarak listeye ekliyoruz ki işlem kolay olsun (-75 yerine 75)
            borclular.append({"isim": isim, "tutar": -bakiye})

    # Listeleri tutara göre sıralayalım (Büyükten küçüğe)
    # Bu, en büyük borcun en büyük alacağa gitmesini sağlar (Senin istediğin mantık)
    alacaklilar.sort(key=lambda x: x["tutar"], reverse=True)
    borclular.sort(key=lambda x: x["tutar"], reverse=True)

    # 4. ADIM: Eşleştirme ve Transfer Listesi Oluşturma
    transferler = []

    # Borçlu ve Alacaklı listesi bitene kadar döngü kuruyoruz
    i_borclu = 0
    i_alacakli = 0

    while i_borclu < len(borclular) and i_alacakli < len(alacaklilar):
        borclu = borclular[i_borclu]
        alacakli = alacaklilar[i_alacakli]

        odenecek_tutar = min(borclu["tutar"], alacakli["tutar"])

        # Transferi kaydet
        transferler.append(f"{borclu['isim']} -> {alacakli['isim']} kişisine {odenecek_tutar:.2f} TL ödemeli.")

        # Bakiyeleri güncelle
        borclu["tutar"] -= odenecek_tutar
        alacakli["tutar"] -= odenecek_tutar

        # Kimin hesabı kapandıysa bir sonraki kişiye geç
        if borclu["tutar"] < 0.01: # Kuruş hatası olmasın diye 0.01
            i_borclu += 1
        
        if alacakli["tutar"] < 0.01:
            i_alacakli += 1

    return transferler

# ... (Yukarıdaki fonksiyon kodları aynen kalsın) ...

# --- TEST ALANI ---
if __name__ == "__main__":
    # DİKKAT: Buradan sonraki her şey bir TAB içeride olmalı
    print("--- HESAPLAŞMA SONUCU ---")

    # Örnek verileri de içeri alıyoruz
    ornek_grup = {
        "Vedat": 400,
        "Fatih": 200,
        "Şahin": 100,
        "Yusuf": 0
    }

    # Fonksiyonu çağırıp sonucu alıyoruz
    sonuclar = hesaplari_denklestir(ornek_grup)

    # Yazdırma işlemi de if bloğunun içinde (girintili) olmalı
    for islem in sonuclar:
        print(islem)