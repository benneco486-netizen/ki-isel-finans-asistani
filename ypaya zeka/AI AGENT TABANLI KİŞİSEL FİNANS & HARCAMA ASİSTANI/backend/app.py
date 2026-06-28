# -*- coding: utf-8 -*-
"""
AI Kişisel Finans Asistanı FastAPI REST API
Bu servis, Streamlit veya diğer dış istemcilerin finans asistanı agent'ı ile
iletişim kurmasını sağlayan HTTP uç noktalarını (endpoints) sunar.
"""

import sys
from pathlib import Path
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

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

# FastAPI Uygulaması Tanımı
app = FastAPI(
    title="AI Personal Finance Assistant API",
    description="Kullanıcı metinlerinden harcama analizi, kategorizasyon ve tasarruf önerileri üreten AI Agent API'si.",
    version="1.0"
)

# CORS Ayarları (Streamlit veya frontend bağlantıları için)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global Agent Örneği (Hızlı erişim için ilk yüklemede oluşturulur)
agent = FinanceAgent()

# Pydantic İstek ve Yanıt Modelleri
class AnalyzeRequest(BaseModel):
    user_input: str = Field(
        ..., 
        min_length=10, 
        description="Analiz edilecek harcama metni (örn: faturalar, market alışverişleri vb.)",
        examples=["Bu ay kira 7500 TL, market 2300 TL, Netflix 139 TL ödedim. Benzin için de 800 TL harcadım."]
    )
    income: Optional[float] = Field(
        None, 
        ge=0, 
        description="Kullanıcının aylık net geliri (50/30/20 bütçe analizi için isteğe bağlı)"
    )

class AnalyzeResponse(BaseModel):
    status: str
    extracted_expenses: str
    categorized_expenses: str
    analysis: str
    suggestions: str
    budget_analysis: str
    chart_data: Dict[str, float]

class HealthResponse(BaseModel):
    status: str
    message: str

@app.post("/analyze", response_model=AnalyzeResponse, summary="Harcama Metnini Analiz Et")
async def analyze_expenses(request: AnalyzeRequest):
    """
    Kullanıcının girdiği serbest harcama metnini ve isteğe bağlı gelir bilgisini alarak
    çok adımlı AI analiz sürecini (ayıklama, sınıflandırma, analiz, bütçe kıyaslama, grafik oluşturma) çalıştırır.
    """
    try:
        # Agent analizini çalıştır
        result = agent.analyze(request.user_input, income=request.income)
        
        if result.get("status") == "error":
            raise HTTPException(
                status_code=500, 
                detail=f"Agent analiz işlemi başarısız oldu: {result.get('message')}"
            )
            
        return AnalyzeResponse(
            status=result["status"],
            extracted_expenses=result["extracted_expenses"],
            categorized_expenses=result["categorized_expenses"],
            analysis=result["analysis"],
            suggestions=result["suggestions"],
            budget_analysis=result["budget_analysis"],
            chart_data=result["chart_data"]
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"API sunucusunda bir iç hata oluştu: {str(e)}"
        )

@app.get("/health", response_model=HealthResponse, summary="Servis Sağlık Kontrolü")
async def health_check():
    """
    API servisinin aktif olup olmadığını kontrol eden sağlık uç noktası.
    """
    return HealthResponse(
        status="ok",
        message="AI Finans Asistanı API servisi aktif ve çalışıyor."
    )

if __name__ == "__main__":
    # Uvicorn ile API sunucusunu localhost 8000 portunda başlat
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
