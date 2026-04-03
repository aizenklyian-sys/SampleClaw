#pragma once

#include <vector>
#include <memory>
#include <bitset>
#include <array>
#include <iostream>

namespace SampleClaw {

using EntityID = std::size_t;
const EntityID MAX_ENTITIES = 10000;

class Component {
public:
    virtual ~Component() = default;
};

using ComponentTypeID = std::size_t;

inline ComponentTypeID getUniqueComponentID() {
    static ComponentTypeID lastID = 0;
    return lastID++;
}

template <typename T>
inline ComponentTypeID getComponentTypeID() noexcept {
    static ComponentTypeID typeID = getUniqueComponentID();
    return typeID;
}

const std::size_t MAX_COMPONENTS = 32;
using ComponentBitset = std::bitset<MAX_COMPONENTS>;
using ComponentArray = std::array<Component*, MAX_COMPONENTS>;

class Entity {
public:
    Entity(EntityID id) : m_id(id), m_isActive(true) {}

    bool IsActive() const { return m_isActive; }
    void Destroy() { m_isActive = false; }

    template <typename T, typename... TArgs>
    T& AddComponent(TArgs&&... mArgs) {
        T* c(new T(std::forward<TArgs>(mArgs)...));
        m_components[getComponentTypeID<T>()] = c;
        m_componentBitset.set(getComponentTypeID<T>());
        return *c;
    }

    template <typename T>
    T& GetComponent() const {
        auto ptr(m_components[getComponentTypeID<T>()]);
        return *static_cast<T*>(ptr);
    }

    template <typename T>
    bool HasComponent() const {
        return m_componentBitset.test(getComponentTypeID<T>());
    }

private:
    EntityID m_id;
    bool m_isActive;
    ComponentArray m_components;
    ComponentBitset m_componentBitset;
};

class Manager {
public:
    void Update() {
        for (auto& e : m_entities) {
            // Update entities
        }
    }

    void Draw() {
        for (auto& e : m_entities) {
            // Draw entities
        }
    }

    void Refresh() {
        m_entities.erase(std::remove_if(m_entities.begin(), m_entities.end(),
            [](const std::unique_ptr<Entity>& mEntity) {
                return !mEntity->IsActive();
            }), m_entities.end());
    }

    Entity& AddEntity() {
        Entity* e = new Entity(m_entities.size());
        std::unique_ptr<Entity> uPtr{e};
        m_entities.emplace_back(std::move(uPtr));
        return *e;
    }

private:
    std::vector<std::unique_ptr<Entity>> m_entities;
};

} // namespace SampleClaw
