import pygame, pymunk

class Walls():
    def __init__(self):
        self.color = (95, 99, 102)
        self.ground_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.ground_body.position = 0, 700
        self.ground_shape = pymunk.Poly.create_box(self.ground_body, (10000, 60))
        self.ground_shape.friction = 1
        self.ground_shape.collision_type = 1

        self.left_wall_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.left_wall_body.position = 0, 0
        self.left_wall_shape = pymunk.Poly.create_box(self.left_wall_body, (60, 1500))
        self.left_wall_shape.friction = 1

        self.right_wall_body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.right_wall_body.position = 3700, 0
        self.right_wall_shape = pymunk.Poly.create_box(self.right_wall_body, (60, 1500))
        self.right_wall_shape.friction = 1

    def add_to_space(self, space):
        space.add(self.ground_body, self.ground_shape)
        space.add(self.left_wall_body, self.left_wall_shape)
        space.add(self.right_wall_body, self.right_wall_shape)

    def draw(self, screen, offset):
        vert = self.ground_shape.get_vertices()
        vert = [self.ground_body.local_to_world(v) - offset for v in vert]
        pygame.draw.polygon(screen, self.color, vert)

        vert = self.left_wall_shape.get_vertices()
        vert = [self.left_wall_body.local_to_world(v) - offset for v in vert]
        pygame.draw.polygon(screen, self.color, vert)

        vert = self.right_wall_shape.get_vertices()
        vert = [self.right_wall_body.local_to_world(v) - offset for v in vert]
        pygame.draw.polygon(screen, self.color, vert)

