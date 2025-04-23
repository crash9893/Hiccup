import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
LOGS_DIR = PROJECT_ROOT / "logs"
TEMPLATES_DIR = PROJECT_ROOT / "templates"

# Create necessary directories
LOGS_DIR.mkdir(exist_ok=True)
TEMPLATES_DIR.mkdir(exist_ok=True)

# ScreenPipe settings
SCREENPIPE_CONFIG = {
    "default_confidence": 0.8,
    "screenshot_interval": 0.1,
    "max_screenshots": 100
}

# Terminator settings
TERMINATOR_CONFIG = {
    "move_duration": 0.5,
    "click_interval": 0.1,
    "type_interval": 0.1,
    "failsafe": True
}

# Logging settings
LOG_CONFIG = {
    "level": "INFO",
    "rotation": "500 MB",
    "retention": "10 days",
    "format": "{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
}

# Load environment variables
def load_env():
    """Load environment variables from .env file"""
    env_file = PROJECT_ROOT / ".env"
    if env_file.exists():
        with open(env_file) as f:
            for line in f:
                if line.strip() and not line.startswith("#"):
                    key, value = line.strip().split("=", 1)
                    os.environ[key] = value

# Initialize environment
load_env() 