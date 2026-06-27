# silicon-is-all-you-need

```
+--------------------------------------------------+
|          FROM NAND TO A COMPUTER                 |
|                0s  •  1s  •  LOGIC               |
+--------------------------------------------------+
```

> Building a computer from first principles — gates, chips, CPU, OS, and beyond.

---

## Roadmap

```
[NAND] ══════> [GATES] ══════> [ALU  ]
   |               |               |
   v               v               v
[CPU ] ══════> [OS   ] ══════> [TETRIS]
                                    |
                                    v
                                [SUDOKU?]
```

---

## Projects

### Part 1 — Hardware

- [x] **Boolean Logic** — 15 chips from NOT to MUX/DMUX, all reduced to NAND
- [ ] **Boolean Arithmetic** — adders, incrementer, ALU
- [ ] **Memory** — flip-flops, registers, RAM, program counter
- [ ] **Machine Language** — assembly programs on the Hack platform
- [ ] **Computer Architecture** — CPU + memory + instruction fetch cycle

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

```
silicon-is-all-you-need/
├── Part1-Hardware/
│   └── Project1-BooleanLogic/
│   └── Project2-BooleanArithmetic/
└── Part2-Software/
```

---

## Philosophy

```
Everything begins with NAND.
Everything else is abstraction.
```