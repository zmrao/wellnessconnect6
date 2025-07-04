"""
Application settings and configuration
"""

import os
from typing import List
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://localhost/wellnessconnect")
    
    # WhatsApp Business API
    WHATSAPP_ACCESS_TOKEN: str = os.getenv("WHATSAPP_ACCESS_TOKEN", "")
    WHATSAPP_PHONE_NUMBER_ID: str = os.getenv("WHATSAPP_PHONE_NUMBER_ID", "")
    WHATSAPP_WEBHOOK_VERIFY_TOKEN: str = os.getenv("WHATSAPP_WEBHOOK_VERIFY_TOKEN", "")
    WHATSAPP_BUSINESS_ACCOUNT_ID: str = os.getenv("WHATSAPP_BUSINESS_ACCOUNT_ID", "")
    
    # Claude AI
    CLAUDE_API_KEY: str = os.getenv("CLAUDE_API_KEY", "")
    CLAUDE_MODEL: str = os.getenv("CLAUDE_MODEL", "claude-3-sonnet-20240229")
    
    # Redis
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    
    # Application
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    
    # Timezone
    DEFAULT_TIMEZONE: str = os.getenv("DEFAULT_TIMEZONE", "Europe/London")
    
    # Languages
    SUPPORTED_LANGUAGES: List[str] = os.getenv("SUPPORTED_LANGUAGES", "en,ar").split(",")
    DEFAULT_LANGUAGE: str = os.getenv("DEFAULT_LANGUAGE", "en")
    
    # Business Settings
    BUSINESS_NAME: str = os.getenv("BUSINESS_NAME", "The Wellness London")
    BUSINESS_PHONE: str = os.getenv("BUSINESS_PHONE", "+44123456789")
    BUSINESS_EMAIL: str = os.getenv("BUSINESS_EMAIL", "info@thewellnesslondon.com")
    BUSINESS_ADDRESS: str = os.getenv("BUSINESS_ADDRESS", "123 Wellness Street, London, UK")
    
    # Treatment Types
    TREATMENT_TYPES = {
        "BLOOD_TESTING": "blood_testing",
        "PRP": "prp",
        "WEIGHT_MANAGEMENT": "weight_management",
        "GENERAL_WELLNESS": "general_wellness"
    }
    
    # Lead Qualification Statuses
    LEAD_STATUSES = {
        "HOT": "hot",
        "WARM": "warm",
        "COLD": "cold",
        "QUALIFIED": "qualified",
        "UNQUALIFIED": "unqualified"
    }
    
    # Language Codes
    LANGUAGE_CODES = {
        "ENGLISH": "en",
        "ARABIC": "ar"
    }

    class Config:
        env_file = ".env"

settings = Settings()