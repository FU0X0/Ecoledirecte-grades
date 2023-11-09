from imports import dumps, req
from year import school_year
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
                    'moyenne': 0,
                    'coefTotal': 0
                }
            })
            if i['libelleMatiere']:
                grades[i['codeMatiere']]['name'] = i['libelleMatiere']
            else:
                grades[i['codeMatiere']]['name'] = i['codeMatiere']
        if i['valeur']:
            grades[i['codeMatiere']]['notes'].update({
                i['devoir']: i['valeur'] + '/' + i['noteSur']
            })
        if not i['enLettre'] and not i['nonSignificatif'] and i['valeur']:
            i['valeur'] = i['valeur'].replace(",",".")
            grades[i['codeMatiere']]['moyenne'] += float(i['valeur']) / int(i['noteSur']) * float(i['coef'])
            grades[i['codeMatiere']]['coefTotal'] += float(i['coef'])
    average = {}
    for matiere in grades:
        if grades[matiere]['moyenne'] and grades[matiere]['coefTotal']:
            average.update({
                matiere: grades[matiere]['moyenne'] / grades[matiere]['coefTotal'] * 20
            })
    return(grades, average)