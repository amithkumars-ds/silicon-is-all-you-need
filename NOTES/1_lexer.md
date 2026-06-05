# Notes

1. Token: A token is the smallest meaningful unit of the language.
2. Lexer: The Lexer reads the raw text, character-by-character, then groups characters into chunks, and labales each chunk with a type.

For example,
```
x = 10 + 5
```

the tokens are,
| word | compiler word | example |
| ---- | ------------- | ------- |
| alphabet | IDENTIFIER | x |
| number | NUMBER | 5, 10 |
| operator | OPERATOR | + |
| = | ASSIGN | = |
| white space | SKIP IT |  |




here lexer sees it as,
```
[IDENTIFIER x] [ASSIGN = ] [NUMBER 10] [OPERATOR +] [NUMBER 5]
```

The lexer moves through text one character at a time using a cursor. current_char is always what's under the cursor. None means end of input. None here is doing the job of what in hardware would be called a sentinel — a special value that means "stop, nothing more to read." You'll see this pattern constantly in systems programming.

