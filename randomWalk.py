from random import choice

class RandomWalk:
    """A class to generate random walks"""
    def __init__(self, num_points= 5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate the points in the walk"""
        # keeping taking the steps until the walk reaches the desired length
        while self.num_points > len(self.x_values):
            #decide which direction and to go and the distance to go
            x_step = self.get_step()
            y_step = self.get_step()
            if y_step ==0 and x_step ==0:
                continue
            #calculate the new step
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):
        direction = choice([1,-1])
        distance = choice([i for i in range(1,9)])
        return direction * distance

