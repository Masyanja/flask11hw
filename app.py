from flask import Flask, render_template
from utils import *


app = Flask(__name__)

@app.route("/")
def page_index():#вызываем всех функции, кот мы написали в утилиты
    candidate_json = load_candidates_from_json('candidates.json')#создаем переменную, где будет хранится все содержимое candidates.json
    return render_template('list.html', candidates=candidate_json)

@app.route("/candidate/<int:id>")
def page_candidate(id):#со страницы page_index переход на всю инфо на 1ого кандидата по id
    candidate_info = get_candidate(id)#создаем переменную, в кот через функцию get_candidate записываем информацию по одному кандидату
    return render_template('card.html', candidate=candidate_info) #candidate - переменная в шаблоне, присваеваем инфо из функции get_candidate
    print(candidate_info)

@app.route("/search/<candidate_name>")
def page_candidate_name(candidate_name):
    candidate_name = get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidate_name, count=len(candidate_name))

@app.route("/skill/<skill_name>")
def page_skill(skill_name):
    candidates_skill = get_candidates_by_skill(skill_name)
    return render_template('skill.html', candidates=candidates_skill, skill=skill_name, count=len(candidates_skill))




app.run()