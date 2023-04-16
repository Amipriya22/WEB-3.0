import math as m


class Car():

    # attributes of this Car class
    def __init__(self,make,model,year,speed,x,y,angle):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed
        self.x = x
        self.y = y
        self.angle = angle
        self.velocity = (self.speed *m.cos(self.angle), self.speed *m.sin(self.angle))

    # Methods of this Car class
    def acclerate(self,speed_increment):
        self.speed += speed_increment

    def brake(self,speed_decrement):
        self.speed -= speed_decrement

    def move(self,dt):
        self.x += self.speed*m.cos(m.radians(self.angle))*dt
        self.y += self.speed*m.sin(m.radians(self.angle))*dt

    def detect_collision(self,car2):
        relative_distance = m.sqrt(((self.x-car2.x)**2) +((self.y-car2.y)**2))
        if relative_distance<0.1 :
            return True
        else:
            return False

    def time_to_collision(self, car2):
        if self.detect_collision(car2):
            return None

        angle_diff = abs(m.atan2(*np.cross(self.velocity, car2.velocity)) % (m.pi))


        if angle_diff == 0 or angle_diff == m.pi:
            return None  # no time to collision

        a = (self.velocity[0] - car2.velocity[0]) ** 2 + (self.velocity[1] - car2.velocity[1]) ** 2
        b = 2 * ((self.velocity[0] - car2.velocity[0]) * (self.position[0] - car2.position[0]) +
                 (self.velocity[1] - car2.velocity[1]) * (self.position[1] - car2.position[1]))
        c = (self.position[0] - car2.position[0]) ** 2 + (self.position[1] - car2.position[1]) ** 2

        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0:
            return None
        else:
            sqrt_discriminant = m.sqrt(discriminant)
            t1 = (-b + sqrt_discriminant) / (2 * a)
            t2 = (-b - sqrt_discriminant) / (2 * a)
            if t1 > 0:
                return t1  # this is the time to collision





#_main_

#
# car1 =Car("tesla","model 3",2022,20,0,0,m.pi/4)
# car2 =Car("auto","model 2",2022,30,2,2,3*(m.pi)/4)
#
# car1.brake(10)
# print(car1.speed)
# car1.acclerate(12)
# print(car1.speed)
# print(car1.velocity)
# print(car1.detect_collision(car2))



