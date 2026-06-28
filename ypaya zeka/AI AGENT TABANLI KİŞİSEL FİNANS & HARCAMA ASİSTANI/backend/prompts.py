# -*- coding: utf-8 -*-
"""
AI Kişisel Finans Asistanı Prompt Şablonları Dökümanı
Bu dosya, finans asistanı agent'ının tüm aşamalarında LLM'e gönderilecek prompt şablonlarını içerir.
"""

# 1. SYSTEM_PROMPT (String Sabiti)
SYSTEM_PROMPT = (
    "Sen deneyimli, profesyonel bir kişisel finans danışmanı ve finansal analistsin. "
    "Kullanıcıların harcama alışkanlıklarını analiz eder, gereksiz giderleri tespit eder "
    "ve net, uygulanabilir tasarruf önerileri sunarsın. "
    "Cevapların açık, maddeli, sade, profesyonel ve her zaman Türkçe olmalıdır."
)

def get_extraction_prompt(user_input: str) -> str:
    """
    Kullanıcının girdiği serbest metinden harcama kalemlerini ve tutarlarını ayıklayan prompt.
    """
    return f"""
Kullanıcı tarafından girilen aşağıdaki ham metinden harcama kalemlerini ve tutarlarını ayıkla.

Kurallar:
- Tutar belirtilmemişse tahminde bulunma, "belirtilmemiş" yaz.
- Tüm tutarları sayısal değerler olarak ayıkla. Para birimlerini standart hale getir (örneğin 120 TL, 120₺, 120 lira -> 120 TL).
- Harcama dışı bilgileri (örneğin gelir veya harcama ile doğrudan ilgisi olmayan cümleler) yok say.
- Çıktıyı SADECE aşağıdaki formatta ver, ekstra açıklama ekleme:
  Kalem: [Harcama kalemi adı] | Tutar: [Değer ve Para Birimi, örn: 150 TL veya belirtilmemiş]

Ham Kullanıcı Metni:
"{user_input}"
"""

def get_categorization_prompt(expense_list: str) -> str:
    """
    Ayıklanan harcama listesini belirli kategorilere ayıran prompt.
    """
    return f"""
Aşağıda verilen harcama listesini incele ve her bir kalemi aşağıdaki 6 kategoriden birine ata:
Kategoriler: kira, yemek, ulaşım, eğlence, abonelik, diğer

Kurallar:
- Her kalemi sadece bir kategoriye ata.
- Çıktı formatı SADECE aşağıdaki gibi olmalıdır. Ekstra açıklama veya giriş/gelişme cümleleri yazma:
  
  Kategori: kira
  - [Kalem] (Tutar)
  
  Kategori: yemek
  - [Kalem] (Tutar)
  
  (Tüm kategorileri sırayla listele, eğer o kategoride harcama yoksa altına hiçbir şey yazma ya da boş bırak.)

Harcama Listesi:
{expense_list}
"""

def get_analysis_prompt(categorized_data: str) -> str:
    """
    Kategorize edilmiş veriler üzerinden harcama ve risk analizi yapan prompt.
    """
    return f"""
Aşağıdaki kategorize edilmiş harcama verilerini detaylıca analiz et:

Senden istenenler:
1. En yüksek harcama yapılan ilk 2-3 alanı (kategoriyi) ve bunların toplam içindeki ağırlığını değerlendir.
2. Riskli, gereksiz veya optimize edilebilecek (örneğin tekrarlanan abonelikler, dışarıda çok fazla yemek yeme vb.) harcama kalemlerini tespit et.
3. Kullanıcının genel harcama örüntüsü hakkında (örneğin dengeli mi, lüks harcama ağırlıklı mı) profesyonel bir yorum yap.

Analizini anlaşılır, maddeler halinde ve yapıcı bir dille Türkçe olarak sun.

Kategorize Edilmiş Harcama Verileri:
{categorized_data}
"""

def get_suggestion_prompt(analysis_result: str) -> str:
    """
    Yapılan analize göre kullanıcıya tasarruf önerileri sunan prompt.
    """
    return f"""
Aşağıdaki harcama analizi sonuçlarına dayanarak kullanıcı için tasarruf önerileri üret:

Kurallar:
- Net, uygulanabilir ve gerçekçi öneriler sun.
- En az 3, en fazla 7 öneri listele.
- Her bir önerinin altına, bunu neden önerdiğini (analizdeki hangi veriye dayandığını) 1-2 cümleyle açıkla.
- Pozitif ve teşvik edici bir finansal koç dili kullan.

Harcama Analiz Sonucu:
{analysis_result}
"""

def get_budget_analysis_prompt(income: float, categorized_data: str) -> str:
    """
    Kullanıcının geliri ile harcamalarını 50/30/20 kuralına göre karşılaştıran prompt.
    """
    return f"""
Kullanıcının Aylık Net Geliri: {income} TL

Aşağıdaki kategorize edilmiş harcamaları incele. 
50/30/20 Finansal Kuralı çerçevesinde bir bütçe analizi yap:
- %50 İhtiyaçlar (Kira, faturalar, temel market, ulaşım)
- %30 İstekler (Eğlence, dışarıda yemek, abonelikler, sinema)
- %20 Tasarruf/Borç Ödeme (Yatırım, birikim, borç kapatma)

Senden istenenler:
1. Kullanıcının mevcut harcamalarının bu üç gruba (İhtiyaç, İstek, Tasarruf) dağılımını hesapla (yaklaşık yüzde veya tutar olarak).
2. Gelir ile toplam harcamayı karşılaştır (Bütçe açığı var mı, yoksa ne kadar tasarruf edebilir?).
3. 50/30/20 kuralına göre hangi grupta bütçe aşımı yapıldığını ve bunun nasıl dengelenebileceğini açıkla.

Sonuçları Türkçe, net ve maddeler halinde yaz.

Kategorize Edilmiş Harcama Verileri:
{categorized_data}
"""

def get_chart_parsing_prompt(categorized_data: str) -> str:
    """
    Kategorize edilmiş veriyi grafik çizimi için JSON formatına dönüştüren prompt.
    """
    return f"""
Aşağıdaki kategorize edilmiş harcama metnini analiz et ve her bir kategorinin ("kira", "yemek", "ulaşım", "eğlence", "abonelik", "diğer") toplam harcama tutarını hesapla.

Çıktıyı SADECE ve SADECE aşağıdaki gibi geçerli bir JSON objesi olarak ver. Markdown kod blokları veya herhangi bir açıklama ekleme. Sadece saf JSON verisi döndür.

Örnek Çıktı:
{{
  "kira": 5000,
  "yemek": 2300,
  "ulaşım": 800,
  "eğlence": 350,
  "abonelik": 198,
  "diğer": 150
}}

Eğer bir kategoriye ait hiçbir harcama yoksa veya tutar belirtilmemişse o kategorinin değerini 0 yaz. Sayısal değerler dışında bir şey yazma (TL ibaresini ekleme, sadece sayı).

Kategorize Edilmiş Veri:
{categorized_data}
"""
