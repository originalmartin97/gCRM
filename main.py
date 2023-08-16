import csv
import smtplib
import os
import time


def send_email(email, name, template_content):
    """Sends an email to the specified address with the specified name and template content."""
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("originalmartin97@gmail.com", "zklybkojdcacniof")

    message = "Subject: MetLife Zrt. (Győr)\n\n"
    message += template_content
    message = message.encode("utf-8")

    server.sendmail("originalmartin97@gmail.com", email, message)
    server.quit()


if __name__ == "__main__":
    with open("./potential_customers_insurance.csv", "r+") as csvfile:
        lines = []
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            temp = row
            if row[2] != "Sent":
                email = row[1]
                name = row[0]
                template_content = "Kedves {},\n\na nevem Takács Martin, én egyike vagyok a MetLife (Győr) kapcsolatfelvételért és az Élet-, Baleset- és Egészségbiztosítások szolgáltatásáért felelős munkatársainak.\n\nÉszleltük, hogy korábban az egyik hirdetésünk által megadta az elérhetőségét, és érdeklődött a személyi biztosításokat tartalmazó szolgáltatásaink iránt. Ezért úgy gondoltuk, hogy felvesszük Önnel a kapcsolatot.\n\nAmennyiben aktuálisan érdekli valamely szolgáltatásunk, kérem, töltse ki az alábbi kérdőívet. A kérdőív kitöltése nem kötelező, de előzetesen segít nekünk abban, hogy jobban megismerjük az igényeit, és megfelelő ajánlatot tudjunk adni, majd felkeresni Önt a későbbiekben, lehetőségeink szerint személyesen vagy telefonon keresztül.\n\nValamint lehetősége van minket megkeresni SMS-ben és telefonon az alábbi számon:\nTakács Martin: +36300822050\n\nA kérdőív kitöltését az alábbi linkre kattintva tudja elérni: https://docs.google.com/forms/d/e/1FAIpQLSeVgd5Wkci3cEhzBUYNP9d7_GJXjp_d3kWJc0wObPUXGBwlfg/viewform?usp=sf_link\n\nHa bármilyen kérdése van vagy más szolgáltatásaink után szeretne érdeklődni, kérjük, ne habozzon kapcsolatba lépni velünk a megadott telefonszámon vagy az originalmartin97@gmail.com címen keresztül.\n\n(MetLife - Győr; Élet-, Baleset- és Egészségbiztosítás)\n\nÜdvözlettel,\nTakács Martin".format(
                    name
                )
                send_email(email, name, template_content)
                time.sleep(1)
                temp[2] = "Sent"

            lines.append(temp)
        csvfile.close()
        os.remove("./potential_customers_insurance.csv")

        with open("./potential_customers_insurance.csv", "w", newline="") as newCsvFile:
            writer = csv.writer(newCsvFile, delimiter=",")

            # Write the rows to the CSV file using writerows().

            writer.writerows(lines)
            newCsvFile.close()
