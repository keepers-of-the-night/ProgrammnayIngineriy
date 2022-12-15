student("Vasa", "Irina", "Petr", "Arzu").
man("Vasa").
man("Petr").
woman("Irina").
women("Arzu").
otlichnic("Arzu").
horoshist("Petr").
horoshist("Irina").
troechnic("Vasa").
molodci(X):-
    otlichnic(X); horoshist(X).
?-molodci(X).