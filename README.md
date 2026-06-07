# Black Hole Simulator

A real-time N-body gravitational simulator built in Python.
Implements Newtonian gravity (F = Gm₁m₂/r²) with Euler integration.

## Physics
- Gravitational force computed between every pair of bodies each frame
- Time step: 36000 simulated seconds per frame

## Features (current)
- 3-body orbit simulation
- Scalable coordinate system (1 pixel = 1,000,000 km)

## Planned
- N-body multi-object simulation
- Gravitational lensing approximation
- Interactive body placement
- Implement Schwarzschild radius visualised: R = 2GM/c²

## Stack
Python · Pygame · No external ML/data libraries

## Run
pip install pygame
python main.py

![alt text](image-1.png)