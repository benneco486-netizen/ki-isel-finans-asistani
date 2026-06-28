# -*- coding: utf-8 -*-
"""
AI Kişisel Finans Asistanı Agent Denetleyicisi (Agent Controller)
Bu sınıf, Gemini ve Groq API'lerini kullanarak çok adımlı finans analiz akışını yönetir.
Gemini başarısız olursa otomatik olarak Groq (Llama 3) modeline fallback (yedek) yapar.
"""

import os
import sys
import json
import logging
from dotenv import load_dotenv

# UTF-8 Kodlamasını Terminal İçin Zorunlu Yap (Windows Uyumlu)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

import google.generativeai as genai
from groq import Groq

# Promptları içe aktar
from backend.prompts import (
    SYSTEM_PROMPT,
    get_extraction_prompt,
    get_categorization_prompt,
    get_analysis_prompt,
    get_suggestion_prompt,
    get_budget_analysis_prompt,
    get_chart_parsing_prompt
)

# Loglama ayarları
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class FinanceAgent:
    def __init__(self, gemini_api_key=None, groq_api_key=None):
        """
        FinanceAgent sınıfını ilklendirir. API anahtarlarını .env'den veya parametrelerden okur.
        """
        # .env dosyasını yükle
        load_dotenv()

        # API anahtarlarını al (Parametre öncelikli, yoksa env'den)
        self.gemini_key = gemini_api_key or os.getenv("GEMINI_API_KEY")
        self.groq_key = groq_api_key or os.getenv("GROQ_API_KEY")

        # Gemini API Kurulumu
        if self.gemini_key:
            genai.configure(api_key=self.gemini_key)
            logger.info("Gemini API başarıyla kuruldu.")
        else:
            logger.warning("Gemini API Anahtarı bulunamadı! Lütfen .env dosyasını kontrol edin.")

        # Groq API Kurulumu
        if self.groq_key:
            self.groq_client = Groq(api_key=self.groq_key)
            logger.info("Groq API istemcisi başarıyla kuruldu.")
        else:
            self.groq_client = None
            logger.warning("Groq API Anahtarı bulunamadı! Yedek LLM devre dışı kalabilir.")

    def _call_llm(self, prompt: str) -> str:
        """
        LLM çağrısını gerçekleştirir. Önce Gemini'yi dener. Başarısız olursa Groq'a geçer.
        """
        # 1. Adım: Gemini Pro/Flash
        if self.gemini_key:
            try:
                logger.info("Gemini-1.5-Flash modeline istek gönderiliyor...")
                model = genai.GenerativeModel(
                    model_name="gemini-1.5-flash",
                    system_instruction=SYSTEM_PROMPT
                )
                response = model.generate_content(prompt)
                if response and response.text:
                    logger.info("Gemini yanıtı başarıyla alındı.")
                    return response.text.strip()
            except Exception as e:
                logger.error(f"Gemini API çağrısı sırasında hata oluştu: {str(e)}")
                logger.info("Gemini başarısız oldu, Groq'a (Llama 3) geçiliyor...")

        # 2. Adım: Groq / Llama3 Fallback
        if self.groq_client and self.groq_key:
            try:
                logger.info("Groq (llama3-8b-8192) modeline istek gönderiliyor...")
                chat_completion = self.groq_client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": prompt}
                    ],
                    model="llama3-8b-8192",
                    temperature=0.2
                )
                response_text = chat_completion.choices[0].message.content
                if response_text:
                    logger.info("Groq (Llama 3) yanıtı başarıyla alındı.")
                    return response_text.strip()
            except Exception as e:
                logger.error(f"Groq API çağrısı sırasında hata oluştu: {str(e)}")
                raise Exception("Hem Gemini hem de Groq (Llama 3) servisleri yanıt vermedi. Lütfen API anahtarlarınızı ve internet bağlantınızı kontrol edin.")
        else:
            raise Exception("Gemini API çağrısı başarısız oldu ve Groq API yapılandırılmadığı için yedek sisteme geçilemedi.")

    def analyze(self, user_input: str, income: float = None) -> dict:
        """
        Kullanıcı girdisini analiz eden 6 adımlı pipeline akışı.
        """
        logger.info("🚀 AI Finans Analiz Süreci Başlıyor...")

        try:
            # ADIM 1: Harcama Kalemlerini Ayıklama
            logger.info("🔍 Adım 1: Harcama Kalemleri Ayıklanıyor...")
            extraction_prompt = get_extraction_prompt(user_input)
            extracted_expenses = self._call_llm(extraction_prompt)
            logger.info("✅ Adım 1 tamamlandı: Harcamalar ayıklandı.")

            # ADIM 2: Kategorilere Ayırma
            logger.info("🗂️ Adım 2: Harcamalar Kategorize Ediliyor...")
            categorization_prompt = get_categorization_prompt(extracted_expenses)
            categorized_expenses = self._call_llm(categorization_prompt)
            logger.info("✅ Adım 2 tamamlandı: Harcamalar kategorilere ayrıldı.")

            # ADIM 3: Risk ve Harcama Analizi
            logger.info("📈 Adım 3: Harcama Analizi Yapılıyor...")
            analysis_prompt = get_analysis_prompt(categorized_expenses)
            analysis_result = self._call_llm(analysis_prompt)
            logger.info("✅ Adım 3 tamamlandı: Harcamalar analiz edildi.")

            # ADIM 4: Tasarruf Önerileri
            logger.info("💡 Adım 4: Tasarruf Önerileri Oluşturuluyor...")
            suggestion_prompt = get_suggestion_prompt(analysis_result)
            suggestions = self._call_llm(suggestion_prompt)
            logger.info("✅ Adım 4 tamamlandı: Öneriler oluşturuldu.")

            # ADIM 5: Bütçe Analizi (Eğer Gelir Girildiyse)
            budget_analysis = "Gelir bilgisi girilmediği için bütçe analizi yapılmadı."
            if income is not None and income > 0:
                logger.info(f"💼 Adım 5: {income} TL bütçeye göre analiz yapılıyor...")
                budget_prompt = get_budget_analysis_prompt(income, categorized_expenses)
                budget_analysis = self._call_llm(budget_prompt)
                logger.info("✅ Adım 5 tamamlandı: Bütçe analizi yapıldı.")

            # ADIM 6: Grafik İçin JSON Çıktısı Hazırlama
            logger.info("📊 Adım 6: Grafikler için veriler ayrıştırılıyor...")
            chart_prompt = get_chart_parsing_prompt(categorized_expenses)
            chart_json_str = self._call_llm(chart_prompt)
            
            # JSON'u doğrula ve parse et
            try:
                # Bazen model markdown kod bloğu içine yerleştirebilir, temizleyelim
                clean_json_str = chart_json_str.strip()
                if clean_json_str.startswith("```json"):
                    clean_json_str = clean_json_str[7:]
                if clean_json_str.endswith("```"):
                    clean_json_str = clean_json_str[:-3]
                clean_json_str = clean_json_str.strip()
                
                chart_data = json.loads(clean_json_str)
                logger.info("✅ Adım 6 tamamlandı: Grafik verisi JSON olarak ayrıştırıldı.")
            except Exception as json_err:
                logger.error(f"Grafik verisi JSON parse hatası: {str(json_err)}. Dönen metin: {chart_json_str}")
                # Hata durumunda varsayılan boş yapıyı döndür
                chart_data = {"kira": 0, "yemek": 0, "ulaşım": 0, "eğlence": 0, "abonelik": 0, "diğer": 0}

            logger.info("🎉 Tüm analiz süreci başarıyla tamamlandı!")
            
            return {
                "status": "success",
                "extracted_expenses": extracted_expenses,
                "categorized_expenses": categorized_expenses,
                "analysis": analysis_result,
                "suggestions": suggestions,
                "budget_analysis": budget_analysis,
                "chart_data": chart_data
            }

        except Exception as e:
            logger.error(f"❌ Analiz pipeline hatası: {str(e)}")
            return {
                "status": "error",
                "message": str(e)
            }
