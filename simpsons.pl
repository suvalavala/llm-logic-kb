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

