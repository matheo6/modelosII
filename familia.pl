padrede('juan','maria').
padrede('pablo','juan').
padrede('pablo','marcela').
padrede('Luis','debora').
padrede('Lina','Carlos').
padrede('Mateo','Carlos').
padrede('William','Lina').
padrede('William','Luis').
padrede('matilde','William').
hijode(A,B) :- padrede(B,A).
abuelode(A,B) :- padrede(A,C), padrede(C,B).
bisabuelode(A,B) :- abuelode(A,C),padrede(C,B).
hermanode(A,B) :- padrede(C,A), padrede(C,B), A \== B.
primode(A,B) :- padrede(C,A),hermanode(C,D),padrede(D,B).
tiode(A,B):- hijode(B,C),hermanode(C,A).
casadocon(L,M) :- padrede(L,C),padrede(M,C),L\==M.
esfeliz(L,M):- casadocon(L,M).
familiarde(A,B) :- padrede(A,B).
familiarde(A,B) :- tiode(A,B).
familiarde(A,B) :- primode(A,B).
familiarde(A,B) :- bisabuelode(A,B).
familiarde(A,B) :- casadocon(A,B).
familiarde(A,B) :- abuelode(A,B).
familiarde(A,B) :- hermanode(A,B).