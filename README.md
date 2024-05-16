# Planet Orbit Simulation

This program is a simulation of the orbits of planets in our solar system. The user can run the program to see the orbits of the planets around the sun. The user can adjust the speed of the simulation by changing the value of the `TIMESTEP` constant in the `Planet` class.

The program uses the laws of gravity and motion to calculate the positions of the planets over time. The positions are stored in the `orbit` list of each planet, and are used to draw the path of the planet on the screen. The distance of each planet from the sun is also calculated and displayed on the screen.

## How to Run

To run this program, you need to have pygame installed. If you don't have it, you can install it by running `pip install pygame` in the command line.

Then, to run the program, run `python3 main.py` in the command line.

## Physics Equations

The program uses the following physics equations to calculate the positions of the planets over time:

The law of gravity states that every point mass attracts every other point mass by a force acting along the line intersecting both points. The force of gravity can be calculated using the following equation:

F = G \* (m1 \* m2) / r^2

where F is the force of gravity, G is the gravitational constant, m1 and m2 are the masses of the two objects, and r is the distance between them.

The acceleration of an object can be calculated using the following equation:

a = F / m

where a is the acceleration of the object, F is the force acting on it, and m is its mass.

The velocity of an object can be calculated using the following equation:

v = v0 + at

where v is the velocity of the object, v0 is its initial velocity, a is its acceleration, and t is the time.

The position of an object can be calculated using the following equation:

x = x0 + vt

where x is the position of the object, x0 is its initial position, v is its velocity, and t is the time.
<<<<<<<  f13e6a75-de18-4317-8b62-7b0ba0f7afcd  >>>>>>>
To use this program, run it and watch as the planets move around the sun. The user can adjust the speed of the simulation by changing the value of the `TIMESTEP` constant in the `Planet` class.

## Physics/Science Explanation

The program uses the laws of gravity and motion to calculate the positions of the planets over time. The law of gravity states that every point mass attracts every other point mass by a force acting along the line intersecting both points. The force of gravity is proportional to the product of the two masses and inversely proportional to the square of the distance between them.

The program also uses the laws of motion to calculate the positions of the planets over time. The laws of motion state that an object at rest will remain at rest, and an object in motion will continue to move, unless acted upon by an external force. The program uses this to calculate the velocity and position of each planet over time.

The program also uses the concept of time dilation to speed up or slow down the simulation. Time dilation is a concept in relativity that states that time passes more slowly for an observer in motion relative to a stationary observer. By increasing or decreasing the value of the `TIMESTEP` constant, the user can speed up or slow down the simulation.