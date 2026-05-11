# 🏓 Pong Game  
Uma recriação do clássico Pong em Python usando o módulo **turtle**, com classes separadas para organização: **Ball**, **Paddle** e **Scoreboard**.  
O objetivo é simples: impedir que a bola passe pelo teu paddle e marcar pontos até atingir a vitória.

---

## 🎯 Objetivo  
Criar uma versão modular e orientada a objetos do jogo Pong, com animações suaves, deteção de colisões, sistema de pontuação e condição de vitória para o primeiro jogador a atingir **3 pontos**.

---

## 🧩 Estrutura do Projeto  
- **Ball** – controla o movimento da bola, rebotes e velocidade  
- **Paddle** – representa as raquetes e o seu movimento vertical  
- **Scoreboard** – mostra e atualiza a pontuação, incluindo o ecrã de fim de jogo  
- **main.py** – contém o loop principal do jogo, deteção de colisões e lógica de vitória

---

## 🚀 Funcionalidades  
- Movimento fluido da bola com atualização manual do ecrã (`screen.tracer(0)`)  
- Rebotes nas paredes e nos paddles  
- Aceleração progressiva da bola após cada colisão  
- Sistema de pontuação para ambos os jogadores  
- Fim de jogo quando um jogador atinge 3 pontos  
- Mensagem de **GAME OVER** exibida no centro do ecrã  

---

## 🎮 Controlo do Jogo  
- **W** → mover paddle esquerdo para cima (raquete esquerda)
- **S** → mover paddle esquerdo para baixo (raquete esquerda)
- **Seta ↑** → mover paddle direito para cima (raquete direita)
- **Seta ↓** → mover paddle direito para baixo (raquete direita)

---

## 🧠 Conceitos Praticados  
- Programação orientada a objetos (OOP)  
- Herança de classes (`Ball`, `Paddle` e `Scoreboard` herdam de `Turtle`)  
- Animação com `screen.tracer()`  
- Deteção de colisões  
- Gestão de velocidade e direção  
- Loops de jogo  
- Modularização de código  
