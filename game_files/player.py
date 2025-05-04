import pygame, pymunk, math

class Player():
    def __init__(self):
        self.color = (0, 0, 0)
        self.ypos = 450

        self.head_body = pymunk.Body()
        self.head_shape = pymunk.Circle(self.head_body, 20)
        self.head_body.position = 640, self.ypos + 15
        self.head_shape.mass = 2
        self.head_shape.friction = 1
        self.head_shape.collision_type = 2

        self.torso_body = pymunk.Body()
        self.torso_body.position = 620, self.ypos + 40
        self.torso_shape = pymunk.Poly(self.torso_body, [(0,0), (40,0), (0,80), (40,80)])
        self.torso_shape.mass = 5
        self.torso_shape.friction = 1

        self.left_arm_body = pymunk.Body()
        self.left_arm_body.position = 595, self.ypos + 40
        self.left_arm_shape = pymunk.Poly(self.left_arm_body, [(0,0), (20,0), (0,60), (20,60)])
        self.left_arm_shape.mass = 2
        self.left_arm_shape.friction = 1

        self.right_arm_body = pymunk.Body()
        self.right_arm_body.position = 665, self.ypos + 40
        self.right_arm_shape = pymunk.Poly(self.right_arm_body, [(0,0), (20,0), (0,60), (20,60)])
        self.right_arm_shape.mass = 2
        self.right_arm_shape.friction = 1

        self.left_leg_body = pymunk.Body()
        self.left_leg_body.position = 615, self.ypos + 125
        self.left_leg_shape = pymunk.Poly(self.left_leg_body, [(0,0), (20,0), (0,60), (20,60)])
        self.left_leg_shape.mass = 7
        self.left_leg_shape.friction = 1

        self.right_leg_body = pymunk.Body()
        self.right_leg_body.position = 645, self.ypos + 125
        self.right_leg_shape = pymunk.Poly(self.right_leg_body, [(0,0), (20,0), (0,60), (20,60)])
        self.right_leg_shape.mass = 7
        self.right_leg_shape.friction = 1

        self.torso_head_joint = pymunk.PivotJoint(self.torso_body, self.head_body, (640, self.ypos + 40)) 
        self.torso_head_limit_joint = pymunk.RotaryLimitJoint(self.torso_body, self.head_body, -0.5, 0.5)

        self.torso_left_arm_joint = pymunk.PivotJoint(self.torso_body, self.left_arm_body, (620,self.ypos + 40))
        self.torso_left_arm_limit_joint = pymunk.RotaryLimitJoint(self.torso_body, self.left_arm_body,-1000,1000)
        self.torso_left_arm_motor = pymunk.SimpleMotor(self.torso_body, self.left_arm_body, 0)
        self.torso_left_arm_motor.max_force = 1000000

        self.torso_right_arm_joint = pymunk.PivotJoint(self.torso_body, self.right_arm_body, (660,self.ypos + 40))
        self.torso_right_arm_limit_joint = pymunk.RotaryLimitJoint(self.torso_body, self.right_arm_body,-1000,1000)
        self.torso_right_arm_motor = pymunk.SimpleMotor(self.torso_body, self.right_arm_body, 0)
        self.torso_right_arm_motor.max_force = 1000000

        self.torso_left_leg_joint = pymunk.PivotJoint(self.torso_body, self.left_leg_body, (625,self.ypos + 125))
        self.torso_left_leg_limit_joint = pymunk.RotaryLimitJoint(self.torso_body, self.left_leg_body,-1000,1000)
        self.torso_left_leg_motor = pymunk.SimpleMotor(self.torso_body, self.left_leg_body, 0)
        self.torso_left_leg_motor.max_force = 1000000

        self.torso_right_leg_joint = pymunk.PivotJoint(self.torso_body, self.right_leg_body, (655,self.ypos + 125))
        self.torso_right_leg_limit_joint = pymunk.RotaryLimitJoint(self.torso_body, self.right_leg_body,-1000,1000)
        self.torso_right_leg_motor = pymunk.SimpleMotor(self.torso_body, self.right_leg_body, 0)
        self.torso_right_leg_motor.max_force = 1000000

        self.left_arm_shape.filter = pymunk.ShapeFilter(group = 1)
        self.right_arm_shape.filter = pymunk.ShapeFilter(group = 1)
        self.left_leg_shape.filter = pymunk.ShapeFilter(group = 1)
        self.right_leg_shape.filter = pymunk.ShapeFilter(group = 1)
        self.torso_shape.filter = pymunk.ShapeFilter(group = 1)
        self.head_shape.filter = pymunk.ShapeFilter(group = 1)

    
    def add_to_space(self, space):
        space.add(self.head_body, self.head_shape)
        space.add(self.torso_body, self.torso_shape)
        space.add(self.left_arm_body, self.left_arm_shape)
        space.add(self.right_arm_body, self.right_arm_shape)
        space.add(self.left_leg_body, self.left_leg_shape)
        space.add(self.right_leg_body, self.right_leg_shape)
        space.add(self.torso_head_joint)
        space.add(self.torso_head_limit_joint)

        space.add(self.torso_left_arm_joint)
        space.add(self.torso_left_arm_limit_joint)
        space.add(self.torso_left_arm_motor)

        space.add(self.torso_right_arm_joint)
        space.add(self.torso_right_arm_limit_joint)
        space.add(self.torso_right_arm_motor)
        
        space.add(self.torso_left_leg_joint)
        space.add(self.torso_left_leg_limit_joint)
        space.add(self.torso_left_leg_motor)

        space.add(self.torso_right_leg_joint)
        space.add(self.torso_right_leg_limit_joint)
        space.add(self.torso_right_leg_motor)

    def draw_poly(self, poly_body, poly_shape, screen, offset):
        vert = poly_shape.get_vertices()
        vert = [poly_body.local_to_world(v) - offset for v in vert]
        pygame.draw.polygon(screen, self.color, vert)
    
    def draw_all(self, screen, offset):
        pygame.draw.circle(screen, self.color, (self.head_body.position - offset), 20)
        self.draw_poly(self.torso_body, self.torso_shape, screen, offset)
        self.draw_poly(self.left_arm_body, self.left_arm_shape, screen, offset)
        self.draw_poly(self.right_arm_body, self.right_arm_shape, screen, offset)
        self.draw_poly(self.left_leg_body, self.left_leg_shape, screen, offset)
        self.draw_poly(self.right_leg_body, self.right_leg_shape, screen, offset)
    
        
        
        
        
        
    

    
        