class Radnoylar_soni:
    def __init__(self, son):
        self.son = son
        self.Radnoylar = []

    def funktion_Radnoylar_soni(self):
        for i in range(self.son):
            self.Radnoylar.append(input(f"{i + 1}-Radnoyizni ismini yozing:\n>>"))
        return self.Radnoylar


a = Radnoylar_soni(int(input("Nechta radnoyizni taklif qilmoqchisiz ? ")))
print(a.funktion_Radnoylar_soni())
