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

<pre>
├── Part1:Hardware/
│   └── <a href="Part1:Hardware/Project1%3ABooleanLogic">Project1:BooleanLogic</a>
│   └── <a href="Part1:Hardware/Project2%3ABooleanArithmetic">Project2:BooleanArithmetic</a>
│   └── <a href="Part1:Hardware/Project3%3AMemory">Project3:Memory</a>
│   └── <a href="Part1:Hardware/Project4%3AMachineLanguage">Project4:MachineLanguage</a>
│   └── <a href="Part1:Hardware/Project5%3AComputerArchitectures">Project5:ComputerArchitectures</a>
│   └── <a href="Part1:Hardware/Project6%3AAssembler">Project6:Assembler</a>
</pre>

---

## Philosophy

```
Everything begins with NAND and ends in abstraction.
```