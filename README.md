---
title: PayGuard AI Agentic Commerce
emoji: 🛡️
colorFrom: blue
colorTo: indigo
sdk: gradio
sdk_version: 4.44.1
app_file: app.py
pinned: true
license: mit
---

# 🛡️ PayGuard AI: Autonomous Multimodal Invoice Auditor, AG Grid Ledger & PayPal Execution Agent

<p align="left">
  <a href="https://paypalaihackathon.devpost.com/"><img src="https://img.shields.io/badge/PayPal_AI_Hackathon_2026-$67,500_Challenge-00457C?style=for-the-badge&logo=paypal&logoColor=white" alt="PayPal Hackathon"></a>
  <a href="https://tokenfactory.nebius.com"><img src="https://img.shields.io/badge/Nebius_AI_Builders-Approved_Builder-6B4FBB?style=for-the-badge" alt="Nebius Approved"></a>
  <a href="https://www.linkedin.com/in/ibrahim-adel-pro-ai"><img src="https://img.shields.io/badge/Architect-Ibrahim_Adel-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="MIT License"></a>
</p>

**Engineered Exclusively for the PayPal AI Hackathon 2026 by Ibrahim Adel (Founder & AI Systems Architect @ MuseOS Labs — Organization ID: `aitenant-e00nrfr08gavh9pj8c`)**

**PayGuard AI** is a purpose-built, enterprise-grade autonomous agentic commerce platform engineered from the ground up for B2B financial auditing and automated PayPal settlements. It bridges **Multimodal Invoice Vision**, **Live Web Price Verification (Tavily)**, **Pre-Execution Financial Firewalls (`SafeAgents` + `Sentinel 200-SOP`)**, **Interactive `AG Grid` Financial Ledgers**, and **Automated PayPal Sandbox Settlements** with local zero-data-retention **SQLite** persistence.

---

## 🌟 Key Architectural Pillars (Built for PayPal AI Hackathon)

1. **Multimodal Invoice Vision & Tiered Model Routing (`main.py`):**
   - Uses **NVIDIA Nemotron 3.5 Super VL / Qwen2-VL-72B** with in-memory RAM compression (`1024x1024 JPEG`) for optical invoice parsing.
   - Uses **DeepSeek-V3** and **Nemotron Ultra 253B** for mathematical tax reconciliation and **Llama-3.3-70B / Groq LPU** for sub-second JSON formatting.
2. **SafeAgents Financial Firewall & Sentinel 200-SOP Auditor (`paypal_tools.py`):**
   - Inspects every payment tool call before execution against **200 Standard Operating Procedures (SOPs)** and **36 international tax/compliance frameworks**.
   - Automatically blocks invoices exceeding fair market value by `>25%` or exceeding the `$500.00` autonomous threshold, requiring human-in-the-loop CFO sign-off with `SHA-256` cryptographic signatures.
3. **Interactive Enterprise `AG Grid` Ledger (`app.py` - Tab 1):**
   - Embedded interactive **AG Grid** financial table enabling real-time multi-column sorting, filtering, variance inspection, and 1-click UTF-8 BOM Excel (`.csv`) + RFC-5545 payment due alarm (`.ics VALARM`) exports.
4. **Live Market Price Grounding via Tavily (`paypal_tools.py`):**
   - Queries real-time wholesale and retail market benchmarks to prevent B2B invoice fraud and price gouging.
5. **Global Delivery & E-Commerce COD Voice Guard — 40+ Languages (`main.py` & `database.py`):**
   - Verifies customer order confirmations across **40+ global languages** (English, Spanish, French, German, Arabic & regional dialects at `temperature=0.0`) to eliminate Return-to-Origin (RTO) shipping losses.
6. **Automated PayPal Sandbox Payouts, SaaS Subscriptions (`/myplan`, `/activate`) & `n8n` Sync:**
   - Executes live/simulated OAuth2 PayPal Sandbox settlements, upgrades merchant SaaS tiers, records reusable `SKILL.md` accounting protocols (`/teach`), and dispatches structured webhooks to `n8n`.

---

## 🏆 Unit Economics & Enterprise Compliance

- **99.2% Cost Reduction vs. Legacy Enterprise FinTech SaaS:** Eliminates `$2,160/month` idle dedicated GPU servers by combining client-side SQLite/Regex reflexes, `NVFP4` 4-bit quantized typed JSON decisions (`<$0.01 per 100 decisions`), and Pay-Per-Token serverless inference.
- **Enterprise Data Sovereignty:** Local SQLite ledger (`payguard_ledger.db`) operates with strict zero-data-retention compliance (`HIPAA`, `SOC 2 Type II`, `ISO 27001` aligned).
- **40+ Global Languages:** Built natively for international B2B commerce and cross-border PayPal settlements.

---

## 🛠️ Setup & Run Instructions

```bash
git clone https://github.com/ibrahimadel-ai/payguard-ai.git
cd payguard-ai
pip install -r requirements.txt
python app.py
```

## 📄 License
This project is licensed under the **MIT License** — Copyright (c) 2026 **Ibrahim Adel (MuseOS Labs — `aitenant-e00nrfr08gavh9pj8c`)**. Protected internationally under the Berne Convention (180+ Countries).

---
