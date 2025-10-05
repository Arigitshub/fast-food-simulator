# Setup Guide

Instructions for setting up the Fast Food Simulator project.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Arigitshub/fast-food-simulator.git
   cd fast-food-simulator
   ```

2. Install required dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Running the Simulator

To run the Fast Food Simulator with the integrated game loop:

```bash
python src/main.py
```

The main game loop in `src/main.py` integrates all game features including:

- Character customization
- Restaurant and restroom cleaning
- Trolley system
- Controller support

The game will continuously run and handle all events through the integrated loop until the player exits.

## Asset Folder Setup

The project uses an `assets/` directory structure to organize game resources:

### Directory Structure

```
assets/
├── audio/       # Sound effects and background music
└── images/      # Sprites, textures, and UI graphics
```

### Adding Assets

1. **Audio Files**: Place sound files (`.wav`, `.mp3`, `.ogg`) in `assets/audio/`
   - Background music
   - Sound effects for cleaning, trolley actions, etc.

2. **Image Files**: Place image files (`.png`, `.jpg`, `.bmp`) in `assets/images/`
   - Character sprites
   - Environment textures
   - UI elements

### Asset Notes

- The asset folders are initialized with `.gitkeep` files to maintain directory structure in version control
- Assets are loaded dynamically by the game loop
- Supported audio formats: WAV, MP3, OGG
- Supported image formats: PNG, JPG, BMP
- Keep file sizes reasonable for optimal game performance
- Use descriptive filenames (e.g., `character_walk.png`, `cleaning_sound.wav`)

## Project Structure

- `src/main.py` - Main entry point for the simulator with integrated game loop
- `src/cleaning.py` - Restaurant and restroom cleaning functions
- `src/customization.py` - Character customization features
- `src/trolley.py` - Trolley system for carrying boxes
- `src/controller_support.py` - Full controller support functionality
- `assets/` - Game assets (audio and images)
- `docs/` - Documentation files

## Features

- Restaurant Cleaning
- Restroom Cleaning
- Character Customization
- Trolley System for carrying boxes
- Full Controller Support
- Integrated Game Loop
- Day/night cycle
- Customer/employee AI
- Money/score system
- Real controller/gamepad integration

## Development

To contribute to the project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

See the LICENSE file for details.
