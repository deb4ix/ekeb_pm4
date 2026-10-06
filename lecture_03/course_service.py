class Course:
    def __init__(self, name, capacity):
        if not name:
            raise ValueError("Название курса не может быть пустым")

        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Количество мест должно быть положительным целым числом")

        self.name = name
        self.capacity = capacity
        self.enrolled = 0

    def available_places(self):
        return self.capacity - self.enrolled

    def enroll(self):
        if self.enrolled >= self.capacity:
            raise ValueError("Нет свободных мест")

        self.enrolled += 1
        return self.available_places()