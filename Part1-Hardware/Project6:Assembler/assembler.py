import sys
import re

symbol_table = {
    "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
    "SCREEN": 16384, "KBD": 24576,
    **{f"R{i}": i for i in range(16)}
}

comp_table = {
    # a = 0
    "0":   "0101010", "1":   "0111111", "-1":  "0111010",
    "D":   "0001100", "A":   "0110000", "!D":  "0001101",
    "!A":  "0110001", "-D":  "0001111", "-A":  "0110011",
    "D+1": "0011111", "A+1": "0110111", "D-1": "0001110",
    "A-1": "0110010", "D+A": "0000010", "D-A": "0010011",
    "A-D": "0000111", "D&A": "0000000", "D|A": "0010101",
    # a = 1
    "M":   "1110000", "!M":  "1110001", "-M":  "1110011",
    "M+1": "1110111", "M-1": "1110010", "D+M": "1000010",
    "D-M": "1010011", "M-D": "1000111", "D&M": "1000000",
    "D|M": "1010101"
}

dest_table = {
    "":    "000", "M":   "001", "D":   "010", "MD":  "011",
    "A":   "100", "AM":  "101", "AD":  "110", "AMD": "111"
}

jump_table = {
    "":    "000", "JGT": "001", "JEQ": "010", "JGE": "011",
    "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111"
}

# Clean a line of comments and whitespace
def clean(line):
    return re.sub("//.*", "", line).strip()

# First pass: resolve labels
def first_pass(lines):
    rom = 0
    for line in lines:
        line = clean(line)
        if not line:
            continue
        if line.startswith("("):
            label = line[1:-1]
            symbol_table[label] = rom
        else:
            rom += 1

# Second pass: generate binary code
def second_pass(lines):
    ram_address = 16
    binary_lines = []
    for line in lines:
        line = clean(line)
        if not line or line.startswith("("):
            continue

        if line.startswith("@"):  # A-instruction
            symbol = line[1:]
            if symbol.isdigit():
                address = int(symbol)
            else:
                if symbol not in symbol_table:
                    symbol_table[symbol] = ram_address
                    ram_address += 1
                address = symbol_table[symbol]
            binary_lines.append(f"{address:016b}")

        else:  # C-instruction
            if "=" in line:
                dest, comp_jump = line.split("=")
            else:
                dest, comp_jump = "", line
            if ";" in comp_jump:
                comp, jump = comp_jump.split(";")
            else:
                comp, jump = comp_jump, ""

            comp_bits = comp_table.get(comp.strip(), "0000000")
            dest_bits = dest_table.get(dest.strip(), "000")
            jump_bits = jump_table.get(jump.strip(), "000")

            binary_lines.append("111" + comp_bits + dest_bits + jump_bits)

    return binary_lines

# Main assembler function
def assemble(asm_path, hack_path=None):
    with open(asm_path, 'r') as file:
        lines = file.readlines()

    first_pass(lines)
    binary = second_pass(lines)

    out_path = hack_path or asm_path.replace(".asm", ".hack")
    with open(out_path, 'w') as file:
        file.write("\n".join(binary))

    print(f"Assembly complete: {out_path}")

# If running from CLI
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python assembler.py <file.asm>")
    else:
        assemble(sys.argv[1])
