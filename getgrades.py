from imports import json, req
from year import school_year
def get_grades(uid, token):
    useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    url = "https://api.ecoledirecte.com/v3/eleves/" + uid + "/notes.awp"
    data = {
        "anneeScolaire": school_year(),
    }
    send = 'data=' + json.dumps(data)
    request = req.post(url, headers={'X-Token': token, 'User-Agent': useragent}, params={'verbe': 'get'}, data=send)
    notes = {}
    for note in request.json()['data']['notes']:
        if not note['codeMatiere'] in notes:
            notes.update({
                note['codeMatiere']: {
                    'notes': {
                        note['devoir']: note['valeur'] + '/' + note['noteSur']
                    },
                    'moyenne': 0,
                    'coefTotal': 0
                }
            })
            if not note['enLettre'] and not note['nonSignificatif'] and note['valeur']:
                if ',' in str(note['valeur']):
                    note['valeur'] = note['valeur'].replace(",",".")
                notes[note['codeMatiere']].update({
                    'moyenne': float(note['valeur']) / int(note['noteSur']) * float(note['coef']),
                    'coefTotal': float(note['coef'])
                })
            if note['libelleMatiere'] != '':
                notes[note['codeMatiere']]['name'] = note['libelleMatiere']
            else:
                notes[note['codeMatiere']]['name'] = note['codeMatiere']
        else:
            notes[note['codeMatiere']]['notes'].update({
                note['devoir']: note['valeur'] + '/' + note['noteSur']
            })
            if not note['enLettre'] and not note['nonSignificatif'] and note['valeur']:
                if ',' in str(note['valeur']):
                    n = ''
                    for i in note['valeur']:
                        if i == ',':
                            i = '.'
                        n += i
                    note['valeur'] = n
                notes[note['codeMatiere']]['moyenne'] += float(note['valeur']) / int(note['noteSur']) * float(note['coef'])
                notes[note['codeMatiere']]['coefTotal'] += float(note['coef'])
    moyenne = {}
    for matiere in notes:
        if notes[matiere]['moyenne'] and notes[matiere]['coefTotal']:
            moyenne.update({
                matiere: notes[matiere]['moyenne'] / notes[matiere]['coefTotal'] * 20
            })
    return(notes, moyenne)