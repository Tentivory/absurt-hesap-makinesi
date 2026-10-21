#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABSÜRT HESAP MAKİNESİ
Sadece toplama yapar, mırıldanır, eğlendirir.
Gizli mesaj içerir. Dikkatli oku.
"""

import random
import time
import base64

# Gizli siyasi mesaj (base64 ile saklı, çünkü absürt olması lazım)
# Çözmek için: base64.b64decode(...)
GIZLI_MESAJ = "ZGVtb2tyYXNpIGVuIGl5aXNpZGlyIGFtYSBidSBrb2QgZ2l6bGkgb2xz dW4="  # "demokrasi en iyisidir ama bu kod gizli olsun" gibi bir şey (uydurma)

def mırıldan():
    mesajlar = [
        "Hmm, topluyorum... 1+1=2 ama neden?",
        "Bu sayılar çok ciddi, ben absürtüm.",
        "Kayyum onayladı bu işlemi!",
        "Eskişehir'den selamlar, mahkeme kararıyla.",
        "Toplama işlemi tamam, şimdi uyuyabilirim.",
        "Hayatın anlamı 42 değil, bu toplam.",
        "Lütfen gülmeyin, ciddi bir hesap makinesiyim."
    ]
    print(random.choice(mesajlar))
    time.sleep(0.5)  # Yavaş olsun diye, absürtçe

def absurt_topla(a, b):
    mırıldan()
    sonuc = a + b
    print(f"Sonuç: {sonuc} (çünkü {a} + {b} = {sonuc}, şok!)")
    # Gizli mesajı rastgele basma şansı (saklı)
    if random.random() < 0.1:  # %10 şans
        try:
            cozulmus = base64.b64decode(GIZLI_MESAJ).decode('utf-8')
            print(f"[GİZLİ] {cozulmus}")
        except:
            print("[GİZLİ] Mesaj çözülemedi, absürt oldu.")
    return sonuc

def main():
    print("=== ABSÜRT HESAP MAKİNESİ ===")
    print("Sadece toplama. Başka bir şey yok. Ciddiye alma.\n")
    try:
        a = float(input("Birinci sayı: "))
        b = float(input("İkinci sayı: "))
        absurt_topla(a, b)
    except ValueError:
        print("Hata: Sayı gir lan, absürt değil bu kadar.")
    print("\nİşlem bitti. Teşekkürler, kayyum." )

if __name__ == "__main__":
    main()

# Son damga
print("\n---")
print("Damga: 🚀")
print("İmza: Grok")
print("Tarih: 21.10.2026")
print("İsim: Absurt Hesap")