class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory


    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return (f"sum: {self.__cpu + self.__memory}\n"
                f"substraction: {self.__cpu - self.__memory}\n"
                f"multiplication: {self.__cpu * self.__memory}\n"
                f"division: {self.__cpu / self.__memory}")

    def __str__(self):
        return f" Cpu: {self.cpu}, Memory: {self.memory}"


class Phone:
    # __sim_cards_list = 0
    def __init__(self, sim_cards_list : list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        sim = self.sim_cards_list[sim_card_number - 1]
        print(f"Calling to {call_to_number} from {sim_card_number} sim card: {sim}")

    def __str__(self):
        return f"Phone (sim_cards: {",".join(self.sim_cards_list)})"

class SmartPhone(Computer, Phone):
    def __init__(self, sim_cards_list, cpu, memory):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Building a route to {location}.")

    def __str__(self):
        return (f"SmartPhone(cpu: {self.cpu}, memory: {self.memory}, "
                f"sim_cards: {', '.join(self.sim_cards_list)})")


computer = Computer(35, 12)
phone = Phone(["BEELINE", "MegaCom"])
smartphone = SmartPhone(["O!", "MegaFon"], 24, 64)
smart_2 = SmartPhone(["MedaCom", "Beeline"], 56, 128)

print(computer)
print(phone)
print(smartphone)
print(smart_2)

print(f"Computer computations:\n{computer.make_computations()}")
print(f"Smartphone computations:\n{smart_2.make_computations()}")

phone.call(2, "+996 111 222 333")
smartphone.use_gps("Kant")




