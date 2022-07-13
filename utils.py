import json
# with open("candidates.json") as f:
#     candidates_json = json.load(f)


def load_candidates_from_json(file):#переводим json file в словарь
    with open(file) as f:
        candidates_json = json.load(f)
    return candidates_json #возвращает и больше ничего не делает

def get_candidate(candidate_id):
    candidates_json = load_candidates_from_json("candidates.json")#Нам нужно вызвать функцию и записать ее значения в переменную
    for candidate in candidates_json:
        if candidate_id == candidate['id']:
            return candidate


def get_candidates_by_name(candidate_name):
    candidate_json = load_candidates_from_json("candidates.json")
    candidate_name_list = []
    for candidate in candidate_json:
        if candidate_name.lower() in candidate['name'].lower():
            candidate_name_list.append(candidate)
    return candidate_name_list

def get_candidates_by_skill(skill_name):
    candidate_json = load_candidates_from_json("candidates.json")
    candidate_skill_list = []
    for candidate in candidate_json:
        if skill_name.lower() in candidate['skills'].lower():
            candidate_skill_list.append(candidate)
    return candidate_skill_list

print(load_candidates_from_json("candidates.json"))
print(get_candidate(3))
#print(get_candidates_by_name('Burt Stein'))
print(get_candidates_by_skill('Python'))