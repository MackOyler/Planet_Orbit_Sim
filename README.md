# Planet Orbit Simulation

## Overview
`Planet_Orbit_Sim` is a simulation of planetary orbits around the sun, demonstrating the principles of gravitational physics. This project utilizes Python and Pygame to create a visual representation of celestial bodies interacting under gravitational forces.

### Features
- Simulates the orbit of planets around the sun.
- Real-time calculation of gravitational forces and planetary positions.
- Visual display of orbital paths and distances from the sun.
- Includes Earth, Mars, Mercury, Venus, and the Sun in the simulation.

### Physics Explanation
The simulation models the gravitational attraction between celestial bodies using Newton's Law of Universal Gravitation:
$$
F = \frac{G \cdot m_1 \cdot m_2}{r^2}
$$
Where:
- \( F \) is the gravitational force between two bodies.
- \( G \) is the gravitational constant, \( G = 6.67428 \times 10^{-11} \text{ N m}^2/\text{kg}^2 \).
- \( m_1 \) and \( m_2 \) are the masses of the bodies.
- \( r \) is the distance between the centers of the masses.

Each planet's position and velocity are updated iteratively, taking into account the gravitational forces exerted by other planets and the sun.


## Installation
Ensure you have Python and Pygame installed on your system.

1. **Install Pygame:**
   ```bash
   pip install pygame
