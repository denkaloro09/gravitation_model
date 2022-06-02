class Storage:
    storage = []

    def add_obj(self, _planet):
        self.storage.append(_planet)

    def simulate_moving(self):
        for planet in self.storage:
            list_of_planets = [x for x in self.storage if x != planet]
            planet.move(list_of_planets)

    def draw(self, main_surface, track_surface):
        for planet in self.storage:
            planet.draw(main_surface, track_surface)
