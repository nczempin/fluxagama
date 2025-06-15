# Fluxagama: 2D Vertical Shooter

> **🗄️ Archived Project**: This was a learning project for my kids when they were getting into programming. It's no longer actively developed, but kept here for nostalgia. One of them is a game developer now (though probably not because of this 😄).

A simple Space Invaders-style game built with PyGame. It's intentionally basic - perfect for learning game development concepts.

## What's Implemented

- ✅ Player ship movement and shooting
- ✅ Static enemy formations
- ✅ Collision detection (shoot the enemies!)
- ✅ Score tracking
- ✅ Sound effects
- ✅ Basic explosion graphics

## What's NOT Implemented

The enemies don't move or shoot back - they just sit there waiting to be destroyed. Think of it as a shooting gallery in space. All those GitHub issues from 2012? Those were meant as exercises we never got around to.

## Quick Start

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the game:
   ```
   make run
   ```
   or
   ```
   python -m fluxagama.fluxagama
   ```

## Controls

- **A/D** or **Arrow Keys**: Move left/right
- **Space**: Shoot
- **Escape**: Exit game
- **E**: Debug feature (manual enemy shot)

## Development

Run `make` to install dependencies, run linters and tests, and build a wheel.

## Repository Structure

- `src/fluxagama/` - Game source code
- `data/` - Game assets (sprites and sounds)
- `tests/` - Test files
- `scripts/` - Setup scripts

---

*Originally created as an educational project around 2012.*