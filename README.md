# silicon-is-all-you-need

> Building a computer from first principles — gates, chips, CPU, OS, and beyond.


## Roadmap

```
┌─────────┐     ┌─────────┐     ┌─────────┐
│  NAND   │ ──> │  GATES  │ ──> │   ALU   │
└─────────┘     └─────────┘     └────┬────┘
                                     │
                                     ▼
┌─────────┐     ┌─────────┐     ┌─────────┐
│ SUDOKU? │ <── │ TETRIS  │ <── │   CPU   │
└─────────┘     └────▲────┘     └────┬────┘
                     │               │
                     │               ▼
                     │          ┌─────────┐
                     └───────── │   OS    │
                                └─────────┘
```

---

## Projects

### Part 1 — Hardware

- [x] **Boolean Logic** — 15 chips from NOT to MUX/DMUX, all reduced to NAND
- [x] **Boolean Arithmetic** — adders, incrementer, ALU
- [x] **Memory** — flip-flops, registers, RAM, program counter
- [x] **Machine Language** — assembly programs on the Hack platform
- [x] **Computer Architecture** — CPU + memory + instruction fetch cycle
- [x] **Assembler** - converts machine language to bit representation

### Part 2 — Software

- [ ] **Assembler** — translates Hack assembly to binary
- [ ] **VM I: Stack** — stack arithmetic and memory segments
- [ ] **VM II: Control** — branching, functions, call stack
- [ ] **Compiler I: Syntax** — tokenizer and parser for Jack
- [ ] **Compiler II: Code Generation** — Jack → VM code
- [ ] **Operating System** — math, memory, screen, keyboard, output
- [ ] **Tetris** — it runs
- [ ] **Sudoku?** — it might

---

## Structure

**Part1-Hardware**
- [x] [Project1-BooleanLogic](./Part1-Hardware/Project1%3ABooleanLogic)
- [x] [Project2-BooleanArithmetic](./Part1-Hardware/Project2%3ABooleanArithmetic)
- [x] [Project3-Memory](./Part1-Hardware/Project3%3AMemory)
- [x] [Project4-MachineLanguage](./Part1-Hardware/Project4%3AMachineLanguage)
- [x] [Project5-ComputerArchitecture](./Part1-Hardware/Project5%3AComputerArchitecture)
- [x] [Project6-Assembler](./Part1-Hardware/Project6%3AAssembler)

**Part2-Software**
- [ ] [Project7-VM1StackArithmetic]
- [ ] [Project8-VM2ProgramControl]
- [ ] [Project9-HighLevelLanguage]
- [ ] [Project10-Compiler1Parsing]
- [ ] [Project11-Compiler2CodeGeneration]
- [ ] [Project12-OperatingSystem]

---

## Philosophy

```
Everything begins with NAND and ends in abstraction.
```