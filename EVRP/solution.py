import numpy as np

class Solution():
    def __init__(self):
        self.tours = []
    
    def append(self, id):
        self.tours.append(id)
    
    def set(self, solution):
        self.tours = solution
        
    def get(self, id):
        return self.tours[id]
    
    def get_tour_length(self):
        self.calculate_tour_length()
        return self.tour_length
    
    def to_array(self):
        return np.array([node.id for node in self.tours])
    
    def get_vehicle_tours(self):
        
        """ Vehicle did not start or end depot """
        if not self.tours[0].is_depot() or not self.tours[-1].is_depot():
            return None
        
        vehicle_tours = []
        tour = [self.tours[0]]
        
        for node in self.tours[1:]:
            if node.is_depot():
                tour.append(self.tours[0])
                vehicle_tours.append(tour)
                tour = [self.tours[0]]
            else:
                tour.append(node)
        return vehicle_tours
    
    def set_vehicle_tours(self, tours):
        self.tours = [node for node in tours[0]]
        for tour in tours[1:]:
            self.tours.extend(tour[1:])
        
    def calculate_tour_length(self):
        tour_length = 0
        for i in range(len(self.tours) - 1):
            tour_length += self.tours[i].distance(self.tours[i + 1])
        self.tour_length = tour_length
    
    def print(self, max_visible_tours=15):
        vehicle_tours = self.get_vehicle_tours()
        print("-" * 40)
        print("Tour length: " + str(self.get_tour_length()))
        for i, tour in enumerate(vehicle_tours):
            if len(tour) > max_visible_tours:
                print('Tour {}: '.format(i) +' | '.join(map(str, tour[:max_visible_tours])) + ' | ...')
            else:
                print('Tour {}: '.format(i)+ ' | '.join(map(str, tour)))
        print("-" * 40)
        