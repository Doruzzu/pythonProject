
""" The function called proportion_of_education which returns the proportion of children in the dataset who had a mother
with the education levels equal to less than high school (<12), high school (12),
more than high school but not a college graduate (>12) and college degree."""

def proportion_of_education():
    import pandas as pd
    data = pd.read_csv('NISPUF17.csv')

    d = {"less than high school": 0.0,
         "high school": 0.0,
         "more than high school but not college": 0.0,
         "college": 0.0}

    d['less than high school'] = len(data[data['EDUC1'] == 1]) / len(data)
    d["high school"] = len(data[data['EDUC1'] == 2]) / len(data)
    d["more than high school but not college"] = len(data[data['EDUC1'] == 3]) / len(data)
    d["college"] = len(data[data['EDUC1'] == 4]) / len(data)

    return d

# the relationship between being fed breastmilk as a child and getting a seasonal influenza vaccine from a healthcare provider.
#Return a tuple of the average number of influenza vaccines for those children we know received breastmilk as a child and those who know did not."""

def average_influenza_doses():
    import pandas as pd
    data = pd.read_csv('NISPUF17.csv')

    vaccine_yes = data[data['CBF_01'] == 1]
    vaccine_no = data[data['CBF_01'] == 2]
    return (vaccine_yes['P_NUMFLU'].mean(), vaccine_no['P_NUMFLU'].mean())

#Calculate the ratio of the number of children who contracted chickenpox but were vaccinated against it (at least one varicella dose) versus
# those who were vaccinated but did not contract chicken pox. Return results by sex.
def chickenpox_by_sex():
    import pandas as pd
    data = pd.read_csv('NISPUF17.csv')
    d = {}

    vaccinated = data[data['P_NUMVRC'] >= 1]
    vaccinated_male = vaccinated[vaccinated['SEX'] == 1]
    vaccinated_female = vaccinated[vaccinated['SEX'] == 2]

    d['male'] = len(vaccinated_male[vaccinated_male['HAD_CPOX'] == 1]) / len(
        vaccinated_male[vaccinated_male['HAD_CPOX'] == 2])
    d['female'] = len(vaccinated_female[vaccinated_female['HAD_CPOX'] == 1]) / len(
        vaccinated_female[vaccinated_female['HAD_CPOX'] == 2])
    return d


def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd

    data = pd.read_csv('NISPUF17.csv')


    df = pd.DataFrame({"had_chickenpox_column": np.random.randint(1, 3, size=(100)),"num_chickenpox_vaccine_column": np.random.randint(0, 6, size=(100))})


    corr, pval = stats.pearsonr(df["had_chickenpox_column"], df["num_chickenpox_vaccine_column"])


    vacc = data[data['P_NUMVRC'] >= 0]
    yes_no = vacc[(vacc['HAD_CPOX'] >= 1) & (vacc['HAD_CPOX'] <= 2)]
    corr_data, pval_data = stats.pearsonr(yes_no['HAD_CPOX'], yes_no['P_NUMVRC'])
    return corr_data

print(corr_chickenpox())