from faker import Faker
import csv

output = open('datos.csv', mode='w', encoding='utf-8')
csv_writer = csv.writer(output)
faker = Faker()
columns =['nombre','edad','direccion','ciudad','departamento','zip','longitud','latitud']
csv_writer.writerow(columns)
for _ in range(1000):
    csv_writer.writerow(
        [
        faker.name(),
        faker.random_int(min=15,max=90, step=1),
        faker.street_address(),
        faker.city(),
        faker.state(),
        faker.zipcode(),
        faker.longitude(),
        faker.latitude()
        ]
    )
