class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return self.__format_time(self.__hours, self.__minutes, self.__seconds)

    def next_second(self):
        self.__seconds += 1
        if self.__seconds == 60:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes == 60:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours == 24:
                    self.__hours = 0

    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds == -1:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes == -1:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours == -1:
                    self.__hours = 23

    @staticmethod
    def __format_time(hours, minutes, seconds):
        return f"{hours:02}:{minutes:02}:{seconds:02}"

# Test de la classe Timer
timer = Timer(23, 59, 59)
print(timer)  # Affiche: 23:59:59
timer.next_second()
print(timer)  # Affiche: 00:00:00
timer.prev_second()
print(timer)  # Affiche: 23:59:59
