
import pickle
from Company import Company

with open('./code/company_data.pkl', 'rb') as input:
    company1 = pickle.load(input)
    print(company1.name)  # -> banana
    print(company1.value)  # -> 40

    company2 = pickle.load(input)
    print(company2.name) # -> spam
    print(company2.value)  # -> 42
