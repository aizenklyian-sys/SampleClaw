#pragma once

#include <SDL2/SDL.h>
#include <string>
#include <memory>

namespace SampleClaw {

class Engine {
public:
    Engine(const std::string& title, int width, int height);
    ~Engine();

    bool Init();
    void Run();
    void Stop();

private:
    void ProcessInput();
    void Update(float deltaTime);
    void Render();

    std::string m_title;
    int m_width;
    int m_height;
    bool m_isRunning;

    SDL_Window* m_window;
    SDL_Renderer* m_renderer;
};

} // namespace SampleClaw
