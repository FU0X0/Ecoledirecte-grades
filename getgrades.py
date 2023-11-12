from imports import dumps, req
from year import school_year
from average import Avg
def get_grades(uid, token):
    useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    url = f"https://api.ecoledirecte.com/v3/eleves/{uid}/notes.awp"
    data = {
        "anneeScolaire": school_year(),
    }
    send = 'data=' + dumps(data)
    request = req.post(url, headers={'X-Token': token, 'User-Agent': useragent}, params={'verbe': 'get'}, data=send)
    grades = {}
    for i in request.json()['data']['notes']:
        if not i['codeMatiere'] in grades:
            grades.update({
                i['codeMatiere']: {
                    'notes': {},
                    'moyenne': Avg()
                }
            })
            if i['libelleMatiere']:
                grades[i['codeMatiere']]['name'] = i['libelleMatiere']
            else:
                grades[i['codeMatiere']]['name'] = i['codeMatiere']
        if i['valeur'] and not i['enLettre']:
            grades[i['codeMatiere']]['notes'].update({
                i['devoir']: f"{i['valeur']}/{i['noteSur']}"
            })
        elif i['valeur'] and i['enLettre']:
            grades[i['codeMatiere']]['notes'].update({
                i['devoir']: i['valeur']
            })
        if not i['enLettre'] and not i['nonSignificatif'] and i['valeur']:
            i['valeur'] = i['valeur'].replace(",",".")
            grades[i['codeMatiere']]['moyenne'].add(i['valeur'], i['noteSur'], i['coef'])
    average = {}
    for matiere in grades:
        if grades[matiere]['moyenne'].get():
            average.update({
                matiere: grades[matiere]['moyenne'].get()
            })
    return(grades, average)