from imports import json, req
def login(username, password):
    useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    data={
        "identifiant": username,
        "motdepasse": password,
        "isReLogin": "false",
        "uuid": ""
    }
    send = 'data=' + json.dumps(data)
    request = req.post("https://api.ecoledirecte.com/v3/login.awp?v=3.43.0", headers={'User-Agent': useragent}, data=send)
    uid = str(request.json()['data']['accounts'][0]['id'])
    token = request.json()['token']
    return[uid, token]