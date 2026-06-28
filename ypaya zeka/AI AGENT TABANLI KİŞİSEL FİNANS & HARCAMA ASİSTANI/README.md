# 💰 AI Agent Tabanlı Kişisel Finans & Harcama Asistanı

Bu proje, kullanıcının serbest metin olarak girdiği harcama verilerini (banka SMS'leri, harcama notları, faturalar vb.) alan, bunları akıllı bir şekilde analiz eden, sınıflandıran, bütçe uyumluluğunu kontrol eden ve kişiye özel tasarruf önerileri üreten **v1.0 MVP** düzeyinde bir yapay zeka finans asistanıdır.

---

## 🎯 Ne Yapar?

- **Harcama Kalemi Ayıklama:** Girdi metinlerindeki tüm harcama isimlerini ve tutarlarını kuruşu kuruşuna ayıklar.
- **Akıllı Kategorizasyon:** Harcamaları *kira*, *yemek*, *ulaşım*, *eğlence*, *abonelik* ve *diğer* kategorilerine sınıflandırır.
- **Bütçe Analizi (50/30/20):** Aylık gelirinizi temel alarak bütçenizi analiz eder ve finansal kurala uygunluğunu değerlendirir.
- **Finansal Sağlık Durumu:** Harcama alışkanlıklarınıza göre 0-100 arası interaktif bir sağlık skoru hesaplar.
- **Tasarruf Önerileri:** Harcama örüntülerinizdeki riskli/gereksiz alanları tespit edip net, maddeli tasarruf tavsiyeleri sunar.
- **Çift LLM Desteği (Fallback):** Birincil olarak Google Gemini Pro/Flash kullanır; Gemini servislerinde bir kesinti oluşursa otomatik olarak Groq (Llama 3) modeline geçiş yapar.

---

## 🏗️ Mimari ve Akış Şeması

Uygulama, **FastAPI backend** ve **Streamlit frontend** olmak üzere iki katmandan oluşan bir **Agentic Pipeline (Çok Adımlı LLM Akışı)** mimarisine sahiptir.

```
+--------------------------------------------------------+
|                   Streamlit Frontend                   |
|  (Harcama Girişi, Plotly Grafikleri, Bütçe Karşılaştırma)|
+---------------------------+----------------------------+
                            |
                     HTTP   |   Direct Import
                    Requests|   (Cloud Deploy)
                            v
+---------------------------+----------------------------+
|                   FastAPI Backend API                  |
|          (Endpoint /analyze & /health)                 |
+---------------------------+----------------------------+
                            |
                            v
+---------------------------+----------------------------+
|                  Agent Controller (agent.py)           |
+---------------------------+----------------------------+
                            |
         +------------------+------------------+
         | 1. Tercih:                          | 2. Fallback:
         v (Gemini API)                        v (Groq API)
+--------+---------------+            +--------+---------------+
|   Google Gemini Pro    |            |     Groq Llama 3       |
|      (1.5 Flash)       |            |     (8b-8192)          |
+------------------------+            +------------------------+
```

---

## 📁 Dosya Yapısı

```
AI AGENT TABANLI KİŞİSEL FİNANS & HARCAMA ASİSTANI/
│
├── backend/
│   ├── __init__.py
│   ├── agent.py          # Agent Akış Kontrolcüsü (Gemini/Groq Fallback)
│   ├── prompts.py        # Tüm LLM Prompt Şablonları
│   ├── app.py            # FastAPI API Sunucusu
│   └── test_agent.py     # Yerel Test Scripti
│
├── frontend/
│   ├── __init__.py
│   └── streamlit_app.py   # Streamlit Arayüzü (Plotly & HTML/CSS)
│
├── .env                  # Yerel API Key Dosyası (Git'e eklenmez)
├── .env.example          # API Key Şablonu
├── .gitignore            # Git Yoksayma Kuralları
├── requirements.txt      # Gerekli Kütüphaneler
└── README.md             # Proje Kılavuzu
```

---

## ⚙️ Kurulum ve Çalıştırma

### Gereksinimler
- Python 3.11 veya üzeri kurulu olmalıdır.
- [Google AI Studio](https://aistudio.google.com)'dan alınmış ücretsiz **Gemini API Key**.
- [Groq Console](https://console.groq.com)'dan alınmış ücretsiz **Groq API Key** (Yedek model için).

### Adım Adım Kurulum

1. **Projeyi Klonlayın veya İlgili Klasöre Gidin:**
   ```bash
   cd "z:\NEJDET TUT\python\Python 127\necmettin\ypaya zeka\AI AGENT TABANLI KİŞİSEL FİNANS & HARCAMA ASİSTANI"
   ```

2. **Sanal Ortam (Virtual Environment) Oluşturun ve Aktifleştirin:**
   ```bash
   python -m venv .venv
   # Windows için aktifleştirme:
   .venv\Scripts\activate
   # macOS/Linux için aktifleştirme:
   source .venv/bin/activate
   ```

3. **Gerekli Bağımlılıkları Yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

4. **API Anahtarlarını Yapılandırın:**
   Kök dizindeki `.env` dosyasını açın ve API anahtarlarınızı girin:
   ```env
   GEMINI_API_KEY=AIzaSy... (Gemini anahtarınız)
   GROQ_API_KEY=gsk_... (Groq anahtarınız)
   BACKEND_URL=http://localhost:8000
   ```

---

## 🚀 Projeyi Çalıştırma

Proje iki farklı şekilde çalıştırılabilir:

### Seçenek A: API ve Streamlit Birlikte Çalıştırma (Önerilen Yerel Geliştirme Modu)

1. **FastAPI Backend Servisini Başlatın:**
   ```bash
   python backend/app.py
   ```
   API sunucusu varsayılan olarak `http://localhost:8000` adresinde çalışacaktır. API belgelerine `http://localhost:8000/docs` adresinden erişebilirsiniz.

2. **Streamlit Frontend Uygulamasını Başlatın:**
   Yeni bir terminal açıp sanal ortamı aktifleştirdikten sonra çalıştırın:
   ```bash
   streamlit run frontend/streamlit_app.py
   ```
   Streamlit arayüzü tarayıcınızda otomatik olarak açılacaktır (genelde `http://localhost:8501`). Soldaki çalışma modunu **"API Sunucusu Üzerinden"** olarak seçin.

### Seçenek B: Bağımsız (Standalone) Streamlit Modu (FastAPI Olmadan)

Sadece Streamlit uygulamasını çalıştırıp, arayüzün sol panelindeki ayar kısmından **"Doğrudan Agent (Bulut & Bağımsız Mod)"** seçeneğini seçin. Bu sayede FastAPI sunucusuna gerek kalmadan, doğrudan API anahtarlarıyla sorgu gerçekleştirebilirsiniz.

---

## 🚀 Streamlit Cloud Deployment (Buluta Dağıtım)

Bu projeyi **Streamlit Cloud** (`share.streamlit.io`) üzerinde FastAPI backend sunucusu kurmadan doğrudan deploy edebilirsiniz.

1. Projeyi kendi GitHub hesabınızda bir repository'e push edin (Hassas `.env` dosyasını dahil etmediğinizden emin olun).
2. [Streamlit Share](https://share.streamlit.io) adresine gidin ve GitHub hesabınızla giriş yapın.
3. **"New App"** butonuna tıklayarak projenizin reposunu, branch'ini ve ana dosya yolunu (`frontend/streamlit_app.py`) seçin.
4. **Advanced Settings (Gelişmiş Ayarlar)** -> **Secrets** kısmına giderek API anahtarlarınızı şu formatta ekleyin:
   ```toml
   GEMINI_API_KEY = "SİZİN_GEMINI_KEYİNİZ"
   GROQ_API_KEY = "SİZİN_GROQ_KEYİNİZ"
   ```
5. **"Deploy"** butonuna basın. Uygulamanız bulutta yayına girecek ve FastAPI sunucusu olmadan doğrudan çalışacaktır!

---

## 🔄 Agent Pipeline Akış Detayları

1. **Extraction (Ayıklama):** Kullanıcının girdiği metindeki gürültüleri filtreleyerek sadece `Kalem: X | Tutar: Y` şeklinde veriler üretir.
2. **Categorization (Sınıflandırma):** Ayıklanan kalemi analiz ederek 6 finansal kategoriye eşleştirir.
3. **Analysis (Analiz):** En yüksek harcamaları, potansiyel riskleri ve harcama alışkanlıklarını yorumlar.
4. **Suggestions (Tasarruf Önerileri):** Analiz sonuçlarına dayanarak 3-7 adet yapıcı ve uygulanabilir tavsiye listeler.
5. **Budget Compare (Bütçe Karşılaştırma):** Gelir verisiyle birlikte 50/30/20 kuralına göre bütçe dağılımını hesaplar.
6. **Chart Parsing (Grafikleme):** Kategorize edilmiş tutarları görselleştirmek üzere JSON formatına indirger ve Plotly grafiklerine besler.

---

## 📝 Örnek Kullanım senaryoları

### Örnek Girdi:
> *"Bu ay ev kirasına 15000 TL verdim. Market alışverişim 3500 TL tuttu. Haftasonu sinema ve yemeğe arkadaşımla 1200 TL harcadım. Netflix aboneliği 139 TL çekildi. Otobüs kartına da 400 TL attım."*

### Beklenen Çıktı Görselleri:
- **📊 Özet Metrikleri:** Toplam Harcama: `20,239.00 TL`, Kalan: `4,761.00 TL` (Gelir 25.000 TL girildiyse), Sağlık Skoru: `75/100`.
- **📈 Grafikler:** Kategori dağılımlarını gösteren Pasta ve Sütun grafikleri ile 50/30/20 kuralının hedef vs. gerçekleşen durumunu gösteren karşılaştırma grafikleri.
- **💡 AI Önerisi:** *"Abonelikleriniz veya eğlence harcamalarınız gelirinizin %X kadarını oluşturuyor, tasarruf etmek için dışarıda yeme-içme giderlerinizi sınırlandırabilirsiniz..."*

---

## 🛠️ Teknolojiler

- **Backend:** FastAPI (Python)
- **Frontend:** Streamlit (Python)
- **Birincil LLM:** Google Gemini 1.5 Flash
- **Yedek LLM:** Groq Llama 3 8B
- **Veri Görselleştirme:** Plotly Express & Plotly Graph Objects
- **Yapılandırma:** Pydantic v2, Python-Dotenv, HTTPX

---

*Geliştirici: Necmeddin Tekik | Versiyon: 1.0 MVP | 2026*
