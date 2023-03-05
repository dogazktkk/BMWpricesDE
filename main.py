from ScrapeBMWprices import ScrapeBMWprices
from email_html import email_html
from send_mail import send_email


i_serie_list, x_serie_list, m_serie_list, eight_serie_list, seven_serie_list, six_serie_list, five_serie_list, four_serie_list, three_serie_list, two_serie_list, one_serie_list, z4_serie_list = ScrapeBMWprices()

car_list = []

for i in range(len(i_serie_list)):
    car_list.append(i_serie_list[i].replace("Konfigurieren & Preise","").replace("Fahrzeuginformationen","").replace("*","").replace("\n","<br>"))

for i in range(len(x_serie_list)):
    car_list.append(x_serie_list[i].replace("Konfigurieren & Preise","").replace("Fahrzeuginformationen","").replace("*","").replace("\n","<br>"))

for i in range(len(m_serie_list)):
    car_list.append(m_serie_list[i].replace("Konfigurieren & Preise","").replace("Fahrzeuginformationen","").replace("*","").replace("\n","<br>"))

for i in range(len(eight_serie_list)):
    car_list.append(eight_serie_list[i].replace("Konfigurieren & Preise","").replace("Fahrzeuginformationen","").replace("*","").replace("\n","<br>"))

for i in range(len(seven_serie_list)):
    car_list.append(seven_serie_list[i].replace("Konfigurieren & Preise","").replace("Fahrzeuginformationen","").replace("*","").replace("\n","<br>"))

for i in range(len(six_serie_list)):
    car_list.append(six_serie_list[i].replace("Konfigurieren & Preise","").replace("Fahrzeuginformationen","").replace("*","").replace("\n","<br>"))

for i in range(len(five_serie_list)):
    car_list.append(five_serie_list[i].replace("Konfigurieren & Preise","").replace("Fahrzeuginformationen","").replace("*","").replace("\n","<br>"))

for i in range(len(four_serie_list)):
    car_list.append(four_serie_list[i].replace("Konfigurieren & Preise","").replace("Fahrzeuginformationen","").replace("*","").replace("\n","<br>"))

for i in range(len(three_serie_list)):
    car_list.append(three_serie_list[i].replace("Konfigurieren & Preise","").replace("Fahrzeuginformationen","").replace("*","").replace("\n","<br>"))

for i in range(len(two_serie_list)):
    car_list.append(two_serie_list[i].replace("Konfigurieren & Preise","").replace("Fahrzeuginformationen","").replace("*","").replace("\n","<br>"))

for i in range(len(one_serie_list)):
    car_list.append(one_serie_list[i].replace("Konfigurieren & Preise","").replace("Fahrzeuginformationen","").replace("*","").replace("\n","<br>"))

for i in range(len(z4_serie_list)):
    car_list.append(z4_serie_list[i].replace("Konfigurieren & Preise","").replace("Fahrzeuginformationen","").replace("*","").replace("\n","<br>"))


content = email_html.format(car_list[0], car_list[1], car_list[2], car_list[3], car_list[4], car_list[5], car_list[6], car_list[7], car_list[8], car_list[9], car_list[10], car_list[11], car_list[12], car_list[13], car_list[14], car_list[15], car_list[16], car_list[17], car_list[18], car_list[19], car_list[20], car_list[21], car_list[22], car_list[23], car_list[24], car_list[25], car_list[26], car_list[27], car_list[28], car_list[29], car_list[30], car_list[31], car_list[32], car_list[33], car_list[34], car_list[35])
send_email(content, "BMW DE prices", "dogao@skoda.com.tr")
