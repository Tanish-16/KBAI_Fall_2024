class MonsterClassificationAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass

    def solve(self, samples, new_monster):
        monster_attributes = {}
        for sample in samples:
            is_monster = sample[1]
            if is_monster is True:
                attributes = sample[0]
                for key, value in attributes.items():
                    if key not in monster_attributes:
                        monster_attributes[key] = [value]
                    else:
                        if value not in monster_attributes[key]:
                            monster_attributes[key].append(value)

        # print(monster_attributes)
        # print(new_monster)
        cnt = 0
        for key, value in new_monster.items():
            if value in monster_attributes[key]:
                cnt += 1
        # print(cnt)
        if cnt >= 10:
            return True
        return False