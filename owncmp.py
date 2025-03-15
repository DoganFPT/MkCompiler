import sys
import os

program_filepath = sys.argv[1]
prog_line = []

with open(program_filepath, "r") as progfile:
    prog_line = [
            line.strip()
                for line in progfile.readlines()]


#create tokens of .hi lang
program = []

for line in prog_line:
    parts = line.split(" ")
    op = parts[0]

    if op == "":
        continue

    program.append(op)

    if op == "PUSH":
        number = int(parts[1])
        program.append(number)
    elif op == "PRINT":
        string_sent = "".join(parts[1:])[1:-1]
        program.append(string_sent)
    elif op == "JUMP0":
        func_label = parts[1]
        program.append(func_label)
    elif op == "JUMPGOTO":
        func_label = parts[1]
        program.append(func_label)

print(program)


#convert tokens into assembly

asm_filepath = program_filepath[:-4] + ".asm"
out = open(asm_filepath,"w") 

out.write("""; ---header---
          bits 64
          default rel
          """)

out.write("""; ---variables---
          section .bss
          """)

out.write("""; ---data---
          section .data
          """)

out.write("""; ---Starting point---
          section .text
          global main
          extern ExitProcess
          extern printf
          extern scanf

          main:
          \tPUSH rbp
          \tMOV rbp, rsp
          \tSUB rsp, 32
          """)

instruction_pointer = 0
while instruction_pointer < len(program):
    op = program[instruction_pointer]
    instruction_pointer +=1

    if op.endswith(":"):
        out.write(f";---label---\n")
        out.write(f"{op}\n")
    elif op == "PUSH":
        number = program[instruction_pointer]
        instruction_pointer += 1
        out.write(f";---PUSH---\n")
        out.write(f"\tPUSH {number}\n")
    elif op == "POP":
        out.write(f";---POP---\n")
        out.write(f"\tPOP\n")
    elif op == "ADD":
        out.write(f";---ADD---\n")
        out.write(f"\tPOP rax\n")
        out.write(f"\tPOP rbx\n")
        out.write(f"\tADD rbx, rax\n")
        out.write(f"\tPUSH rbx\n")
    elif op == "SUB":
        out.write(f";---SUB---\n")
        out.write(f"\tPOP rax\n")
        out.write(f"\tPOP rbx\n")
        out.write(f"\tSUB rbx, rax\n")
        out.write(f"\tPUSH rbx\n")
    elif op == "PRINT":
        string_literal_id = program[instruction_pointer]
        instruction_pointer += 1
        out.write(f";---PRINT---\n")
        out.write(f" TO IMPLEMENT\n")
    elif op == "READ":
        out.write(f";---READ---\n")
        out.write(f" TO IMPLEMENT\n")
    elif op == "JUMP0":
        label = program[instruction_pointer]
        instruction_pointer +=1
        out.write(f";---JUMP0---\n")
        out.write(f"\tCMP qword [rsp], 0\n")
        out.write(f"\tJE {label}\n")
    elif op == "JUMPGOTO":
        label = program[instruction_pointer]
        instruction_pointer += 1
        out.write(f";---JUMPGOTO\n")
        out.write(f"\tCMP qword [rsp], 0\n")
        out.write(f"\tJG {label}\n")
    elif op == "HALT":
        out.write(f";---HALT---\n")
        out.write(f"\tJMP EXIT_LABEL\n")
out.write("EXIT_LABEL\n")
out.write(f"\tXOR rax, rax\n")
out.write(f"\tCALL ExitProcess\n")
out.close()

print("Assembling data")
os.system(f"nasm -f elf64 {asm_filepath}")
print("Linking")
os.system(f"gcc -o {asm_filepath[:-4]+ '.exe'} {asm_filepath[:-3]+ 'o'}")

print("Run")
os.system(f"{asm_filepath[:-4] + 'o'}")




