# -*- coding: utf-8 -*-
"""
AI Kişisel Finans Asistanı Agent Test Betiği
Bu script, FinanceAgent pipeline akışının ve Gemini/Groq LLM bağlantılarının
yerel makinede doğru çalışıp çalışmadığını test etmek için kullanılır.
"""

import sys
from pathlib import Path

# UTF-8 Kodlamasını Terminal İçin Zorunlu Yap (Windows Uyumlu)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

# backend klasörünün üst dizinini Python yoluna ekle (böylece 'import backend' çalışabilir)
current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
if str(parent_dir) not in sys.path:
    sys.path.append(str(parent_dir))

from backend.agent import FinanceAgent

def test_agent_pipeline():
    print("=" * 60)
    print("🤖 AI Finans Agent Yerel Test Başlatılıyor...")
    print("=" * 60)

    # Agent'ı başlat
    try:
        agent = FinanceAgent()
    except Exception as e:
        print(f"❌ Agent başlatılırken hata oluştu: {str(e)}")
        return

    # Örnek test verisi
    test_input = (
        "Bu ay kira için ev sahibine 8500 TL gönderdim. "
        "Ayrıca elektrik faturası 350 TL, su faturası 150 TL geldi. "
        "Yemek için marketten 2300 TL harcadım ve haftasonu restoranda 600 TL ödedim. "
        "Netflix aboneliğim 139 TL, Spotify ise 59 TL çekti. "
        "Otobüs kartıma da 400 TL yükleme yaptım."
    )
    test_income = 25000.0

    print(f"\n📝 Test Giriş Metni:\n{test_input}")
    print(f"💼 Test Gelir: {test_income} TL")
    print("-" * 60)

    # Analizi çalıştır
    result = agent.analyze(test_input, income=test_income)

    # Sonuçları incele
    if result.get("status") == "success":
        print("\n✅ TEST BAŞARILI! Agent analizi başarıyla tamamladı.")
        print("\n🔍 1. AYIKLANAN HARCAMALAR:")
        print(result["extracted_expenses"])
        
        print("\n🔍 2. KATEGORİZE EDİLMİŞ HARCAMALAR:")
        print(result["categorized_expenses"])
        
        print("\n🔍 3. HARCAMA ANALİZİ:")
        print(result["analysis"])
        
        print("\n🔍 4. TASARRUF ÖNERİLERİ:")
        print(result["suggestions"])
        
        print("\n🔍 5. BÜTÇE ANALİZİ (50/30/20):")
        print(result["budget_analysis"])
        
        print("\n🔍 6. GRAFİK JSON VERİSİ:")
        print(result["chart_data"])
    else:
        print("\n❌ TEST BAŞARISIZ!")
        print(f"Hata Mesajı: {result.get('message')}")
        
    print("=" * 60)

if __name__ == "__main__":
    test_agent_pipeline()
