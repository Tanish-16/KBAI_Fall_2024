from MonsterDiagnosisAgent import MonsterDiagnosisAgent

def test():
    #This will run your code against two initial test cases.
    test_agent = MonsterDiagnosisAgent()

    diseases = {"Alphaitis":
             {"A": "+", "B": "0", "C": "-", "D": "0", "E": "0", "F": "+", "G": "0", "H": "0", "I": "+",
              "J": "-", "K": "0", "L": "0", "M": "0", "N": "0", "O": "-", "P": "0", "Q": "0", "R": "0",
              "S": "0", "T": "0", "U": "0", "V": "0", "W": "0", "X": "0", "Y": "0", "Z": "+"},
            "Betatosis":
             {"A": "0", "B": "0", "C": "-", "D": "0", "E": "+", "F": "-", "G": "0", "H": "0", "I": "+",
              "J": "+", "K": "0", "L": "0", "M": "0", "N": "0", "O": "0", "P": "0", "Q": "0", "R": "-",
              "S": "0", "T": "0", "U": "0", "V": "0", "W": "0", "X": "0", "Y": "0", "Z": "-"},
            "Gammanoma":
             {"A": "0", "B": "+", "C": "+", "D": "+", "E": "+", "F": "+", "G": "0", "H": "0", "I": "0",
              "J": "0", "K": "0", "L": "0", "M": "0", "N": "0", "O": "0", "P": "0", "Q": "0", "R": "0",
              "S": "0", "T": "0", "U": "0", "V": "0", "W": "0", "X": "0", "Y": "0", "Z": "+"},
            "Deltaccol":
             {"A": "0", "B": "0", "C": "+", "D": "0", "E": "0", "F": "0", "G": "0", "H": "-", "I": "0",
              "J": "0", "K": "0", "L": "0", "M": "0", "N": "0", "O": "0", "P": "0", "Q": "0", "R": "0",
              "S": "0", "T": "0", "U": "0", "V": "0", "W": "0", "X": "0", "Y": "0", "Z": "-"},
            "Epsicusus":
             {"A": "0", "B": "0", "C": "+", "D": "0", "E": "0", "F": "0", "G": "0", "H": "0", "I": "+",
              "J": "+", "K": "0", "L": "0", "M": "0", "N": "0", "O": "0", "P": "0", "Q": "0", "R": "0",
              "S": "0", "T": "0", "U": "0", "V": "0", "W": "0", "X": "0", "Y": "0", "Z": "+"}}
    patient_1 = {"A": "+", "B": "0", "C": "-", "D": "0", "E": "+", "F": "0", "G": "0", "H": "0", "I": "+", "J": "0", "K": "0", "L": "0", "M": "0", "N": "0", "O": "-", "P": "0", "Q": "0", "R": "-", "S": "0", "T": "0", "U": "0", "V": "0", "W": "0", "X": "0", "Y": "0", "Z": "0"}
    patient_2 = {"A": "0", "B": "+", "C": "+", "D": "+", "E": "+", "F": "+", "G": "0", "H": "-", "I": "+", "J": "+", "K": "0", "L": "0", "M": "0", "N": "0", "O": "0", "P": "0", "Q": "0", "R": "0", "S": "0", "T": "0", "U": "0", "V": "0", "W": "0", "X": "0", "Y": "0", "Z": "+"}

    print(test_agent.solve(diseases, patient_1))
    print(test_agent.solve(diseases, patient_2))

if __name__ == "__main__":
    test()