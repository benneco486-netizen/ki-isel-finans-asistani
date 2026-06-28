#streamlit_app.py
import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Sayfa yapılandırması
st.set_page_config(
    page_title="Yapay Zeka Destekli Müşteri Yorum Analiz Sistemi",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# .env yükle
load_dotenv()

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/predict")
API_KEY = os.getenv("API_KEY")

# Premium CSS Tasarımı
st.markdown("""
<style>
    /* Google Fonts Entegrasyonu */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    /* Ana Kart Tasarımları */
    .main-card {
        background: rgba(30, 41, 59, 0.45);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
        backdrop-filter: blur(8px);
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }
    
    .main-card:hover {
        border-color: rgba(99, 102, 241, 0.4);
        box-shadow: 0 8px 32px 0 rgba(99, 102, 241, 0.1);
    }
    
    /* Gradyan Başlık */
    .glow-text {
        background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 50%, #f472b6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.5rem;
        margin-bottom: 10px;
        text-shadow: 0 0 30px rgba(167, 139, 250, 0.2);
    }
    
    /* Duygu Durum Kutuları */
    .verdict-box {
        border-radius: 12px;
        padding: 16px;
        font-weight: 600;
        margin-top: 15px;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    .verdict-positive {
        background: rgba(16, 185, 129, 0.15);
        border: 1px solid rgba(16, 185, 129, 0.3);
        color: #34d399;
    }
    
    .verdict-negative {
        background: rgba(239, 68, 68, 0.15);
        border: 1px solid rgba(239, 68, 68, 0.3);
        color: #f87171;
    }
    
    .verdict-neutral {
        background: rgba(245, 158, 11, 0.15);
        border: 1px solid rgba(245, 158, 11, 0.3);
        color: #fbbf24;
    }

    /* Mikro Animasyonlar */
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }
    
    .pulse-animation {
        animation: pulse 2s infinite ease-in-out;
    }
</style>
""", unsafe_allow_html=True)

# Başlık Alanı
st.markdown('<div class="glow-text">🧠 Yapay Zeka Destekli Müşteri Yorum Analizi</div>', unsafe_allow_html=True)
st.markdown("<p style='font-size: 1.15rem; color: #94a3b8; margin-top: -10px;'>Müşterilerinizin geri bildirimlerini saniyeler içinde analiz edin, duygu durumunu ve memnuniyet oranlarını keşfedin.</p>", unsafe_allow_html=True)
st.markdown("<hr style='border-color: rgba(255,255,255,0.08); margin-bottom: 25px;'>", unsafe_allow_html=True)

# Session State Hazırlığı
if 'input_text' not in st.session_state:
    st.session_state['input_text'] = ""

# Örnek yorumları yüklemek için callback fonksiyonları
def load_sample(text_content):
    st.session_state['input_text'] = text_content

# Düzen: Yan yana iki ana kolon
col_left, col_right = st.columns([1.1, 0.9], gap="large")

with col_left:
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.subheader("📝 Müşteri Yorumu Girişi")
    
    # Metin alanı
    text_input = st.text_area(
        "Analiz edilecek yorum metnini girin:",
        value=st.session_state['input_text'],
        height=180,
        placeholder="Örn: Siparişim çok hızlı geldi, ürün kalitesi mükemmel! Teşekkür ederim...",
        key="text_area_main"
    )
    
    # Hızlı Örnekler
    st.markdown("<span style='font-size: 0.9rem; color: #94a3b8;'>Hızlı Deneme Örnekleri:</span>", unsafe_allow_html=True)
    
    sample_col1, sample_col2, sample_col3 = st.columns(3)
    with sample_col1:
        if st.button("😊 Pozitif Örnek", use_container_width=True, help="Harika bir müşteri yorumu yükler"):
            load_sample("Ürün paketlemesi çok özenliydi ve teslimat çok hızlı gerçekleşti. Kalitesine bayıldım, kesinlikle tavsiye ederim!")
            st.rerun()
    with sample_col2:
        if st.button("😔 Negatif Örnek", use_container_width=True, help="Şikayet içeren bir müşteri yorumu yükler"):
            load_sample("Kargo günlerce gelmedi, müşteri hizmetleri de hiç yardımcı olmadı. Ürün ise defolu çıktı, kesinlikle iade edeceğim.")
            st.rerun()
    with sample_col3:
        if st.button("😐 Karmaşık/Nötr Örnek", use_container_width=True, help="Kararsız bir müşteri yorumu yükler"):
            load_sample("Ürün fiyatına göre fena değil ama kargo süresi beklediğimden biraz uzun sürdü. Yine de iş görür.")
            st.rerun()
            
    st.markdown("</div>", unsafe_allow_html=True)

    # Analiz Et Butonu
    submit_button = st.button("🚀 Duygu Durumunu Analiz Et", use_container_width=True, type="primary")

with col_right:
    st.markdown('<div class="main-card" style="height: 100%;">', unsafe_allow_html=True)
    st.subheader("📊 Analiz Sonuçları")
    
    # Analiz tetiklendiğinde veya metin varsa
    if submit_button:
        # Metin alanı boş mu kontrol et (st.session_state veya text_input üzerinden)
        actual_text = text_input.strip()
        if not actual_text:
            st.warning("Lütfen analiz etmek için bir yorum metni girin.")
        else:
            with st.spinner("BERT Modeli Yorumu Analiz Ediyor..."):
                headers = {"x-api-key": API_KEY or ""}
                try:
                    response = requests.post(
                        API_URL,
                        json={"text": actual_text},
                        headers=headers,
                        timeout=15
                    )
                    
                    if response.status_code == 200:
                        result = response.json()
                        pos_score = result.get("positive", 0.0)
                        neg_score = result.get("negative", 0.0)
                        
                        # Karar ve Görsel Tasarım
                        st.markdown("<p style='font-size: 1rem; color: #94a3b8; margin-bottom: 2px;'>Duygu Durum Dağılımı</p>", unsafe_allow_html=True)
                        
                        # Özel İlerleme Çubukları (Custom Progress Bars)
                        st.markdown(f"**Pozitiflik Oranı:** {pos_score:.1%}")
                        st.progress(pos_score)
                        
                        st.markdown(f"**Negatiflik Oranı:** {neg_score:.1%}")
                        st.progress(neg_score)
                        
                        # Karar Metni ve Stil
                        if pos_score > 0.60:
                            st.markdown(
                                f'<div class="verdict-box verdict-positive pulse-animation">😊 <b>Pozitif:</b> Bu yorum güçlü bir memnuniyet bildiriyor. ({pos_score:.1%})</div>',
                                unsafe_allow_html=True
                            )
                        elif neg_score > 0.60:
                            st.markdown(
                                f'<div class="verdict-box verdict-negative pulse-animation">😔 <b>Negatif:</b> Bu yorum müşteri memnuniyetsizliği içeriyor. ({neg_score:.1%})</div>',
                                unsafe_allow_html=True
                            )
                        else:
                            st.markdown(
                                f'<div class="verdict-box verdict-neutral">😐 <b>Nötr / Kararsız:</b> Yorumda karışık duygular veya nötr ifadeler baskın.</div>',
                                unsafe_allow_html=True
                            )
                            
                        # Metrik Kartları
                        st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
                        m_col1, m_col2 = st.columns(2)
                        with m_col1:
                            st.metric("Pozitif Skor", f"{pos_score:.2%}", delta=None)
                        with m_col2:
                            st.metric("Negatif Skor", f"{neg_score:.2%}", delta=None)
                            
                    elif response.status_code == 401:
                        st.error("🔒 Yetkilendirme Hatası: API Anahtarı geçersiz veya bulunamadı.")
                    else:
                        st.error(f"❌ API Hatası (Kod: {response.status_code}): {response.text}")
                except requests.exceptions.ConnectionError:
                    st.error("🔌 Backend Sunucusuna Bağlanılamadı! Lütfen backend FastAPI servisinin çalıştığından emin olun.")
                except Exception as e:
                    st.error(f"💥 Beklenmedik bir hata oluştu: {e}")
    else:
        st.info("Analiz sonuçları burada görüntülenecektir. Lütfen sol taraftaki alana bir yorum yazıp 'Duygu Durumunu Analiz Et' butonuna tıklayın.")
        
    st.markdown("</div>", unsafe_allow_html=True)

# Alt Bilgi (Footer)
st.markdown("<br><br><hr style='border-color: rgba(255,255,255,0.08);'>", unsafe_allow_html=True)
footer_col1, footer_col2 = st.columns([1, 1])
with footer_col1:
    st.caption("AI Destekli Yorum Analiz Sistemi v1.0.0 | Model: dbmdz / BERTurk Sentiment")
with footer_col2:
    st.markdown("<div style='text-align: right; font-size: 0.8rem; color: #64748b;'>API Key Güvenliği ve FastAPI Backend ile Entegre</div>", unsafe_allow_html=True)