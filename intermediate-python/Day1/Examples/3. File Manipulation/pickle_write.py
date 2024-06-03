import pickle
from Company import Company

with open('./code/company_data.pkl', 'wb') as output:
    company1 = Company('banana', 40)
    pickle.dump(company1, output)

    company2 = Company('spam', 42)
    pickle.dump(company2, output)

del company1
del company2
