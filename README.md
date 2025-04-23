# Hiccup - Desktop Automation Framework

Hiccup is a powerful desktop automation framework that combines screen analysis capabilities with precise input control. It uses ScreenPipe for screen capture and analysis, and Terminator for keyboard and mouse control.

## Features

- Screen capture and analysis
- Template matching for UI elements
- Precise mouse and keyboard control
- Configurable automation settings
- Comprehensive logging
- Failsafe mechanisms

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/hiccup.git
cd hiccup
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
hiccup/
├── core/           # Core application logic
├── screenpipe/     # Screen capture and analysis
├── terminator/     # Input control
├── config/         # Configuration files
├── logs/           # Application logs
├── templates/      # Template images for matching
└── commands/       # Automation commands
```

## Usage

1. Create a `.env` file in the project root (optional):
```
DEBUG=False
LOG_LEVEL=INFO
```

2. Run the application:
```bash
python core/app.py
```

## Components

### ScreenPipe
- Screen capture
- Template matching
- Image analysis
- Screenshot management

### Terminator
- Mouse control
- Keyboard input
- Hotkey support
- Input simulation

## Safety Features

- Failsafe mechanism (move mouse to corner to abort)
- Configurable delays between actions
- Error handling and logging
- Resource cleanup

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 