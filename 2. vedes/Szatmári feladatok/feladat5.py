class Sor():                        # queue
    def __init__(self) -> None:
        self.elemek = []


    def ures(self):
        if len(self.elemek) == 0:
            return True
        else:
            return False


    def betesz(self, x):                # push
        return self.elemek.append(x)


    def kivesz(self):
        if len(self.elemek) == 0:
            pass
        else:
            return self.elemek.pop(0)      # pop


    def meret(self):
        return len(self.elemek)


class Verem():                # stack
    def __init__(self) -> None:
        self.elemek = []

    def ures(self):
        if len(self.elemek) == 0:
            return True
        else:
            return False


    def betesz(self, x):                # push
        return self.elemek.append(x)

    def kivesz(self):
        if len(self.elemek) == 0:
            pass
        else:
            return self.elemek.pop()      # pop 

    def meret(self):
        return len(self.elemek)


def main():
   pass
  


if __name__ == "__main__":
    main()