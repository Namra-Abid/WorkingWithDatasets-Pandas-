from urllib.request import urlretrieve
# urlretrieve('https://hub.jovian.ml/wp-content/uploads/2020/09/italy-covid-daywise.csv',
#             'italy-covid-daywise.csv')
import pandas as pd
covid_df = pd.read_csv('italy-covid-daywise.csv')
#print(covid_df)
#s=(covid_df.info())
d=covid_df.describe()
#print(d)
#print(covid_df['new_cases'])
#print(covid_df['new_cases'][246])=print(covid_df.at[246,'new_cases'])
#print(covid_df.at[246,'new_cases'])
#print(covid_df.new_cases)  # same as covid_df['new_cases']

first_five_rows=covid_df.head(5)
last_five_rows=covid_df.tail(5)
data_between=covid_df.loc[107:115]
#print(data_between)
random_sample_of_data=covid_df.sample(15)
#print(random_sample_of_data)
first_appearence_of_test=covid_df.new_tests.first_valid_index()
#print(first_appearence_of_test)
total_cases=covid_df.new_cases.sum()
total_death=covid_df.new_deaths.sum()

death_ratio=total_death/total_cases*100
#print("The death ratio is : {} %".format(death_ratio))

initial_tests=935310
total_test=initial_tests+covid_df.new_tests.sum()
#print(total_test)
positive_results_of_tests=total_cases/total_test*100
#print("{} % cases are tested positive ".format(positive_results_of_tests))
