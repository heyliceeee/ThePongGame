# 🏓 Pong Game  
A recreation of the classic Pong in Python using the **turtle** module, with separate classes for organization: **Ball**, **Paddle**, and **Scoreboard**.  
The goal is simple: prevent the ball from passing your paddle and score points until you win.

---

## 🎯 Purpose  
Create a modular, object‑oriented version of the Pong game, featuring smooth animations, collision detection, a scoring system, and a win condition for the first player to reach **3 points**.

---

## 🧩 Project Structure  
- **Ball** — controls ball movement, bouncing, and speed  
- **Paddle** — represents the paddles and their vertical movement  
- **Scoreboard** — displays and updates the score, including the game‑over screen  
- **main.py** — contains the main game loop, collision detection, and win logic  

---

## 🚀 Features  
- Smooth ball movement using manual screen updates (`screen.tracer(0)`)  
- Wall and paddle collision detection  
- Progressive ball speed increase after each hit  
- Scoring system for both players  
- Game ends when a player reaches 3 points  
- **GAME OVER** message displayed at the center of the screen  

---

## 🎮 Controls  
- **W** → move left paddle up  
- **S** → move left paddle down  
- **Up Arrow** → move right paddle up  
- **Down Arrow** → move right paddle down  

---

## 🧠 Concepts Practiced  
- Object‑Oriented Programming (OOP)  
- Class inheritance (`Ball`, `Paddle`, and `Scoreboard` inherit from `Turtle`)  
- Animation with `screen.tracer()`  
- Collision detection  
- Speed and direction management  
- Game loops  
- Code modularization  
