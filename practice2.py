# 1 - PRINT_VENKY
# 2 - HALT
# 3 - SAVE_REG store a value in a register
# 4 - PRINT_REG print the register value in decimal


memory = [
  1, # PRINT_VENKY
  3, # SAVE_REG R4 37, instruction itself also called "opcode"
  4, # 4 and 37 are arguments to SAVE-REG, also called "operands"
  37, 
  4, # PRINT_REG R4(INSTRUCTION)
  4,
  2 # HALT
]

running = True

pc = 0
registers = [0]*8
while running:
  ir = memory[pc]
  
  if ir == 1:
    print('venky')
    pc += 1

  elif ir == 2:
    running = False  
    pc += 1

  elif ir == 3:
    reg_num = memory[pc+1]  
    value = memory[pc+2]
    registers[reg_num] = value
    print(registers)

    pc += 3
  elif ir == 4:
    reg_num = memory[pc+1]   
    print(registers[reg_num])

    pc += 2
