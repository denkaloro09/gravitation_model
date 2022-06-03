class Storage:
    storage = []

    def add_obj(self, _planet):
        self.storage.append(_planet)

    def simulate_moving(self):
        for planet in self.storage:
            if not planet.is_clicked():
                planet.move(self.storage)
        self.reset_processing()

    def draw(self, main_surface, track_surface):
        for planet in self.storage:
            planet.draw(main_surface, track_surface)

    def move_by_mouse(self, rel):
        for planet in self.storage:
            if planet.is_clicked():
                planet.move_by_mouse(rel)

    def move_system_position(self, rel):
        for planet in self.storage:
            planet.move_by_mouse(rel)

    def is_planets_collide_point(self, pos):
        for planet in self.storage:
            if planet.is_clicked_by_mouse(pos):
                return True
        return False

    def cancel_planet_clicks(self):
        for planet in self.storage:
            if planet.is_clicked():
                planet.not_clicked()

    def reset_processing(self):
        for planet in self.storage:
            planet.processed = False

    def count(self):
        return len(self.storage)
