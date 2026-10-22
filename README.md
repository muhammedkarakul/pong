# PONG

session: gemini --resume e82f637b-abd0-4542-942c-f1d0daaeed7e

# Pygame Learning Journey: Classic Pong
This project serves as a step-by-step implementation of the classic game **Pong** to master the fundamentals of 2D game development using Python and Pygame.
---

## 📚 Key Concepts Learned

### 1. The Game Loop Architecture
A video game functions similarly to a high-speed flipbook. The game loop repeats continuously (typically at 60 FPS) and consists of five core phases in
each frame:
1. **Event Polling:** Intercepting user inputs (keyboard, mouse, window controls).
2. **State & Physics Update:** Updating positions, velocities, and checking game logic.
3. **Screen Clearing:** Blanking out the display surface (`screen.fill((0, 0, 0))`) to prevent motion trails.
4. **Drawing (Rendering):** Drawing shapes and sprites onto the back buffer.
5. **Display Flipping:** Updating the actual display via double-buffering (`pygame.display.flip()`).

### 2. Pygame Coordinate System
Unlike standard Cartesian coordinates:
- The origin **`(0, 0)`** is situated at the **top-left corner** of the window.
- **X-axis:** Increases towards the **right**.
- **Y-axis:** Increases downwards towards the **bottom**.
- Screen center for an $800 \times 600$ viewport is at `(400, 300)`.

### 3. Input Handling
- **Discrete Events (`pygame.event.get()`):** Best for one-off occurrences (e.g., closing the window with `pygame.QUIT` or single-trigger actions like
      jumping).
- **Continuous Polling (`pygame.key.get_pressed()`):** Best for smooth, continuous actions (e.g., holding `W` or `S` to glide the paddle).

### 4. Entity Attributes & Movement Logic
Entities are modeled with distinct state properties:
- **Position & Dimensions:** `(x, y, width, height)`
- **Speed & Velocity Vectors:** Displacement step per frame (e.g., `paddle_y += paddle_speed`).
- **Boundary Clamping:** Restricting positions within screen boundaries (`0 <= y <= screen_height - paddle_height`) to prevent objects from moving
off-screen.

---

## 🚀 Current Milestone
- [x] Initialized Pygame engine and created display window ($800 \times 600$).
- [x] Implemented standard game loop with safe termination on window close.
- [x] Rendered player paddle surface using `pygame.draw.rect()`.
- [x] Configured continuous key bindings (`W`/`S`) for player paddle navigation.
- [ ] Implement boundary checking for the paddle.
- [ ] Add the ball entity with $(v_x, v_y)$ directional velocities and bounce mechanics.
- [ ] Implement opponent paddle (AI or 2-player controls).
- [ ] Add collision detection and score tracking.
