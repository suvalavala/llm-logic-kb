# LLM Logic Knowledge Base – Prolog + Python

This repository contains a sample logic knowledge base modeled in Prolog and tested using both SWI-Prolog and a Python-based interpreter (`pylog`). It is part of a logic reasoning exploration for integrating symbolic logic with LLM workflows.

## Contents

- `simpsons.pl`: A Prolog file defining the knowledge base (facts and rules)
- `test_pylog.py`: Python script using `pylog` to load and query the same knowledge
- `README.md`: Setup and usage instructions

## Knowledge Base

The KB contains 10+ facts and 1 rule related to the Simpson family. It defines parent relationships, gender, and includes a `grandparent` rule based on composition of `parent/2`.

### Prolog Sample:
```prolog
parent(homer, bart).
parent(homer, lisa).
parent(marge, bart).
parent(marge, lisa).
parent(abraham, homer).
parent(mona, homer).
male(homer).
male(bart).
female(lisa).
female(marge).

grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
