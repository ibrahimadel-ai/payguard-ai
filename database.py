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
import sqlite3
import datetime
import hashlib
import json
import os

DB_PATH = os.getenv("PAYGUARD_DB_PATH", "/tmp/payguard_ledger.db")

def init_payguard_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS invoices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            invoice_number TEXT,
            vendor_name TEXT,
            amount_usd REAL,
            currency TEXT,
            tax_usd REAL,
            items_summary TEXT,
            semantic_hash TEXT,
            firewall_status TEXT,
            firewall_reason TEXT,
            paypal_order_id TEXT,
            paypal_status TEXT,
            created_at TEXT
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS cod_orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            customer_message TEXT,
            detected_language TEXT,
            order_total_usd REAL,
            deposit_usd REAL,
            risk_score INTEGER,
            paypal_deposit_id TEXT,
            ai_reply TEXT,
            created_at TEXT
        )
    """)
    conn.commit()

    c.execute("SELECT COUNT(*) FROM invoices")
    if c.fetchone()[0] == 0:
        now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        seed_rows = [
            ("INV-2026-8801", "Nebius Cloud GPU Cluster Ltd", 420.00, "USD", 42.00, "Serverless Enterprise AI Inference Credits", hashlib.sha256(b"INV-2026-8801").hexdigest()[:16], "APPROVED (5/5 Gates)", "Passed 200-SOP & Market Benchmark", "PAYPAL-SBX-99201A", "COMPLETED", now),
            ("INV-2026-8802", "Global Logistics & Freight Co", 310.50, "EUR", 31.05, "Cross-Border Express Air Cargo", hashlib.sha256(b"INV-2026-8802").hexdigest()[:16], "APPROVED (5/5 Gates)", "Verified VAT & Fair Market Price", "PAYPAL-SBX-99202B", "COMPLETED", now),
            ("INV-2026-8803", "Unverified_Offshore_Shell_LLC", 4850.00, "USD", 0.00, "Unlisted Consulting Services", hashlib.sha256(b"INV-2026-8803").hexdigest()[:16], "BLOCKED (Gate 2 & 3)", "Vendor on Sanction List & Exceeds $500 Auto-Cap", "BLOCKED-BY-SAFEAGENTS", "HELD_FOR_CFO", now),
        ]
        c.executemany("""
            INSERT INTO invoices (
                invoice_number, vendor_name, amount_usd, currency, tax_usd,
                items_summary, semantic_hash, firewall_status, firewall_reason,
                paypal_order_id, paypal_status, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, seed_rows)
        conn.commit()
    conn.close()

def compute_invoice_fingerprint(invoice_number, vendor_name, amount_usd):
    raw = f"{str(invoice_number).strip().lower()}|{str(vendor_name).strip().lower()}|{float(amount_usd):.2f}"
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]

def check_duplicate_invoice(invoice_number, vendor_name, amount_usd):
    init_payguard_db()
    fp = compute_invoice_fingerprint(invoice_number, vendor_name, amount_usd)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, paypal_order_id FROM invoices WHERE invoice_number = ? OR semantic_hash = ?", (invoice_number, fp))
    row = c.fetchone()
    conn.close()
    return (True, row[1]) if row else (False, None)

def record_invoice_audit(invoice_number, vendor_name, amount_usd, currency, tax_usd, items_summary, firewall_status, firewall_reason, paypal_order_id, paypal_status):
    init_payguard_db()
    fp = compute_invoice_fingerprint(invoice_number, vendor_name, amount_usd)
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM invoices WHERE invoice_number = ?", (invoice_number,))
    c.execute("""
        INSERT INTO invoices (
            invoice_number, vendor_name, amount_usd, currency, tax_usd,
            items_summary, semantic_hash, firewall_status, firewall_reason,
            paypal_order_id, paypal_status, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (invoice_number, vendor_name, float(amount_usd), currency, float(tax_usd), items_summary, fp, firewall_status, firewall_reason, paypal_order_id, paypal_status, now))
    conn.commit()
    conn.close()

def fetch_all_invoices():
    init_payguard_db()
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        SELECT invoice_number, vendor_name, amount_usd, currency, tax_usd,
               firewall_status, paypal_order_id, paypal_status, created_at
        FROM invoices ORDER BY id DESC
    """)
    rows = c.fetchall()
    conn.close()
    return rows
