from underline import underline
def print_grades(notes, moyenne):
    moyenneG = 0
    coefG = 0
    for matiere in notes:
        print('\n' + underline(notes[matiere]['name'] + ':'))
        for i in notes[matiere]['notes']:
            print(i + ': ' + str(notes[matiere]['notes'][i]))
        try:
            moyenneG += moyenne[matiere]
            coefG += 1
            print('\nMoyenne = {:.2f}/20\n'.format(moyenne[matiere]))
        except:
            print('\n')
    if coefG != 0:
        toPrint = 'Moyenne générale : {:.2f}/20'.format(moyenneG / coefG)
        print(underline(toPrint))