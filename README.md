# Conway's Game of Life (Python + Matplotlib)

```
.___________. __   _______  __       __  ___   ___  __  .______      
|           ||  | |   ____||  |     |  | \  \ /  / |  | |   _  \     
`---|  |----`|  | |  |__   |  |     |  |  \  V  /  |  | |  |_)  |    
    |  |     |  | |   __|  |  |     |  |   >   <   |  | |      /     
    |  |     |  | |  |____ |  `----.|  |  /  .  \  |  | |  |\  \----.
    |__|     |__| |_______||_______||__| /__/ \__\ |__| | _| `._____|
```

---

## 📖 Overview

This project is a simple implementation of **Conway's Game of Life** using **Python** and **Matplotlib**.  
It simulates cellular automata on a 2D grid where cells live, die, or reproduce based on their neighbors.  
The visualization is animated with `matplotlib.animation`.

---

## 🧬 Rules of the Game

1. **Underpopulation** – A live cell with fewer than 2 neighbors dies.  
2. **Overpopulation** – A live cell with more than 3 neighbors dies.  
3. **Survival** – A live cell with 2 or 3 neighbors stays alive.  
4. **Reproduction** – A dead cell with exactly 3 neighbors becomes alive.  

---

## 🚀 Features

- Random initial population of cells.
- Interactive **grid evolution** following Game of Life rules.
- Visualization powered by **Matplotlib Animation**.
- Automatically stops when the grid becomes empty.

---

## 📂 Project Structure

```
.
├── main.py         # Implementation of Conway's Game of Life
├── README.md       # Documentation
```

---

## 🛠️ Requirements

- Python 3.x
- Matplotlib

Install dependencies with:

```bash
pip install matplotlib
```

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

You’ll see the animated grid evolve based on the Game of Life rules.  

---

## 🎥 Demo

Cells are represented in a **binary grid** (`1 = alive`, `0 = dead`), and updated every tick.  

![Demo](https://upload.wikimedia.org/wikipedia/commons/e/e5/Gospers_glider_gun.gif)  
*(Example of Conway’s Game of Life)*

---

## 📌 Notes

- Grid size is currently fixed at **25×25**.
- Initial cells are populated randomly.
- Simulation stops when all cells die.

---

## 📜 License

This project is licensed under the **MIT License** – feel free to use, modify, and share.

---

✨ *A minimal yet fun project to visualize the beauty of cellular automata!*
