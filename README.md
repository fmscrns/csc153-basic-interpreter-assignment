# THE INSTRUCTIONS:

The logical expressions we learned in mathematics involves values T for True and F
for False, and basic operations such as ¬ for negation, ∨ for disjunction (or), and ∧ for
conjunction (and). Example expression such as ¬F and this will resolve into T. Other
examples are the following:
• T ∨ F will resolve into T
• F ∧ ¬T will resolve into F
• ¬(T ∨ F) ∧ T will resolve into F
Write a simple interpreter for the resolution of logical expressions. Input should be
any valid logical expressions as string and will produce output of either T or F and
can also handle spaces in the input. You can use symbols available in the keyboard for
the operator such as exclamation mark (!) for negation, vertical bar (|) for disjunction,
and ampersand (&) for conjuction.
You can use the parsers you have written from the previous assignment to handle the
parsing of lexemes of the logical expressions.
Some example of the resolve interpreter function are shown below:

resolve "!F"
T

resolve "T | F"
T

resolve "F & !T"
F

resolve "!(T | F) & T"
F

resolve "T | F & F"
T

The above examples are demonstrated using a commandline interaction to conveniently present the examples. You may have a different way of implementation of
the interpreter, depending on the features provided by your programming language
as long it achieves the same purpose.