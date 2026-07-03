// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

// Initialize screen pointer
@SCREEN
D=A
@addr
M=D         // addr = SCREEN (16384)

// Infinite loop
(LOOP)
// Check keyboard
@KBD
D=M

// Jump to FILL if key pressed (D > 0)
@FILL
D;JGT

// Otherwise, CLEAR
(CLEAR)
    @SCREEN
    D=A
    @addr
    M=D       // Reset addr to SCREEN

    @8192
    D=A
    @count
    M=D       // count = 8192

    (CLEAR_LOOP)
        @addr
        A=M
        M=0    // Write 0 (white)

        @addr
        M=M+1  // addr++

        @count
        MD=M-1 // count--, D=count

        @CLEAR_LOOP
        D;JGT  // Loop if count > 0

    @LOOP
    0;JMP     // Return to main loop

(FILL)
    @SCREEN
    D=A
    @addr
    M=D       // Reset addr to SCREEN

    @8192
    D=A
    @count
    M=D       // count = 8192

    (FILL_LOOP)
        @addr
        A=M
        M=-1   // Write -1 (black, all 1s)

        @addr
        M=M+1   // addr++

        @count
        MD=M-1  // count--, D=count

        @FILL_LOOP
        D;JGT   // Loop if count > 0

    @LOOP
    0;JMP      // Return to main loop
