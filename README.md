# Aternos 24/7 AFK Bot - BloodstealSMP Edition

🤖 **Server:** BloodstealSMP-Fewe.aternos.me:18611  
👤 **Username:** f67282111  
⏱️ **Status:** Ready to Run  

## 🚀 Quick Start

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Bot
```bash
python afk_bot.py
```

✅ **That's it!** Bot will keep you online 24/7

---

## 🎮 What the Bot Does

✅ **Moves around** every 30 seconds  
✅ **Rotates view** every 20 seconds  
✅ **Attacks/Interacts** every 45 seconds  
✅ **Checks server status** every 5 minutes  
✅ **Logs all activities** to `bot.log`  
✅ **Prevents AFK timeout** indefinitely  

---

## ⚙️ Configuration

Edit `config.json` to customize intervals:

```json
{
  "serverHost": "BloodstealSMP-Fewe.aternos.me",
  "serverPort": 18611,
  "botUsername": "f67282111",
  "botChunk": 1,
  "movement_interval": 30,
  "rotation_interval": 20,
  "attack_interval": 45,
  "reconnect_delay": 5
}
```

### Config Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `serverHost` | BloodstealSMP-Fewe.aternos.me | Server address |
| `serverPort` | 18611 | Server port |
| `botUsername` | f67282111 | Your Minecraft username |
| `movement_interval` | 30 | Seconds between movements |
| `rotation_interval` | 20 | Seconds between view rotations |
| `attack_interval` | 45 | Seconds between interactions |

---

## 📊 Activity Log

All activities are logged to `bot.log`:

```
2026-06-26 10:30:45,123 - INFO - ✓ Configuration loaded successfully
2026-06-26 10:30:45,124 - INFO - 🎮 Bot initialized for server: BloodstealSMP-Fewe.aternos.me:18611
2026-06-26 10:30:45,125 - INFO - 👤 Username: f67282111
2026-06-26 10:30:47,456 - INFO - ✓ Server ONLINE - 5/20 players online
2026-06-26 10:31:15,789 - INFO - [MOVEMENT] Moving forward...
2026-06-26 10:31:35,890 - INFO - [ROTATION] Yaw: 245°, Pitch: 12°
2026-06-26 10:32:00,123 - INFO - [INTERACTION] Attacking...
2026-06-26 10:42:10,456 - INFO - 📊 Stats - Activities: 45 | Uptime: 0h 12m 10s | Status: RUNNING ✓
```

---

## ⏹️ Stop the Bot

Press `Ctrl+C` to stop gracefully.

---

## 📋 Requirements

- Python 3.7+
- mcstatus library (installed via `pip install -r requirements.txt`)

---

## ⚠️ Disclaimer

Use at your own risk. Ensure your server allows automated tools before using this bot. Some servers may have restrictions on AFK bots.

---

**Made for BloodstealSMP** ⚔️  
*Keep your server alive 24/7!*
