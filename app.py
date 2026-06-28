# -*- coding: utf-8 -*-
"""
AI Kişisel Finans Asistanı Streamlit Arayüzü (Ana Giriş Noktası)
Bu dosya, Streamlit Cloud'un doğrudan çalıştırabilmesi için kök dizinde yer alan ana giriş noktasıdır.
"""

import streamlit as st
import requests
import plotly.express as px
import plotly.graph_objects as go
import json
import os
import sys
from pathlib import Path

# Proje dizinini Python yoluna ekle (böylece 'backend' paketini bulabilir)
current_dir = Path(__file__).resolve().parent
root_dir = current_dir / "ypaya zeka" / "AI AGENT TABANLI KİŞİSEL FİNANS & HARCAMA ASİSTANI"
if str(root_dir) not in sys.path:
    sys.path.append(str(root_dir))

# Backend modüllerini içe aktar (Direct Agent Mode için)
try:
    from backend.agent import FinanceAgent
    AGENT_AVAILABLE = True
except ImportError:
    AGENT_AVAILABLE = False

# Sayfa Yapılandırması
st.set_page_config(
    page_title="AI Kişisel Finans & Harcama Asistanı",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS Enjeksiyonu - Modern Glassmorphism & Gradient Tema
def inject_custom_css():
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        /* Ana font ayarı */
        html, body, [class*="css"] {
            font-family: 'Outfit', sans-serif;
        }
        
        /* Arka plan ve cam efekti kartlar */
        .main {
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
            color: #f8fafc;
        }
        
        /* Ana Başlık Alanı */
        .header-container {
            background: linear-gradient(90deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
            padding: 2.5rem;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(99, 102, 241, 0.3);
            margin-bottom: 2.5rem;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        .header-container h1 {
            color: #ffffff;
            font-weight: 800;
            font-size: 2.8rem;
            margin: 0;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        }
        .header-container p {
            color: #e2e8f0;
            font-size: 1.2rem;
            margin-top: 0.5rem;
            font-weight: 400;
        }
        
        /* Premium Bilgi Kartları */
        .finance-card {
            background: rgba(30, 41, 59, 0.7);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 16px;
            padding: 1.5rem;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease;
            margin-bottom: 1rem;
        }
        .finance-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 40px 0 rgba(99, 102, 241, 0.2);
            border-color: rgba(99, 102, 241, 0.3);
        }
        
        /* AI Öneriler Kartları */
        .suggestion-card {
            background: rgba(16, 185, 129, 0.1);
            border-left: 5px solid #10b981;
            border-radius: 8px;
            padding: 1rem 1.5rem;
            margin-bottom: 1rem;
            transition: all 0.2s ease;
        }
        .suggestion-card:hover {
            background: rgba(16, 185, 129, 0.15);
            transform: translateX(4px);
        }
        
        /* Buton Tasarımı */
        .stButton>button {
            background: linear-gradient(90deg, #6366f1 0%, #a855f7 100%);
            color: white !important;
            border: none;
            padding: 0.75rem 2rem;
            font-weight: 600;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
            transition: all 0.3s ease;
            width: 100%;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #4f46e5 0%, #9333ea 100%);
            box-shadow: 0 6px 20px rgba(99, 102, 241, 0.6);
            transform: translateY(-2px);
        }
        
        /* Sidebar Styling */
        section[data-testid="stSidebar"] {
            background-color: #0f172a;
            border-right: 1px solid rgba(255, 255, 255, 0.05);
        }
        
        /* Durum Göstergeleri */
        .badge {
            display: inline-block;
            padding: 0.25em 0.6em;
            font-size: 75%;
            font-weight: 700;
            line-height: 1;
            text-align: center;
            white-space: nowrap;
            vertical-align: baseline;
            border-radius: 0.25rem;
            margin-right: 5px;
        }
        .badge-success { background-color: #10b981; color: white; }
        .badge-warning { background-color: #f59e0b; color: white; }
        .badge-danger { background-color: #ef4444; color: white; }
    </style>
    """, unsafe_allow_html=True)

inject_custom_css()

# API Çağrısı Yapan Fonksiyon
def call_api(user_input: str, income: float, backend_url: str) -> dict:
    try:
        payload = {
            "user_input": user_input,
            "income": income
        }
        response = requests.post(f"{backend_url}/analyze", json=payload, timeout=90)
        if response.status_code == 200:
            return response.json()
        else:
            return {"status": "error", "message": f"Sunucu hatası (Kod {response.status_code}): {response.text}"}
    except Exception as e:
        return {"status": "error", "message": f"API sunucusuna bağlanılamadı: {str(e)}"}

# ----------------- ARAYÜZ TASARIMI -----------------

# Üst Başlık Banner'ı
st.markdown("""
<div class="header-container">
    <h1>💰 AI Agent Tabanlı Kişisel Finans & Harcama Asistanı</h1>
    <p>Harcamalarınızı serbest metin olarak yazın; yapay zeka analiz etsin, bütçelesin ve tasarruf yollarını göstersin!</p>
</div>
""", unsafe_allow_html=True)

# Yan Panel (Sidebar)
with st.sidebar:
    st.image("https://img.icons8.com/isometric/100/financial-growth-analysis.png", width=70)
    st.markdown("### ⚙️ Çalışma Modu & Ayarlar")
    
    # Çalışma modu seçimi
    run_mode = st.radio(
        "Analiz Yöntemi",
        ["API Sunucusu Üzerinden", "Doğrudan Agent (Bulut & Bağımsız Mod)"],
        index=1, # Canlıda doğrudan çalıştırabilmek için varsayılan olarak direct mode seçtik
        help="API modunda FastAPI sunucusuna bağlanır. Bağımsız modda ise API anahtarlarını doğrudan bu uygulama üzerinden kullanır."
    )
    
    if run_mode == "API Sunucusu Üzerinden":
        backend_url = st.text_input("FastAPI Sunucu URL'si", value="http://localhost:8000")
        gemini_api_key = None
        groq_api_key = None
    else:
        st.info("Bu modda FastAPI sunucusuna ihtiyaç duyulmaz. API anahtarlarını aşağıya girin veya .env / secrets ayarlarına ekleyin.")
        # Env'den oku
        env_gemini = os.getenv("GEMINI_API_KEY") or ""
        env_groq = os.getenv("GROQ_API_KEY") or ""
        
        # Streamlit secrets kontrolü (Streamlit Cloud için)
        if "GEMINI_API_KEY" in st.secrets:
            env_gemini = st.secrets["GEMINI_API_KEY"]
        if "GROQ_API_KEY" in st.secrets:
            env_groq = st.secrets["GROQ_API_KEY"]
            
        gemini_api_key = st.text_input("Gemini API Key", value=env_gemini, type="password")
        groq_api_key = st.text_input("Groq API Key", value=env_groq, type="password")
        backend_url = None
        
    st.markdown("---")
    st.markdown("### 💡 Nasıl Kullanılır?")
    st.markdown(
        "1. **Gelirinizi Girin**: Aylık net gelirinizi TL cinsinden yazın.\n"
        "2. **Harcama Metnini Girin**: Günlük notlarınızı, banka SMS'lerini veya alışverişlerinizi yazın.\n"
        "3. **Analiz Et Butonuna Basın**: Agent 6 adımlı pipeline'ı tamamlasın.\n"
        "4. **Grafikleri & Önerileri Keşfedin**: Tasarruf oranlarınızı inceleyin."
    )
    
    st.markdown("---")
    # Hazır örnek senaryolar
    st.markdown("### 📋 Örnek Senaryolar")
    scenario = st.selectbox(
        "Bir örnek şablon seçin:",
        [
            "Seçim Yapın...",
            "1. Yoğun Şehir Yaşamı (Orta Gelir)",
            "2. Öğrenci Bütçesi",
            "3. Banka SMS Formatı",
            "4. Karışık & Düzensiz Girdi"
        ]
    )
    
    example_text = ""
    example_income = 0.0
    
    if scenario == "1. Yoğun Şehir Yaşamı (Orta Gelir)":
        example_income = 45000.0
        example_text = (
            "Kira 16500 TL ödedim. Aidat 1200 TL. Elektrik faturası 650, doğalgaz 1400 TL geldi. "
            "Migros market alışverişi 3400 TL. Haftasonu dışarıda yemeğe 2100 TL gitti. "
            "Netflix 139 TL, Spotify 59 TL ve Youtube Premium 79 TL abonelik ödemelerim çekildi. "
            "Benzinlikten arabaya 1500 TL yakıt aldım. Tiyatro bileti için 800 TL harcadım."
        )
    elif scenario == "2. Öğrenci Bütçesi":
        example_income = 8500.0
        example_text = (
            "Yurt ücreti 2500 TL. Okul yemekhanesine 600 TL yükledim. "
            "Dışarıda arkadaşlarla kahve ve yemek 1800 TL tuttu. "
            "Kitap ve kırtasiye alışverişi 900 TL. Spotify aboneliği 59 TL. "
            "Konser bileti aldım 750 TL. Otobüs kartı yüklemesi 250 TL."
        )
    elif scenario == "3. Banka SMS Formatı":
        example_income = 35000.0
        example_text = (
            "Kartınızla 15.06 tarihinde SHELL firmasından 1200.00 TL tutarında harcama yapılmıştır.\n"
            "Kartınızla 16.06 tarihinde MİGROS firmasından 850.50 TL tutarında harcama yapılmıştır.\n"
            "Kartınızla 17.06 tarihinde NETFLIX firmasından 139.00 TL tutarında abonelik çekilmiştir.\n"
            "Kira havalesi: 12000 TL Ev Sahibi Ahmet."
        )
    elif scenario == "4. Karışık & Düzensiz Girdi":
        example_income = 28000.0
        example_text = (
            "dün spora yazıldım 1200 lira verdik. ev kirasını ödedim 9500 tl. "
            "yol parası 350 tl tuttu bu hafta. akşam arkadaşlarla bir şeyler içtik 800. "
            "netflix 139 tl olmuş. internet faturası da 280 lira geldi. "
            "ha bir de trendyoldan 1400 tlye mont aldım."
        )

# Ana Ekran Tasarımı
col_inputs, col_visuals = st.columns([1, 1.2])

with col_inputs:
    st.markdown("### 📥 Giriş Bilgileri")
    
    # Gelir Girişi
    income_val = st.number_input(
        "Aylık Net Geliriniz (TL)", 
        min_value=0.0, 
        value=example_income if example_income > 0 else 25000.0, 
        step=500.0,
        help="50/30/20 kuralına göre bütçeleme yapılması için gereklidir."
    )
    
    # Harcama Girişi
    user_input_val = st.text_area(
        "Harcama Detayları / Notlar veya Banka SMS'leri",
        value=example_text if example_text else "",
        placeholder="Örn: Bu ay ev kirası 10000 TL, market alışverişi 2500 TL, benzin 1200 TL ödedim...",
        height=250,
        help="Buraya serbest biçimde harcamalarınızı yazabilirsiniz. AI asistanı bunları otomatik olarak ayıklayıp kategorilere ayıracaktır."
    )
    
    # Analiz Et Butonu
    analyze_btn = st.button("🔍 Harcamaları Analiz Et", type="primary")

# Analiz Sonuçları ve Gösterimi
with col_visuals:
    st.markdown("### 📊 Analiz Ekranı")
    
    # Butona basıldığında veya oturumda zaten sonuç varsa çalıştır
    if analyze_btn:
        if not user_input_val.strip() or len(user_input_val.strip()) < 10:
            st.error("⚠️ Lütfen analiz edilmek üzere en az 10 karakterden oluşan geçerli bir harcama metni girin.")
        else:
            with st.spinner("🤖 AI Finans Asistanı verilerinizi işliyor, lütfen bekleyin..."):
                result = None
                
                # API Modu
                if run_mode == "API Sunucusu Üzerinden":
                    result = call_api(user_input_val, income_val, backend_url)
                
                # Doğrudan Agent Modu (Bağımsız Mod)
                else:
                    if not AGENT_AVAILABLE:
                        st.error("❌ backend/agent.py dosyası veya gerekli kütüphaneler yüklenemedi. Sunucu modunu deneyin.")
                    elif not gemini_api_key and not groq_api_key:
                        st.error("⚠️ Lütfen en az bir adet geçerli API anahtarı girin (Gemini veya Groq).")
                    else:
                        try:
                            # Geçici olarak girilen key'leri set et veya doğrudan agent instance'a geç
                            agent_instance = FinanceAgent(gemini_api_key=gemini_api_key, groq_api_key=groq_api_key)
                            result = agent_instance.analyze(user_input_val, income=income_val)
                        except Exception as ex:
                            result = {"status": "error", "message": str(ex)}
                
                # Sonuçları Göster
                if result and result.get("status") == "success":
                    st.session_state["analysis_result"] = result
                    st.balloons()
                    st.success("🎉 Analiz başarıyla tamamlandı!")
                elif result:
                    st.error(f"❌ Analiz sırasında bir hata oluştu: {result.get('message')}")
                    
    # Oturumdaki veriyi yükle
    if "analysis_result" in st.session_state:
        res = st.session_state["analysis_result"]
        chart_data = res.get("chart_data", {})
        
        # Toplam harcamayı hesapla
        total_expense = sum(chart_data.values())
        
        # Finansal Sağlık Skoru Hesaplama (Özel Formül)
        # İstekler (Eğlence + Abonelik) toplam harcamanın %30'undan fazlaysa veya bütçe açığı varsa skor düşer
        wishes = chart_data.get("eğlence", 0) + chart_data.get("abonelik", 0)
        needs = chart_data.get("kira", 0) + chart_data.get("yemek", 0) + chart_data.get("ulaşım", 0) + chart_data.get("diğer", 0)
        
        health_score = 100
        
        # Gelir bilgisi varsa gelire göre bütçe açığı kontrolü
        if income_val > 0:
            if total_expense > income_val:
                # Bütçe aşımı oranı kadar ceza puanı (maksimum 40 puan)
                over_ratio = (total_expense - income_val) / income_val
                health_score -= min(40, int(over_ratio * 100))
                
            if income_val > 0:
                wish_ratio = wishes / income_val
                if wish_ratio > 0.3:
                    health_score -= min(30, int((wish_ratio - 0.3) * 100))
        else:
            # Gelir belirtilmediyse toplam harcamadaki istek oranına bak
            if total_expense > 0:
                wish_ratio = wishes / total_expense
                if wish_ratio > 0.3:
                    health_score -= min(30, int((wish_ratio - 0.3) * 100))
        
        health_score = max(10, min(100, health_score))
        
        # Üst Metrikler (Gelir, Toplam Harcama, Tasarruf, Sağlık Skoru)
        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1:
            st.markdown(f"""
            <div class="finance-card" style="text-align: center;">
                <p style="margin:0; font-size: 0.9rem; color:#94a3b8;">Aylık Toplam Harcama</p>
                <h3 style="margin:5px 0; font-size: 1.8rem; color:#f43f5e; font-weight:700;">{total_expense:,.2f} TL</h3>
            </div>
            """, unsafe_allow_html=True)
            
        with col_m2:
            remaining = income_val - total_expense
            rem_color = "#10b981" if remaining >= 0 else "#ef4444"
            st.markdown(f"""
            <div class="finance-card" style="text-align: center;">
                <p style="margin:0; font-size: 0.9rem; color:#94a3b8;">Kalan / Tasarruf</p>
                <h3 style="margin:5px 0; font-size: 1.8rem; color:{rem_color}; font-weight:700;">{remaining:,.2f} TL</h3>
            </div>
            """, unsafe_allow_html=True)
            
        with col_m3:
            score_color = "#10b981" if health_score >= 70 else ("#f59e0b" if health_score >= 45 else "#ef4444")
            st.markdown(f"""
            <div class="finance-card" style="text-align: center;">
                <p style="margin:0; font-size: 0.9rem; color:#94a3b8;">Finansal Sağlık Skoru</p>
                <h3 style="margin:5px 0; font-size: 1.8rem; color:{score_color}; font-weight:700;">{health_score}/100</h3>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("👈 Analizi başlatmak için soldaki bilgileri doldurup 'Harcamaları Analiz Et' butonuna tıklayın.")

# ----------------- TABS ALANI -----------------
if "analysis_result" in st.session_state:
    res = st.session_state["analysis_result"]
    chart_data = res.get("chart_data", {})
    
    st.markdown("---")
    
    # 4 Tab Yapısı
    tab_list, tab_charts, tab_budget, tab_suggestions = st.tabs([
        "📊 Harcama Listesi & Kategoriler", 
        "📈 İnteraktif Grafikler", 
        "💼 50/30/20 Bütçe Analizi", 
        "💡 AI Tasarruf Önerileri"
    ])
    
    # Tab 1: Harcama Listesi & Kategoriler
    with tab_list:
        col_list1, col_list2 = st.columns(2)
        with col_list1:
            st.markdown("#### 🔍 Metinden Ayıklanan Harcamalar")
            st.code(res.get("extracted_expenses", ""), language="text")
        with col_list2:
            st.markdown("#### 🗂️ Kategorize Edilmiş Harcamalar")
            st.code(res.get("categorized_expenses", ""), language="text")
            
    # Tab 2: İnteraktif Grafikler
    with tab_charts:
        st.markdown("#### 📈 Harcama Dağılım Grafikleri")
        
        # Filtrelenmiş kategori verileri (Tutar > 0 olanlar)
        filtered_chart_data = {k: v for k, v in chart_data.items() if v > 0}
        
        if not filtered_chart_data:
            st.warning("Grafik çizilebilecek tutarlı bir harcama verisi bulunamadı.")
        else:
            col_chart1, col_chart2 = st.columns(2)
            
            with col_chart1:
                # 1. Pasta Grafiği (Kategori Dağılımı)
                fig_pie = px.pie(
                    names=list(filtered_chart_data.keys()),
                    values=list(filtered_chart_data.values()),
                    title="Kategorilere Göre Harcama Dağılımı",
                    hole=0.4,
                    color_discrete_sequence=px.colors.qualitative.Pastel
                )
                fig_pie.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font_color='#ffffff',
                    showlegend=True
                )
                st.plotly_chart(fig_pie, use_container_width=True)
                
            with col_chart2:
                # 2. Bar Grafiği (Kategori Tutarları)
                fig_bar = px.bar(
                    x=list(filtered_chart_data.keys()),
                    y=list(filtered_chart_data.values()),
                    title="Kategori Bazlı Harcama Tutarları (TL)",
                    labels={'x': 'Kategori', 'y': 'Tutar (TL)'},
                    color=list(filtered_chart_data.keys()),
                    color_discrete_sequence=px.colors.qualitative.Safe
                )
                fig_bar.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font_color='#ffffff',
                    showlegend=False
                )
                st.plotly_chart(fig_bar, use_container_width=True)
            
            # 3. Harcama Sağlık Skoru Gauge Göstergesi
            st.markdown("<br>", unsafe_allow_html=True)
            fig_gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=health_score,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Harcama Sağlık Durumu", 'font': {'size': 20, 'color': "#ffffff"}},
                gauge={
                    'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#ffffff"},
                    'bar': {'color': "#6366f1"},
                    'bgcolor': "rgba(255, 255, 255, 0.1)",
                    'borderwidth': 2,
                    'bordercolor': "rgba(255,255,255,0.2)",
                    'steps': [
                        {'range': [0, 45], 'color': '#ef4444'},
                        {'range': [45, 70], 'color': '#f59e0b'},
                        {'range': [70, 100], 'color': '#10b981'}
                    ],
                }
            ))
            fig_gauge.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                font={'color': "#ffffff"}
            )
            st.plotly_chart(fig_gauge, use_container_width=True)

    # Tab 3: 50/30/20 Bütçe Analizi
    with tab_budget:
        st.markdown("#### 💼 50/30/20 Kuralına Göre Bütçe Durumu")
        
        # LLM Metin Çıktısını Göster
        st.info(res.get("budget_analysis", "Bütçe analizi verisi mevcut değil."))
        
        # Bütçe Dağılımını Hesapla ve Grafik Çiz
        if income_val > 0:
            st.markdown("##### 📊 Hedef Bütçe Dağılımı ve Gerçekleşen Karşılaştırması")
            
            # Gerçekleşen değerleri kategorilere göre ata
            needs_val = chart_data.get("kira", 0) + chart_data.get("yemek", 0) + chart_data.get("ulaşım", 0)
            wishes_val = chart_data.get("eğlence", 0) + chart_data.get("abonelik", 0)
            other_val = chart_data.get("diğer", 0) # Diğer harcamaları duruma göre paylaştır veya ayrı tut
            needs_val += other_val # Diğer'i güvenli tarafta kalmak için ihtiyaçlara ekleyelim
            
            total_exp = needs_val + wishes_val
            savings_val = max(0.0, income_val - total_exp)
            
            # Hedef Değerler (50/30/20)
            target_needs = income_val * 0.50
            target_wishes = income_val * 0.30
            target_savings = income_val * 0.20
            
            # Çift Bar Grafiği (Hedef vs. Gerçek)
            categories_names = ['İhtiyaçlar (%50)', 'İstekler (%30)', 'Tasarruf (%20)']
            
            fig_budget = go.Figure(data=[
                go.Bar(name='Hedef Bütçe (TL)', x=categories_names, y=[target_needs, target_wishes, target_savings], marker_color='#a855f7'),
                go.Bar(name='Gerçekleşen Harcama (TL)', x=categories_names, y=[needs_val, wishes_val, savings_val], marker_color='#6366f1')
            ])
            
            fig_budget.update_layout(
                barmode='group',
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='#ffffff',
                title="Bütçe Hedefleri ve Mevcut Durum"
            )
            st.plotly_chart(fig_budget, use_container_width=True)

    # Tab 4: AI Tasarruf Önerileri
    with tab_suggestions:
        st.markdown("#### 💡 Kişiselleştirilmiş Tasarruf Önerileri")
        
        # Analiz Sonucu Metnini Göster
        st.markdown("##### 📊 Harcama Alışkanlığı Yorumu")
        st.info(res.get("analysis", ""))
        
        st.markdown("##### 🚀 Uygulanabilir Öneriler")
        
        # AI'dan gelen önerileri st.markdown veya custom card formatında gösterelim
        raw_suggestions = res.get("suggestions", "")
        
        # Satır satır oku, eğer maddeli ise özel stilde göster
        lines = raw_suggestions.split("\n")
        suggestions_box = []
        
        for line in lines:
            if line.strip().startswith("-") or line.strip().startswith("*") or (len(line.strip()) > 0 and line.strip()[0].isdigit() and "." in line.strip()[:3]):
                # Maddeyi temizle
                cleaned_line = line.replace("-", "").replace("*", "").strip()
                if cleaned_line:
                    st.markdown(f"""
                    <div class="suggestion-card">
                        <strong>💡 {cleaned_line}</strong>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                if line.strip():
                    st.write(line.strip())

# Alt Bilgi (Footer)
st.markdown("<br><br><hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; color: #94a3b8; font-size: 0.85rem;'>"
    "Bu uygulama <strong>Google Gemini Pro/Flash</strong> ve <strong>Groq (Llama 3)</strong> API'leri kullanılarak "
    "Agentic Pipeline mimarisiyle geliştirilmiştir.<br>"
    "© 2026 AI Kişisel Finans Asistanı | Tüm Hakları Saklıdır."
    "</p>",
    unsafe_allow_html=True
)
