# Sample code

import sqlite3
import os
import random
import time
from datetime import datetime, timezone

# --- CONFIGURATION ---
# Target Directory for the evidence
EVIDENCE_DIR = "../evidence/discord"
DB_NAME = "messages.db"
DB_PATH = os.path.join(EVIDENCE_DIR, DB_NAME)

# Suspect ID (John Smith)
SUSPECT_ID = "456123789"
VICTIM_NAME = "Jane Doe"

# --- MOCK DATA ---
# Normal conversations to create "noise"
NORMAL_CHATS = [
    "Anyone up for a game?",
    "Did you see the homework for Math?",
    "Lol that was funny",
    "I'm heading out, cya later",
    "Can you send me the link?",
    "My connection is lagging so bad",
    "gg wp",
    "What time is the event starting?",
]

# Incriminating evidence (The "Smoking Gun")
# Timestamps in October 2025
EVIDENCE_CHATS = [
    (1728230400000, "I can't stand Jane Doe, she's so annoying."),  # Oct 6, 2025
    (1728835200000, "Just wait until everyone sees this meme I made about her."), # Oct 13, 2025
    (1728921600000, "It's going to ruin her reputation. She is so stupid."), # Oct 14, 2025
    (1729440000000, "Check out this video: meme_final.mp4"), # Oct 20, 2025
    (1729526400000, "She actually cried in class today. Mission accomplished."), # Oct 21, 2025
]

def create_database():
    # Ensure directory exists
    os.makedirs(EVIDENCE_DIR, exist_ok=True)
    
    # Remove old DB if it exists to start fresh
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create table matching Discord's schema (simplified)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp INTEGER,
            author_id TEXT,
            channel_id TEXT,
            content TEXT,
            attachments TEXT
        )
    ''')
    
    print(f"[*] Database initialized at {DB_PATH}")
    return conn

def populate_data(conn):
    cursor = conn.cursor()
    
    # 1. Generate Noise (Random dates in Sept/Oct 2025)
    print("[*] Generating background noise...")
    start_ts = 1725148800000 # Sept 1, 2025
    end_ts = 1730419199000   # Oct 31, 2025
    
    for _ in range(500): # 500 random messages
        ts = random.randint(start_ts, end_ts)
        author = random.choice(["111222333", "999888777", SUSPECT_ID, "555666444"])
        content = random.choice(NORMAL_CHATS)
        cursor.execute("INSERT INTO messages (timestamp, author_id, channel_id, content, attachments) VALUES (?, ?, ?, ?, ?)",
                       (ts, author, "GENERAL_CHANNEL", content, ""))

    # 2. Insert The Evidence
    print("[*] Planting evidence...")
    for ts, content in EVIDENCE_CHATS:
        # 50% chance to have an attachment string if it mentions "video"
        attachment = "meme_final.mp4" if "mp4" in content else ""
        
        cursor.execute("INSERT INTO messages (timestamp, author_id, channel_id, content, attachments) VALUES (?, ?, ?, ?, ?)",
                       (ts, SUSPECT_ID, "SECRET_CHANNEL", content, attachment))
        
    conn.commit()
    print(f"[*] Successfully inserted {500 + len(EVIDENCE_CHATS)} messages.")

if __name__ == "__main__":
    conn = create_database()
    populate_data(conn)
    conn.close()
    print("✅ MOCK EVIDENCE GENERATION COMPLETE.")
