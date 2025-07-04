# WellnessConnect - AI-Powered Health Concierge Platform

WellnessConnect is a WhatsApp-based AI health concierge that pre-qualifies leads, schedules appointments, and provides personalized wellness recommendations for The Wellness London.

## Features

- **AI Chatbot Integration**: WhatsApp Business integration with Claude AI assistant
- **Smart Lead Qualification**: Automatic categorization by treatment type and urgency
- **Personalized Content Delivery**: Targeted wellness content in English/Arabic
- **Automated Follow-up**: Post-treatment care reminders and wellness plan delivery
- **White-label Ready**: Scalable solution for other wellness clinics

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy environment variables:
   ```bash
   cp .env.example .env
   ```
4. Configure your environment variables in `.env`
5. Set up the database:
   ```bash
   python scripts/setup_database.py
   ```
6. Seed initial data:
   ```bash
   python scripts/seed_data.py
   ```

## Running the Application

```bash
python main.py
```

## API Documentation

See `docs/api_documentation.md` for detailed API documentation.

## Deployment

See `docs/deployment_guide.md` for deployment instructions.

## White-label Setup

See `docs/white_label_setup.md` for white-label configuration.

## License

Proprietary - The Wellness London