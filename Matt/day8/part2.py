class Machine:

    def __init__(self, debug=False):
        self.acc = 0
        self.pointer = 0
        self.addresses = []
        self.debug = debug
        self.flipped_address = []
        self.flipped = False
    
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
            if not self.debug:
                if input("Continue? > ").upper() != "Y":
                    print(self.addresses)
                    return - 1
            else:
                self.pointer = 0
                self.acc = 0
                self.flipped = False
                self.addresses.clear()
            
        return self.pointer
    
    def nop(self):
        self.pointer += 1
        return self.pointer

    def run(self, insts):
        while True:
            self.addresses.append(self.pointer)
            i = insts[self.pointer].split(" ")
            if self.debug and not self.flipped and self.pointer not in self.flipped_address \
                 and i[0] != "acc":
                self.flipped = True
                self.flipped_address.append(self.pointer)
                print(f"** Flipped address {self.pointer} **")
                i[0] = "jmp" if i[0] == "nop" else "nop"

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
            

con = Machine(True)

with open("input.txt") as f:
    insts = f.read().split("\n")

con.run(insts)
