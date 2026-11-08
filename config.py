"""
================================================================================
🛡️ PAYGUARD AI — AUTONOMOUS MULTIMODAL FINTECH & PAYPAL EXECUTION PLATFORM
================================================================================
Copyright (c) 2026 Ibrahim Adel (AI Systems Architect & Founder @ MuseOS Labs)
Approved Organization Credential ID: aitenant-e00nrfr08gavh9pj8c
Protected Internationally under the Berne Convention for the Protection of
Literary and Artistic Works (180+ Countries) & MIT Open-Core Attribution License.
Unauthorized removal of author attribution or proprietary sovereign weights is
strictly prohibited.
================================================================================
"""
import os

# Cloud AI & Financial Sandbox Credentials (Zero Hardcoded Secrets Policy)
NEBIUS_API_KEY = os.getenv("NEBIUS_API_KEY", "")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "")

# PayPal Developer Platform Sandbox OAuth2 Credentials
PAYPAL_CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID", "")
PAYPAL_CLIENT_SECRET = os.getenv("PAYPAL_CLIENT_SECRET", "")
PAYPAL_API_BASE = os.getenv("PAYPAL_API_BASE", "https://api-m.sandbox.paypal.com")

# SafeAgents 200-SOP Constitutional Financial Firewall Policy Limits
MAX_AUTONOMOUS_PAYOUT_USD = float(os.getenv("MAX_AUTONOMOUS_PAYOUT_USD", "500.00"))
DAILY_BUDGET_CAP_USD = float(os.getenv("DAILY_BUDGET_CAP_USD", "5000.00"))
MAX_PRICE_VARIANCE_PCT = float(os.getenv("MAX_PRICE_VARIANCE_PCT", "25.0"))

SANCTIONED_OR_BLOCKED_VENDORS = [
    "darkweb_supplies_ltd",
    "unverified_offshore_shell_llc",
    "fraud_test_vendor_99",
    "sanctioned_entity_corp"
]

# LangSmith Enterprise Agent Observability & Qwen3 Semantic Anti-Fraud
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY", "")
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2", "true")
LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT", "payguard-ai")
QWEN3_EMBEDDING_MODEL = "Qwen/Qwen3-Embedding-8B"
SUPPORTED_GLOBAL_LANGUAGES_COUNT = 105

# 20 Global Currencies with USD Conversion Rates for Accurate CFO Multi-Currency Accounting
GLOBAL_CURRENCY_RATES_TO_USD = {
    "USD": 1.00,
    "EUR": 1.08,
    "GBP": 1.29,
    "SAR": 0.2667,
    "AED": 0.2723,
    "EGP": 0.0204,
    "KWD": 3.25,
    "QAR": 0.2747,
    "MAD": 0.10,
    "CAD": 0.73,
    "AUD": 0.66,
    "JPY": 0.0067,
    "CNY": 0.14,
    "TRY": 0.029,
    "BRL": 0.18,
    "INR": 0.012,
    "RUB": 0.0105,
    "KRW": 0.00073,
    "IDR": 0.000064,
    "NGN": 0.00061,
}
