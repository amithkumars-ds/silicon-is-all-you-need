# AST: Abstract Syntax tree

For ```'10+5'```, You have:
> [Token(NUMBER, 10), Token(PLUS, +), Token(NUMBER, 5)]

This is a flat list. The lexer's job is done. But consider this input: 
```10 + 5 * 2```

The flat list would be:
> [NUMBER 10] [PLUS +] [NUMBER 5] [MULTIPLY *] [NUMBER 2]

Two ways to evaluate this,
1. Left to right: (10 + 5) * 2 = 30
2. Math rules: 10 + (5 * 2) = 20

So we use a tree,
```markdown
    +
   / \
  10  *
     / \
    5   2
```

Read this bottom up, that's our evaluation order:

5 * 2 first — deepest node
10 + result second — root node

The tree encodes precedence through structure, not through metadata tags. We don't need to say "this has priority 2" — the shape itself tells us.

Now the vocabulary:
| Name | What it is | Example above |
| ---- | ------------- | ------- |
| Node | any single element in the tree | +, 10, * |
| Root | topmost node | + |
| Leaf | node with no children | 10, 5, 2 |
| Internal node | node with children | +, * |


This specific kind of tree has a name — Abstract Syntax Tree, AST.
Abstract because it drops things that don't affect meaning — whitespace, parentheses, semicolons. Only the structure of meaning remains.