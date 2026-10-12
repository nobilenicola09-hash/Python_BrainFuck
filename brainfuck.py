def run_brainfuck(source_code):
    # Filter only the valid characters of the Brainfuck language.
    code = "".join(c for c in source_code if c in "><+-.,[]")
    
    #Initialize the tape and position the pointer at the center (15000).
    memory = bytearray(30000)
    ptr = 15000  
    pc = 0  # Program counter
    
    # Pre-calculate square bracket jumps.
    bracket_map = {}
    stack = []
    for i, cmd in enumerate(code):
        if cmd == '[':
            stack.append(i)
        elif cmd == ']':
            if not stack:
                raise SyntaxError("You left out some brackets ']' ")
            start = stack.pop()
            bracket_map[start] = i
            bracket_map[i] = start
    
    if stack:
        raise SyntaxError("You left out some brackets '[' ")
        
    output = []
    input_buffer = []
    
    # Main execution cycle
    while pc < len(code):
        cmd = code[pc]
        
        if cmd == '>':
            ptr = (ptr + 1) % 30000
        elif cmd == '<':
            ptr = (ptr - 1) % 30000
        elif cmd == '+':
            memory[ptr] = (memory[ptr] + 1) % 256
        elif cmd == '-':
            memory[ptr] = (memory[ptr] - 1) % 256
        elif cmd == '.':
            output.append(chr(memory[ptr]))
        elif cmd == ',':
            if not input_buffer:
                try:
                    user_in = input("Input required: ")
                    input_buffer.extend(map(ord, user_in + "\n"))
                except EOFError:
                    input_buffer.append(0)
            memory[ptr] = input_buffer.pop(0) % 256
        elif cmd == '[':
            if memory[ptr] == 0:
                pc = bracket_map[pc]
        elif cmd == ']':
            if memory[ptr] != 0:
                pc = bracket_map[pc]
                
        pc += 1
        
    return "".join(output)

#  MULTI-LINE INPUT HANDLING 
print("Enter the Brainfuck code.")
print("(You can press Enter to start a new line as many times as you like..")
print(" When you are finished, leave a blank line and press ENTER to start.):\n")

lines = []
while True:
    line = input()
    #If you press Enter on an empty line, the loop terminates and execution begins.
    if line.strip() == "":
        break
    lines.append(line)

codice_utente = "\n".join(lines)

print("\n========================================")
print(" Translation into speech on the terminal:")
print("========================================")
risultato = run_brainfuck(codice_utente)
print(risultato)