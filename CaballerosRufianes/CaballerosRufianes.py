from logic import *

ACaballero = Symbol("A es un Caballero")
ARufian = Symbol("A es un Rufian")

BCaballero = Symbol("B es un Caballero")
BRufian = Symbol("B es un Rufian")

CCaballero = Symbol("C es un Caballero")
CRufian = Symbol("C es un Rufian")

# Primera prueba
# A dice "Soy ambos: Un Caballero y un Rufian."
knowledge0 = And(
	Biconditional(ACaballero,Not(ARufian)),
    Biconditional(ACaballero,And(ACaballero,ARufian))
)

# Puzzle 1
# A dice "Somos ambos rufianes."
# B no dice nada.
knowledge1 = And(
	Biconditional(ACaballero,Not(ARufian)),
    Biconditional(BCaballero,Not(BRufian)),
    Biconditional(ACaballero,And(ARufian,BRufian))
)

# Puzzle 2
# A dice "Somos del mismo tipo."
# B dice "Somos de tipo distinto."
knowledge2 = And(
	Biconditional(ACaballero,Not(ARufian)),
    Biconditional(BCaballero,Not(BRufian)),
    Biconditional(ACaballero,Or(And(ACaballero,BCaballero),And(ARufian,BRufian))),
    Biconditional(BCaballero,Not(Or(And(ACaballero,BCaballero),And(ARufian,BRufian))))
)

# Puzzle 3
# A dice o bien: "Soy un Caballero." o bien "Soy un Rufian.", pero no se sabe cuál de los dos dijo.
# B dice "A dijo 'Soy un Rufian'."
# B dice "C es un Rufian."
# C dice "A es un Caballero."
knowledge3 = And(
	Biconditional(ACaballero,Not(ARufian)),
    Biconditional(BCaballero,Not(BRufian)),
    Biconditional(CCaballero,Not(CRufian)),

    Biconditional(CCaballero,ACaballero), # C dice "A es un Caballero."
    Biconditional(BCaballero,CRufian),
    #para nosotros esto es lo necesari  Implication(ARufian,BRufian)
    # pero para que el algoritmo piense mas por el mismo
    Implication(BCaballero,Biconditional(ACaballero,ARufian))
)


def main():
    symbols = [ACaballero, ARufian, BCaballero, BRufian, CCaballero, CRufian]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
