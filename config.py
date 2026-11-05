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

"""
PayGuard AI — Autonomous Multimodal Financial Auditing & Agentic Commerce Engine
Built for the PayPal AI Hackathon 2026 ($67,500 Challenge)
Target Prizes: 1st Place ($12,000) + Best Use of Agentic Commerce ($5,000) + Best Use of AG Grid ($5,000) + Render ($2,250)
Author: Ibrahim Adel (AI Systems Architect & Founder @ MuseOS Labs)
Organization Credential ID: aitenant-e00nrfr08gavh9pj8c
"""
import os

# Core AI & Inference Endpoints
NEBIUS_API_KEY = os.getenv("NEBIUS_API_KEY", "").strip()
NEBIUS_BASE_URL = os.getenv("NEBIUS_BASE_URL", "https://api.tokenfactory.nebius.com/v1").strip()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()  # Groq LPU high-speed fallback
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "").strip()

# PayPal Agentic Commerce & Sandbox Credentials
PAYPAL_CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID", "PayPal-Sandbox-Agentic-Client-2026").strip()
PAYPAL_CLIENT_SECRET = os.getenv("PAYPAL_CLIENT_SECRET", "").strip()
PAYPAL_MODE = os.getenv("PAYPAL_MODE", "sandbox").strip()

# n8n Accounting Automation Webhook
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL", "https://n8n.museos.labs/webhook/paypal-reconcile").strip()

# Telegram Bot Gateway
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()

# LangSmith Observability
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY", "").strip()
LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT", "PayGuard-AI").strip()

# Tiered Model Routing Matrix (Including Nemotron 3.5 Super VL, DeepSeek, Qwen, Llama)
PRIMARY_REASONING_MODEL = "nvidia/Llama-3_1-Nemotron-Ultra-253B-v1"
MATH_AUDIT_MODEL = "deepseek-ai/DeepSeek-V3"
VISION_AUDIT_MODEL = "nvidia/Nemotron-3.5-Super-VL"
VISION_FALLBACK_MODEL = "Qwen/Qwen2-VL-72B-Instruct"
FAST_DECISION_MODEL = "meta-llama/Llama-3.3-70B-Instruct"
GROQ_FALLBACK_MODEL = "llama-3.3-70b-versatile"

# SafeAgents Financial Firewall & Sentinel SOP Compliance Thresholds
MAX_AUTO_APPROVE_USD = 500.00
PRICE_INFLATION_ALERT_PCT = 25.0  # Flag invoices >25% above live market price
SENTINEL_SOP_FRAMEWORKS = 36
SENTINEL_SOP_CHECKS = 200
DB_PATH = os.getenv("PAYGUARD_DB_PATH", "/tmp/payguard_ledger.db")


# Ultimate Sovereign Mix Additions (PayPal 1st Place Secret Weapons)
SOVEREIGN_FINTECH_MODEL = "MuseOS-Labs/PayGuard-Sovereign-FinTech-12B-NVFP4"
TYPED_DECISION_FLASH_MODEL = "THUDM/glm-4-9b-chat"  # Ultra-low-cost typed JSON decision engine (<$0.01 / 100 decisions)
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", "").strip()
ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID", "21m00Tcm4TlvDq8ikWAM").strip()
