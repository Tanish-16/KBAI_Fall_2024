from itertools import combinations
import string

class MonsterDiagnosisAgent:
    def __init__(self):
        # If you want to do any initial processing, add it here.
        pass

    def solve(self, diseases, patient):
        num_disease = len(diseases)
        disease_keys = list(diseases.keys())
        for i in range(num_disease):
            subset_len = i + 1
            subsets = list(combinations(disease_keys, subset_len))
            for subset in subsets:
                vitamin_levels = {alphabet : 0 for alphabet in string.ascii_uppercase}
                for disease in subset:
                    vitamins = diseases[disease]
                    for vitamin in list(vitamins.keys()):
                        val = vitamins[vitamin]
                        if val == '+':
                            vitamin_levels[vitamin] += 1
                        elif val == '-':
                            vitamin_levels[vitamin] -= 1

                for vitamin in vitamin_levels:
                    if vitamin_levels[vitamin] > 0:
                        vitamin_levels[vitamin] = "+"
                    elif vitamin_levels[vitamin] < 0:
                        vitamin_levels[vitamin] = "-"
                    else:
                        vitamin_levels[vitamin] = "0"
                # print(vitamin_levels)
                if vitamin_levels == patient:
                    return subset


        return "Hi"

