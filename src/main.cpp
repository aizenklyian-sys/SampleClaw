#include "Engine.hpp"
#include <iostream>

int main(int argc, char* argv[]) {
    SampleClaw::Engine engine("SampleClaw - Modernized 2D Platformer Engine", 1280, 720);

    if (!engine.Init()) {
        std::cerr << "Failed to initialize SampleClaw engine." << std::endl;
        return 1;
    }

    std::cout << "SampleClaw engine initialized successfully." << std::endl;
    engine.Run();

    return 0;
}
