class Building:
    total = 0

    def __init__(self, name='Объект'):
        self.name = name
        Building.total += 1

    def __str__(self):
        return str(self.__dict__)


build_list = [Building('Объект №' + str(i)) for i in range(1, 41)]

print(*build_list)
print('Всего объектов:', Building.total)
