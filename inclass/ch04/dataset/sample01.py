import pandas as pd

covid_file_path = 'data_bar.csv'  # 같은 폴더에 있으니까 이렇게 가능
df = pd.read_csv(covid_file_path, sep='|')

print(df)
