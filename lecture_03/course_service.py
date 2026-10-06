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

    def cancel_enrollment(self):
        if self.enrolled == 0:
            raise ValueError("Нет зарегистрированных студентов")

        self.enrolled -= 1

    @property
    def is_full(self):
        return self.enrolled == self.capacity

class IntensiveCourse(Course):
    def __init__(self, name, capacity, hours_per_week):
        super().__init__(name, capacity)

        if not isinstance(hours_per_week, int) or not 6 <= hours_per_week <= 20:
            raise ValueError("Количество часов должно быть от 6 до 20")

        self.hours_per_week = hours_per_week

    def workload_level(self):
        if self.hours_per_week <= 10:
            return "средняя"

        return "высокая"