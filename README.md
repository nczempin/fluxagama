# Fluxagama: 2D Vertical Shooter

## What Problem Does This Solve?
Fluxagama is a 2D vertical shooter game built with PyGame that provides an entertaining gaming experience while demonstrating game development principles in Python. It offers a classic arcade-style shooter experience with modern programming techniques.

## Who Is This For?
- Casual gamers looking for a retro-style vertical shooter
- Python developers interested in game development
- Students learning PyGame and game programming concepts
- Anyone interested in exploring open-source game development

## Current Implementation Status
- ✅ Player ship movement and controls
- ✅ Enemy spawning and basic AI
- ✅ Shooting mechanics
- ✅ Collision detection
- ✅ Basic sound effects
- ✅ Score tracking
- 🚧 Multiple weapon types
- 🚧 Boss enemies
- 📋 Level progression system
- 📋 Power-ups and upgrades

## Setup Instructions

### Prerequisites
- Python 3.x
- PyGame library
- Basic understanding of Python programming

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/nczempin/fluxagama.git
   cd fluxagama
   ```

2. Install PyGame if you don't have it already:
   ```
   pip install pygame
   ```

### Running the Game
1. Navigate to the source directory:
   ```
   cd src
   ```

2. Run the main game file:
   ```
   python -m fluxagama.fluxagama
   ```

## Project Scope

### What This IS
- A 2D vertical shooter game with classic arcade mechanics
- A demonstration of PyGame development techniques
- An open-source game project for learning and entertainment

### What This IS NOT
- Not a commercial-grade game with extensive features
- Not optimized for all platforms and screen sizes
- Not a complete game engine or framework

## Repository Structure
- `src/fluxagama/` - Main game source code
  - `fluxagama.py` - Main game loop and initialization
  - `PlayerShip.py` - Player ship class and controls
  - `Enemy.py` - Enemy ship classes and behaviors
  - `Shot.py` - Projectile mechanics
  - `FluxaSprite.py` - Base sprite class
  - `explosion.py` - Explosion effects
  - `sound.py` - Sound effect handling
  - `graphics.py` - Graphics utilities
  - `text.py` - Text rendering
  - `constants.py` - Game constants and configuration
- `tests/` - Test files for game components

## Controls
- Arrow keys: Move the player ship
- Space: Fire weapon
- Escape: Pause/Menu

## Play Online
You can play the game online at: http://nczempin.github.com/fluxagama/

## Development Status
This is an open-source game project in active development. Contributions and feedback are welcome.
