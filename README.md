# Real Physics

A small sandbox for gravity and orbital mechanics. `Objects.py` defines `MecaPt` ("mechanical point"), a body with mass, velocity, and radius that computes gravitational forces and vectors toward other bodies (its default radius is set to that of the Moon, `1737.4 km`, which suggests an orbital simulation). `UI.py` renders the simulation with pygame.

## Requirements
```
pip install pygame numpy
```

## Running it
```
python UI.py
```
