# test_api.py
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "http://127.0.0.1:8000/predict"
API_KEY = os.getenv("API_KEY", "dev-sentiment-secret-key-2026")

def test_sentiment_api():
    print("=== Baslangic: API Testleri ===")
    
    # 1. Başarılı İstek (Pozitif Yorum)
    positive_text = "Bu ürünü çok sevdim, kalitesi gerçekten harika!"
    print(f"\n[Test 1] Pozitif metin analizi gönderiliyor: '{positive_text}'")
    headers = {"x-api-key": API_KEY}
    response = requests.post(API_URL, json={"text": positive_text}, headers=headers)
    
    assert response.status_code == 200, f"Başarısız durum kodu: {response.status_code}"
    result = response.json()
    print("Sonuç:", result)
    assert result["positive"] > result["negative"], "Pozitif skor negatif skordan büyük olmalı!"
    print("[GECTI] [Test 1] Basarili: Pozitif yorum dogru siniflandirildi.")

    # 2. Başarılı İstek (Negatif Yorum)
    negative_text = "Hizmet çok kötüydü, hiç memnun kalmadım ve iade etmek istiyorum."
    print(f"\n[Test 2] Negatif metin analizi gönderiliyor: '{negative_text}'")
    response = requests.post(API_URL, json={"text": negative_text}, headers=headers)
    
    assert response.status_code == 200, f"Başarısız durum kodu: {response.status_code}"
    result = response.json()
    print("Sonuç:", result)
    assert result["negative"] > result["positive"], "Negatif skor pozitif skordan büyük olmalı!"
    print("[GECTI] [Test 2] Basarili: Negatif yorum dogru siniflandirildi.")

    # 3. Yetkilendirme Hatası (Yanlış API Key)
    print("\n[Test 3] Yanlış API Key ile istek gönderiliyor...")
    bad_headers = {"x-api-key": "wrong-secret-key"}
    response = requests.post(API_URL, json={"text": positive_text}, headers=bad_headers)
    
    assert response.status_code == 401, f"Beklenen 401 ama alınan: {response.status_code}"
    print("Sonuç (Beklenen hata):", response.json())
    print("[GECTI] [Test 3] Basarili: Yetkilendirme hatasi dogru sekilde engellendi.")

    # 4. Boş Metin Hatası
    print("\n[Test 4] Boş metin ile istek gönderiliyor...")
    response = requests.post(API_URL, json={"text": "   "}, headers=headers)
    
    assert response.status_code == 400, f"Beklenen 400 ama alınan: {response.status_code}"
    print("Sonuç (Beklenen hata):", response.json())
    print("[GECTI] [Test 4] Basarili: Bos metin gonderimi engellendi.")

    print("\nTum testler basariyla tamamlandi! API sorunsuz calisiyor.")

if __name__ == "__main__":
    try:
        test_sentiment_api()
    except requests.exceptions.ConnectionError:
        print("\n[HATA]: Sunucuya baglanılamadı. Lutfen FastAPI backend sunucusunun (port 8000) calistigından emin olun.")
    except AssertionError as e:
        print(f"\n[BASARISIZ] TEST BASARISIZ: {e}")
