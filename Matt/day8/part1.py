class Machine:

    def __init__(self):
        self.acc = 0
        self.pointer = 0
        self.addresses = []
    
    def accu(self, o):
        self.acc = self.acc + int(o[1:]) if o[0] == "+" else self.acc - int(o[1:])
        self.pointer += 1
        return self.acc
    
    def jmp(self, o):
        self.pointer = self.pointer + +int(o[1:]) if o[0] == "+" else self.pointer - int(o[1:])
        if self.pointer in self.addresses:
            print("Potential infinite loop detected!")
            print(f"Accumulator is: {self.acc}")
            print(f"Pointer is: {self.pointer}")
            if input("Continue? > ").upper() != "Y":
                print(self.addresses)
                return -1
            
        return self.pointer
    
    def nop(self):
        self.pointer += 1
        return self.pointer
    
    def run(self, insts):
        while True:
            self.addresses.append(self.pointer)
            i = insts[self.pointer].split(" ")
            if i[0] == "jmp":
                ret = self.jmp(i[1])
                if ret == -1:
                    break
                print(f"Jumped to: {ret}")
            elif i[0] == "acc":
                ret = self.accu(i[1])
                print(f"Accumulator is: {ret}")
            elif i[0] == "nop":
                ret = self.nop()
                print(f"No Operation. Next address: {ret}")
            else:
                print("Unsupported operand")
                break
            

con = Machine()

with open("input.txt") as f:
    insts = f.read().split("\n")

con.run(insts)
