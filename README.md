# Real Physics

A small gravity/orbital-mechanics sandbox. `Objects.py` defines `MecaPt` ("mechanical point"), a body with mass, velocity, and radius that computes gravitational forces and vectors toward other bodies (default radius is set to the Moon's, `1737.4 km`, suggesting an orbital simulation). `UI.py` renders the simulation with pygame.

## Requirements
```
pip install pygame numpy
```

## Running it
```
python UI.py
```
