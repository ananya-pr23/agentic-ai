class TravelMemory:
    def __init__(self):
        self.preferences = {}
        self.trip_history = []

    def save_preferences(self, preferences):
        self.preferences.update(preferences)

    def get_preferences(self):
        return self.preferences

    def save_trip(self, trip):
        self.trip_history.append(trip)

    def get_trip_history(self):
        return self.trip_history

    def get_last_trip(self):
        if self.trip_history:
            return self.trip_history[-1]

        return None