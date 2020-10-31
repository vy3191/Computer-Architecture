"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.register = [0] * 8
        self.pc = 0
        self.sp = 7

    def load(self, file_name):
        """Load a program into memory."""
        # address value for tracking the index of the ram memory
        address = 0
        with open(file_name) as f:
            for each_line in f:
                split_line = each_line.split('#')
                # grab the first element at the index 0 and trim the  space if any
                get_item_at_zero = split_line[0].strip()
                self.ram[address] = get_item_at_zero
                address += 1
        print(self.ram)  
        # For now, we've just hardcoded a program:
        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]
        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def ram_read(self, index):
        return self.ram[index]   

    def ram_write(self, address, value):
        # return self.ram[address] = value
        pass
     

    def run(self):
        """Run the CPU."""
        running = True
        
        while running:
            # ir = self.ram[self.pc]   # ir=  _Instruction Register_.
            ir = self.ram_read(self.pc)

            if ir ==  0b10000010: #LDI    index =0
                operand_a = self.ram_read(self.pc+1)  # index at 1
                operand_b = self.ram_read(self.pc+2)  # index at 2 this is the value gives (8)
                self.register[operand_a] = operand_b   # register[0] = 8
                self.pc += 3

            elif ir ==  0b00000001: #HLT   
                running = False
                self.pc += 1  

            elif ir == 0b01000111:  # PRN    this is the index at 3 --->this should print
                operand_a = self.ram_read(self.pc+1)  # grab the next pc value in decimal
                print(self.register[operand_a])   # this should print 8
                self.pc += 2



        
