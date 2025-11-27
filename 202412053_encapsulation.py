class Student:
    def __init__(self, sid, name, gpa=0.0):
        self.sid = sid            # public
        self.name = name          # public
        self._credits = 0         # protected
        self.__gpa = gpa          # private

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, value):
        if not (0.0 <= value <= 4.0):
            raise ValueError("GPA harus antara 0.0 dan 4.0")
        self.__gpa = round(value, 2)

    def add_credits(self, n):
        if n < 0:
            raise ValueError("credits tidak boleh negatif")
        self._credits += n

    def classify(self):
        gpa = self.__gpa
        if gpa >= 3.5:
            return "Cum Laude"
        elif gpa >= 2.5:
            return "Good"
        else:
            return "Remedial"


if __name__ == "__main__":
    s = Student("S100", "Ana", 3.1)
    print(s.get_gpa())
    print(s.classify())

    s.set_gpa(3.75)
    print(s.get_gpa())
    print(s.classify())
