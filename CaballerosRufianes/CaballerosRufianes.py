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
	# TODO
)

# Puzzle 1
# A dice "Somos ambos rufianes."
# B no dice nada.
knowledge1 = And(
	# TODO
)

# Puzzle 2
# A dice "Somos del mismo tipo."
# B dice "Somos de tipo distinto."
knowledge2 = And(
	# TODO
)

# Puzzle 3
# A dice o bien: "Soy un Caballero." o bien "Soy un Rufian.", pero no se sabe cuál de los dos dijo.
# B dice "A dijo 'Soy un Rufian'."
# B dice "C es un Rufian."
# C dice "A es un Caballero."
knowledge3 = And(
	# TODO  

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
