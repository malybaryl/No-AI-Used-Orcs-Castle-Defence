# No AI Used Orcs Castle Defence

## About The Project

This is a classic 2D arcade-style castle defense game built with Pygame. Players must defend their castle from waves of invading orcs that descend from the top of the screen. The orcs follow a predefined path and will shoot back at the player.

As the repository name suggests, this project was developed without the use of AI for code generation.

## Gameplay

Your mission is to stop the orcs from reaching the bottom of the screen. Move your character left and right to dodge enemy projectiles and position your shots to eliminate the invaders. The game ends if an orc reaches your defense line or if your character is hit by an enemy projectile.

![Game screenshot](/screenshots/0.png)

### Controls

*   **Move Left:** `Left Arrow` key
*   **Move Right:** `Right Arrow` key
*   **Shoot:** `Spacebar`

## Getting Started

You can either run the game from the source code or download a pre-built executable from the releases page.

### Running from Source

To run the game from its source code, you will need Python and the dependencies listed in `requirements.txt`.

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/malybaryl/No-AI-Used-Orcs-Castle-Defence.git
    cd No-AI-Used-Orcs-Castle-Defence
    ```

2.  **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3.  **Run the game:**
    ```sh
    python main.py
    ```

### Releases

Pre-built executables for Windows and Linux are automatically generated for each release. You can download the latest version from the [**Releases**](https://github.com/malybaryl/No-AI-Used-Orcs-Castle-Defence/releases) page.

## Building from Source

You can create your own executable using PyInstaller.

1.  Ensure you have installed the project dependencies, including `pyinstaller`.
2.  Run the following command from the project's root directory:
    ```sh
    pyinstaller --onefile --nowindowed main.py
    ```
3.  The executable will be located in the `dist` directory. You will need to copy the `assets` folder into the `dist` directory for the game to run correctly.

## File Structure

```
.
├── .github
│   └── workflows
│       └── build-executables.yml # Github Actions relase build Linux & Windows
├── assets
│   └── images                # Sprites used in game
│       ├── backgrouds
│       │   └──  0.png
│       ├── enemy
│       │   ├──   0.png
│       │   ├──   1.png
│       │   └──   2.png
│       ├── enemyProtectile
│       │   └──  0.png
│       ├── player
│       │   ├──   0.png
│       │   ├──   1.png
│       │   ├──   2.png
│       │   ├──   3.png
│       │   └──   4.png
│       └── player
│           └──  0.png
├── screenshots               # Screnshots used in README.md
│   └── 0.png                
├── src                       # Source code
│   ├── core                
│   │   ├──   __init__.py
│   │   ├──   AssetsLoader.py       # Class AssetsLoader helps with loadnig sprites
│   │   ├──   conts.py              # Conts variables used across whole code
│   │   ├──   EnemyManager.py       # Class EnemyManager controls spawn of enemies
│   │   └──   singleton.py          # Definition for signleton decorator
│   ├── entities                
│   │   ├──   enemies
│   │   │     ├──   __init__.py
│   │   │     └──   Enemy.py        # Enemy class
│   │   ├──   player
│   │   │     ├──   __init__.py
│   │   │     └──   Player.py       # Player class
│   │   ├──   protectiles
│   │   │     ├──   __init__.py
│   │   │     └──   Bullet.py       # Bullet class
│   │   ├──   __init__.py
│   │   ├──   Entity.py             # Base class for entities like objects or end zones
│   │   └──   LivingEntity.py       # Base class for living entities like player or enemies
│   └── ui                
├── .gitignore                # Github gitignore files
├── build.spec                # File used for build executable files
├── main.py                   # Main script initialing game
├── README.md                 # README.md file
└── requirements.txt          # Libraries used by code
```
