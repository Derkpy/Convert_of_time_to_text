from datetime import datetime


class HourToTextConverter:

    def __init__(self):
        # Lista y diccionario que contienen las palabras que se usarán
        # para crear la hora en texto
        self.times = ["o' clock", "past", "quarter", "half", "to"]
        self.numbers = {
            1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
            7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
            12: "twelve", 13: "thirteen", 14: "fourteen", 16: "sixteen",
            17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
            21: "twenty one", 22: "twenty two", 23: "twenty three",
            24: "twenty four", 25: "twenty five", 26: "twenty six",
            27: "twenty seven", 28: "twenty eight", 29: "twenty nine"
        }

    def verify_time(self):  # Comprobar que se ingrese correctamente la hora

        while True:
            try:
                hour_entry = input("Please, Type the time below: ")
                verify_hour = datetime.strptime(hour_entry, "%H:%M")
                break
            except ValueError:
                print("Enter the time correctly")

        # Se separa el tiempo en Hora y Minutos
        hour = int(hour_entry.split(":")[0])
        minute = int(hour_entry.split(":")[1])
        self.election(minute=minute, hour=hour)

    # if para revisar los minutos y estructurar el texto final
    def election(self, minute, hour):
        # Si ingresa 00:59 o 12:59 imprime one minute to one
        if ((hour == 12) or (hour == 0)) and (minute == 59):
            print("one minute to one")
        else:
            hour = hour if not hour >= 12 else hour - 12
            if 60 - minute == 1 or 60 - minute == 59:
                self.format_0(word=self.times[1] if minute == 1
                              else self.times[4],
                              hour=12 if hour == 0 else hour + 1)
            else:
                while True:  # Bucle hasta que encuentre los valores correctos
                    if 2 <= minute <= 14 or 16 <= minute <= 29:
                        word = self.times[1]
                        hour = self.numbers[hour] if not hour == 0 \
                            else self.numbers[12]
                        minute = self.numbers[minute]
                        self.format_1(minute=minute, word=word, hour=hour)
                        break
                    elif minute == 15 or minute == 45 or minute == 30:
                        self.format_2(
                            word_1=self.times[2] if (minute == 15)
                            or (minute == 45)
                            else self.times[3],
                            word_2=self.times[4] if (minute == 45)
                            else self.times[1],
                            hour=self.numbers[hour + 1]
                            if not (minute == 15) or (minute == 30)
                            else self.numbers[hour])
                        break
                    elif 31 <= minute <= 44 or 46 <= minute <= 58:
                        # minute + "minutes" + to + hour soon
                        word = self.times[4]
                        hour = self.numbers[hour + 1]
                        minute = self.numbers[60 - minute]
                        self.format_1(minute=minute, word=word, hour=hour)
                        break
                    else:
                        # se imprime hour + o' clock si minute = 0
                        hour = self.numbers[hour] if not hour == 0 \
                            else self.numbers[12]
                        print(hour + " " + self.times[minute])
                        break

    # Funciones para formar el texto de acuerdo a la selección del if
    def format_0(self, word, hour):  # Unicamente cuando falta o paso un minuto
        print("one minute " + word + " " + self.numbers[hour])

    # Esta funcion se tiene predeterminada "minutes" y de acuerdo a las
    # comprobaciones de los if se ingresan los otros valores
    def format_1(self, minute, word, hour):
        print(minute + " minutes " + word + " " + hour)

    # Especificamente para formar si pasaron o faltan 15 minutos
    # de igual forma para la mitad de las horas
    def format_2(self, word_1, word_2, hour):
        print(word_1 + " " + word_2 + " " + hour)


# Inicializar el programa
if __name__ == "__main__":

    converter = HourToTextConverter()

    converter.verify_time()
