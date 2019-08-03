import csv
from selenium import webdriver


f = open('vakif.csv', 'a')
w = csv.writer(f)
w.writerow([
    'Ad',
    'Adres',
    'Il / Ilce',
    'Tel / Faks',
])
f.close()


driver = webdriver.Chrome()
#driver.get("https://www.vgm.gov.tr/vakiflar/Sayfalar/Yeni-Vak%C4%B1f.aspx")
#driver.get("https://www.vgm.gov.tr/vakiflar/Sayfalar/Yabanc%C4%B1-Vak%C4%B1f.aspx")
#driver.get("https://www.vgm.gov.tr/vakiflar/Sayfalar/M%C3%BClhak-Vak%C4%B1f.aspx")
driver.get("https://www.vgm.gov.tr/vakiflar/Sayfalar/Cemaat-Vak%C4%B1flar%C4%B1.aspx")


but = driver.find_element_by_css_selector('input[type=submit]')

but.click()


page = 1

while True:
    print(page)
    f = open('vakif.csv', 'a')
    w = csv.writer(f)
    table = driver.find_element_by_css_selector('table')
    rows = table.find_elements_by_tag_name('tr')
    rows = rows[1:-2]
    for row in rows:
        ad, adres, ilce, tel = row.find_elements_by_tag_name('td')
        w.writerow([
            ad.text,
            adres.text,
            ilce.text,
            tel.text,
        ])
    f.close()
    page += 1
    try:
        link = table.find_element_by_link_text(str(page))
    except:
        links = table.find_elements_by_link_text('...')
        try:
            next_link = links[1]
        except:
            break
        else:
            next_link.click()
    else:
        link.click()


driver.close()
