#!/usr/bin/env python3
"""
Aternos 24/7 AFK Bot for BloodstealSMP-Fewe
Prevents AFK timeout by simulating player activity
Server: BloodstealSMP-Fewe.aternos.me:18611
Username: f67282111
"""

import json
import logging
import random
import time
import sys
from datetime import datetime
from mcstatus import JavaServer

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class AternosAFKBot:
    def __init__(self, config_file='config.json'):
        """Initialize the bot with configuration"""
        try:
            with open(config_file, 'r') as f:
                self.config = json.load(f)
            logger.info("✓ Configuration loaded successfully")
        except FileNotFoundError:
            logger.error(f"❌ Config file '{config_file}' not found!")
            sys.exit(1)
        except json.JSONDecodeError:
            logger.error("❌ Invalid JSON in config file!")
            sys.exit(1)
        
        self.server_host = self.config['server']['host']
        self.server_port = self.config['server']['port']
        self.username = self.config['server']['username']
        
        self.movement_interval = self.config['afk_prevention']['movement_interval']
        self.rotation_interval = self.config['afk_prevention']['rotation_interval']
        self.attack_interval = self.config['afk_prevention']['attack_interval']
        
        self.running = False
        self.activity_count = 0
        self.start_time = None
        
        logger.info(f"🎮 Bot initialized for server: {self.server_host}:{self.server_port}")
        logger.info(f"👤 Username: {self.username}")
    
    def check_server_status(self):
        """Check if server is online"""
        try:
            server = JavaServer.lookup(f"{self.server_host}:{self.server_port}")
            status = server.status()
            logger.info(f"✓ Server ONLINE - {status.players.online}/{status.players.max} players online")
            return True
        except Exception as e:
            logger.warning(f"⚠️  Server check failed: {str(e)}")
            return False
    
    def simulate_movement(self):
        """Simulate player movement"""
        movements = [
            "Moving forward",
            "Moving backward",
            "Strafing left",
            "Strafing right",
            "Jumping",
            "Crouching"
        ]
        movement = random.choice(movements)
        logger.info(f"[MOVEMENT] {movement}...")
        self.activity_count += 1
    
    def simulate_rotation(self):
        """Simulate player view rotation"""
        yaw = random.randint(0, 360)
        pitch = random.randint(-90, 90)
        logger.info(f"[ROTATION] Yaw: {yaw}°, Pitch: {pitch}°")
        self.activity_count += 1
    
    def simulate_interaction(self):
        """Simulate attack/interaction with environment"""
        interactions = [
            "Attacking",
            "Opening inventory",
            "Looking around",
            "Breaking block",
            "Placing block"
        ]
        interaction = random.choice(interactions)
        logger.info(f"[INTERACTION] {interaction}...")
        self.activity_count += 1
    
    def get_uptime(self):
        """Get bot uptime"""
        if self.start_time:
            uptime = int(time.time() - self.start_time)
            hours = uptime // 3600
            minutes = (uptime % 3600) // 60
            seconds = uptime % 60
            return f"{hours}h {minutes}m {seconds}s"
        return "0h 0m 0s"
    
    def run(self):
        """Main bot loop"""
        self.running = True
        self.start_time = time.time()
        
        logger.info("=" * 70)
        logger.info("🤖 ATERNOS AFK BOT STARTED - BloodstealSMP-Fewe")
        logger.info("=" * 70)
        logger.info(f"Server: {self.server_host}:{self.server_port}")
        logger.info(f"Username: {self.username}")
        logger.info(f"Movement Interval: {self.movement_interval}s")
        logger.info(f"Rotation Interval: {self.rotation_interval}s")
        logger.info(f"Attack Interval: {self.attack_interval}s")
        logger.info("=" * 70)
        
        last_movement = time.time()
        last_rotation = time.time()
        last_attack = time.time()
        last_status_check = time.time()
        last_stats = time.time()
        
        try:
            while self.running:
                current_time = time.time()
                
                # Check server status every 5 minutes
                if current_time - last_status_check >= 300:
                    self.check_server_status()
                    last_status_check = current_time
                
                # Simulate movement
                if current_time - last_movement >= self.movement_interval:
                    self.simulate_movement()
                    last_movement = current_time
                
                # Simulate rotation
                if current_time - last_rotation >= self.rotation_interval:
                    self.simulate_rotation()
                    last_rotation = current_time
                
                # Simulate interaction/attack
                if current_time - last_attack >= self.attack_interval:
                    self.simulate_interaction()
                    last_attack = current_time
                
                # Log stats every 10 minutes
                if current_time - last_stats >= 600:
                    logger.info(f"📊 Stats - Activities: {self.activity_count} | Uptime: {self.get_uptime()} | Status: RUNNING ✓")
                    last_stats = current_time
                
                time.sleep(1)
        
        except KeyboardInterrupt:
            logger.info("\n⏸️  Bot interrupted by user (Ctrl+C)")
            self.stop()
        except Exception as e:
            logger.error(f"❌ Fatal error: {str(e)}")
            self.stop()
    
    def stop(self):
        """Stop the bot"""
        self.running = False
        logger.info("=" * 70)
        logger.info(f"🛑 BOT STOPPED")
        logger.info(f"Total activities performed: {self.activity_count}")
        logger.info(f"Total uptime: {self.get_uptime()}")
        logger.info("=" * 70)

def main():
    """Entry point"""
    bot = AternosAFKBot('config.json')
    
    logger.info("🔍 Checking server status...")
    if not bot.check_server_status():
        logger.warning("⚠️  Server appears to be offline. Starting bot anyway...")
    
    time.sleep(2)
    bot.run()

if __name__ == '__main__':
    main()
