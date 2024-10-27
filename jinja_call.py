from jinja2 import Template
import csv

template_content = open('property.py.jinja').read()
template = Template(template_content)

factor_combinations = []
for min in range(-1000, 1000, 100):
    for max in range(-1000, 1000, 100):
        for repetitions in range(10, 1000, 50):
            print(min, max, repetitions)
            factor_combinations.append({"min": min, "max": max, "repetitions": repetitions})

en_tete = ["min", "max", "repetitions", "result"]

with open("results.csv", mode='w', newline='') as fichier_csv:
    writer = csv.writer(fichier_csv)
    writer.writerow(en_tete)
for factors in factor_combinations:
    generated_code = template.render(factors)
    exec(generated_code)
