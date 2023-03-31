import pickle
from person import Person
from linkedin_scraper import Contact


with open(r"cyril.dill", "rb") as input_file:
        cirill= pickle.load(input_file)

print(cirill)
print(cirill.companies)

