import csv
import requests

f = open('koop.csv', 'w')
w = csv.writer(f)

w.writerow([
    'Id',
    'Unvani',
    'Turu',
    'Kurulus',
    'Merkezi',
])

f.close()

p=1
while True:
    print(p)
    f = open('koop.csv', 'a')
    writer = csv.writer(f)
    r = requests.post(
        'https://koopbis.gtb.gov.tr/Portal/Home/KoopKisaAraResult',
        data={
            'page': p,
            'pageSize': 1000,
        },
        cookies={
            'ASP.NET_SessionId': 'hh4tnynagwojrpleejzezsyd'
        }
    )
    for koop in r.json()['Data']['Items']:
        row = [
            koop['Id'],
            koop['Unvani'],
            koop['Turu'],
            koop['Kurulus'],
            koop['Merkezi'],
        ]
        writer.writerow(row)
    f.close()
    p += 1
    if p > r.json()['PageCount']:
        break


len(r.json()['Data']['Items'])
