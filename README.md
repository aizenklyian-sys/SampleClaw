# SampleClaw

**SampleClaw** is a modernized 2D platformer engine inspired by the **OpenClaw** project (a reimplementation of the 1997 classic "Captain Claw").

## Key Features

- **Modern C++ Architecture**: Built with C++17, focusing on clean code, safety, and performance.
- **Entity Component System (ECS)**: A robust ECS for managing game entities and behaviors.
- **Cross-Platform Support**: Built using SDL2, ensuring compatibility with Windows, Linux, and macOS.
- **Modular Design**: Separates core engine logic, graphics, physics, and audio for easy extension.
- **Modern Rendering**: Supports high-resolution displays and widescreen aspect ratios.

## Getting Started

### Prerequisites

To build SampleClaw, you will need:

- A C++17 compatible compiler (GCC, Clang, or MSVC)
- CMake 3.15 or higher
- SDL2, SDL2_image, SDL2_mixer, and SDL2_ttf development libraries

### Building

```bash
mkdir build
cd build
cmake ..
make
```

### Running

```bash
./SampleClaw
```

## Project Structure

- `include/`: Header files for the engine and ECS.
- `src/`: Implementation files for the engine core and main entry point.
- `assets/`: Directory for game assets (textures, sounds, etc.).
- `cmake/`: Custom CMake modules.

## Acknowledgments

This project is inspired by the original [OpenClaw](https://github.com/pjasicek/OpenClaw) reimplementation of Captain Claw.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
