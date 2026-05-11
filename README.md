# 🏓 The Pong Game

Um remake do clássico **Pong**, desenvolvido em Python com o módulo **Turtle**.  
O jogo inclui movimento fluido, colisões, sistema de pontuação e condição de vitória: **o primeiro jogador a atingir 3 pontos vence**.

---

## 🎮 Comandos

| Jogador | Subir | Descer |
|--------|--------|---------|
| Esquerda | **W** | **S** |
| Direita | **Seta ↑** | **Seta ↓** |

---

## 🧩 Estrutura do Projeto

O projeto está organizado em quatro componentes principais:

- **Game Loop** — gere o movimento, colisões e fim do jogo  
- **Ball** — controla o movimento, rebotes e velocidade  
- **Paddle** — representa as raquetes e o seu movimento vertical  
- **Scoreboard** — mostra e atualiza a pontuação, incluindo o ecrã de Game Over  

---

## 🏁 Condição de Vitória

O jogo termina automaticamente quando:

- Algum jogador atinge **3 pontos**

Quando isso acontece, o ecrã exibe a mensagem **GAME OVER**.