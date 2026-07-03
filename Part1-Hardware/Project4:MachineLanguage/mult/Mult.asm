// File name: projects/4/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// R0 = first number
// R1 = second number
// R2 = result
// Algorithm: repetitive addition

// Pseudo code:
// prod = 0
// i = 0
// while i < R0:
//     prod = prod + R1
//     i = i + 1
// R2 = prod

    // Initialize R2 = 0
    @R2
    M=0

    (LOOP)
        // Exit if count == 0
        @R1
        D=M
        @END
        D;JEQ

        // Add R0 to R2 (R2 += R0)
        @R0
        D=M
        @R2
        M=M+D

        // Decrement R1 (count)
        @R1
        M=M-1

        // Repeat
        @LOOP
        0;JMP

    (END)
        @END
        0;JMP    // Halt (optional)
