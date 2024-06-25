import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
ORBIT_COLORS = [WHITE, YELLOW, BLUE, RED, DARK_GREY]

FONT = pygame.font.SysFont("comicsans", 16)


class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 250 / AU  # 1AU = 100 pixels
    TIMESTEP = 3600 * 24  # 1 day

    def __init__(self, x, y, radius, color, mass, name):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.name = name

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0
        self.orbit_count = 0
        self.previous_angle = None

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)

        pygame.draw.circle(win, self.color, (x, y), self.radius)

        if not self.sun:
            distance_text = FONT.render(f"{self.name}: {round(self.distance_to_sun / 1000, 1)}km", 1, WHITE)
            win.blit(distance_text, (x - distance_text.get_width() / 2, y - distance_text.get_height() / 2))

            velocity_text = FONT.render(f"Vx: {round(self.x_vel / 1000, 2)}km/s Vy: {round(self.y_vel / 1000, 2)}km/s", 1, WHITE)
            win.blit(velocity_text, (x - velocity_text.get_width() / 2, y - distance_text.get_height() / 2 + 20))

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets, speed_factor):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP * speed_factor
        self.y_vel += total_fy / self.mass * self.TIMESTEP * speed_factor

        self.x += self.x_vel * self.TIMESTEP * speed_factor
        self.y += self.y_vel * self.TIMESTEP * speed_factor
        self.orbit.append((self.x, self.y))

        # Check for orbit completion
        angle = math.atan2(self.y, self.x)
        if self.previous_angle is not None:
            if self.previous_angle < 0 and angle >= 0:
                self.orbit_count += 1
        self.previous_angle = angle


def create_starfield():
    stars = []
    for _ in range(200):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        stars.append((x, y))
    return stars


def draw_starfield(win, stars):
    for star in stars:
        win.fill(WHITE, (star[0], star[1], 2, 2))


def draw_information(win, planets, simulation_time, speed_factor):
    info_text = FONT.render(f"Simulation Time: {round(simulation_time / (3600 * 24), 2)} days", 1, WHITE)
    win.blit(info_text, (10, 10))

    speed_text = FONT.render(f"Speed Factor: {speed_factor}x", 1, WHITE)
    win.blit(speed_text, (10, 30))

    for i, planet in enumerate(planets):
        if not planet.sun:
            orbit_text = FONT.render(f"{planet.name} Orbits: {planet.orbit_count}", 1, WHITE)
            win.blit(orbit_text, (10, 50 + i * 20))


def main():
    run = True
    clock = pygame.time.Clock()

    stars = create_starfield()

    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10 ** 30, "Sun")
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10 ** 24, "Earth")
    earth.y_vel = 29.783 * 1000

    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10 ** 23, "Mars")
    mars.y_vel = 24.077 * 1000

    mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, 3.30 * 10 ** 23, "Mercury")
    mercury.y_vel = -47.4 * 1000

    venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10 ** 24, "Venus")
    venus.y_vel = -35.02 * 1000

    planets = [sun, earth, mars, mercury, venus]

    paused = False
    simulation_time = 0
    speed_factor = 1.0

    zoom_scale = 1.0

    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))
        draw_starfield(WIN, stars)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                    Planet.SCALE *= 1.1
                if event.key == pygame.K_MINUS:
                    Planet.SCALE /= 1.1
                if event.key == pygame.K_UP:
                    speed_factor *= 2
                if event.key == pygame.K_DOWN:
                    speed_factor /= 2

        if not paused:
            for planet in planets:
                planet.update_position(planets, speed_factor)
            simulation_time += Planet.TIMESTEP * speed_factor

        for planet in planets:
            planet.draw(WIN)

        draw_information(WIN, planets, simulation_time, speed_factor)

        pygame.display.update()

    pygame.quit()


main()
