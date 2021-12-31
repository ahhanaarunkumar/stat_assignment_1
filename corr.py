import pandas as pd

df1= pd.read_csv("HouseData.csv")
# correlation matrix
df = df1.corr()

def correlation_func(df):
    dependant_variable = input("Enter the dependent variable:")
    var_list = []
    d= {}
    for i in df.index:
        d[i] =df[i].values.tolist()
        d[i]=dict(zip(df[i].index,d[i]))

    for j in d:  
        for k in d:
            if (j == k):
                continue
            elif abs(d[j][k]) >0.75:
                var_list.append(k)
                print(f'{j} and {k} are correlated')

    var_list.remove(dependant_variable)
    return var_list


print("Variables to be dropped:",correlation_func(df))
        
