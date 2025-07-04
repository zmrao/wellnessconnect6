"""
WhatsApp Business API configuration
"""

from config.settings import settings

class WhatsAppConfig:
    # API Endpoints
    BASE_URL = "https://graph.facebook.com/v18.0"
    MESSAGES_ENDPOINT = f"{BASE_URL}/{settings.WHATSAPP_PHONE_NUMBER_ID}/messages"
    MEDIA_ENDPOINT = f"{BASE_URL}/{settings.WHATSAPP_PHONE_NUMBER_ID}/media"
    
    # Headers
    HEADERS = {
        "Authorization": f"Bearer {settings.WHATSAPP_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    # Message Templates
    MESSAGE_TEMPLATES = {
        "WELCOME": {
            "en": "Welcome to {business_name}! 🌟 I'm your AI wellness assistant. How can I help you today?",
            "ar": "مرحباً بك في {business_name}! 🌟 أنا مساعدك الذكي للعافية. كيف يمكنني مساعدتك اليوم؟"
        },
        "APPOINTMENT_CONFIRMATION": {
            "en": "✅ Your appointment has been confirmed for {date} at {time}. We'll send you a reminder 24 hours before.",
            "ar": "✅ تم تأكيد موعدك في {date} في {time}. سنرسل لك تذكيراً قبل 24 ساعة."
        },
        "APPOINTMENT_REMINDER": {
            "en": "⏰ Reminder: You have an appointment tomorrow at {time}. Please reply CONFIRM to confirm or RESCHEDULE to change.",
            "ar": "⏰ تذكير: لديك موعد غداً في {time}. يرجى الرد بـ تأكيد للتأكيد أو إعادة جدولة للتغيير."
        },
        "HEALTH_ASSESSMENT_START": {
            "en": "Let's start your health assessment. This will help us provide personalized recommendations. Ready to begin?",
            "ar": "لنبدأ تقييم صحتك. سيساعدنا هذا في تقديم توصيات شخصية. هل أنت مستعد للبدء؟"
        },
        "FOLLOW_UP": {
            "en": "Hi {name}! How are you feeling after your {treatment} treatment? We'd love to hear about your experience.",
            "