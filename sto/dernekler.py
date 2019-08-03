import json
import csv
import requests

f = open('out.csv', 'a')
w = csv.writer(f)

w.writerow([
    'Ad',
    'Sayi',
    'Oran',
    'Plaka',
    'AnaNevisi',
    'telNo',
    'Mail',
    'WebSitesi',
    'FkSisKodPkNevi',
    'FKSisTeskilatPk',
    'SisKod',
    'KurumAd',
    'KurumAdres',
    'Sira',
    'BaskanAdSoyad',
    'FkSisCityInfoPk',
    'AltNevisString',
    'IsActive',
    'DtOlusturma',
    'DtDegistirme',
    'Olusturan',
    'Degistiren',
])

f.close()


def get_il(il, csv_writer):
    serializedData = json.dumps({
        'secilenTeskilatPk': il,
        'secilenIlcePk': '999999999',
        'neviler': '0',
        'altneviler': '0',
    })
    p = 1
    while True:
        r = requests.post(
            'https://derbis.dernekler.gov.tr/IstatistikDerneklerWeb/GetIlFaaliyetDernek',
            data={
                'page': p,
                'pageSize': 1000,
                'serializedData': serializedData,
            },
            verify=False,
        )
        for dernek in r.json()['Data']:
            row = [
                dernek['Ad'],
                dernek['Sayi'],
                dernek['Oran'],
                dernek['Plaka'],
                dernek['AnaNevisi'],
                dernek['telNo'],
                dernek['Mail'],
                dernek['WebSitesi'],
                dernek['FkSisKodPkNevi'],
                dernek['FKSisTeskilatPk'],
                dernek['SisKod'],
                dernek['KurumAd'],
                dernek['KurumAdres'],
                dernek['Sira'],
                dernek['BaskanAdSoyad'],
                dernek['FkSisCityInfoPk'],
                dernek['AltNevisString'],
                dernek['IsActive'],
                dernek['DtOlusturma'],
                dernek['DtDegistirme'],
                dernek['Olusturan'],
                dernek['Degistiren'],
            ]
            csv_writer.writerow(row)
        if p * 1000 >= r.json()['Total']:
            break
        p += 1

for il in range(35, 82):
    print(il)
    f = open('out35-81.csv', 'a')
    writer = csv.writer(f)
    get_il(il, writer)
    f.close()

f = open('out34.csv', 'a')
writer = csv.writer(f)
get_il(34, writer)
f.close()


len(r.json()['Data'])
r.json()['Errors']
