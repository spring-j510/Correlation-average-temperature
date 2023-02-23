import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor as RFR
from sklearn.model_selection import train_test_split, GridSearchCV
import csv
import pandas as pd
import glob

def convert(table):
    for i in range(len(table[3])):
        if table[4][i] != "":
            table[3][i] = table[3][i] + table[4][i]
        if table[5][i] == "":
            table[5][i] = table[3][i]
    del table[:6]

    return table

Train_files = (glob.glob('Train_data/*.csv'))
Test_file = (glob.glob('Test_data/*.csv'))
print(Train_files,Test_file)

drop_list = ["年月","品質情報","均質番号","現象なし情報"]

df_train_marge = pd.DataFrame()

for i in range(len(Train_files)):
    train_table = []
    filename = Train_files[i]
    with open(filename,'r',encoding='cp932') as f:
        reader = csv.reader(f)
        for line in reader:
            train_table.append(line)
    column = train_table[5]

    train_table = convert(train_table)

    df_train = pd.DataFrame(train_table,columns=column)
    df_train = df_train.drop(drop_list,axis=1)

    if i == 0:
        df_train_marge = df_train
    else:
        df_train_marge = pd.concat([df_train_marge, df_train])
df_train_marge = df_train_marge.replace([""], [0])

test_table = []

filename = Test_file[0]
with open(filename,'r',encoding='cp932') as f:
    reader = csv.reader(f)
    for line in reader:
        test_table.append(line)

column = test_table[5]
test_table = convert(test_table)

df_test = pd.DataFrame(test_table,columns=column)
Horizontal_axis = df_test["年月"]
df_test = df_test.drop(drop_list,axis=1)

df_test = df_test.replace([""], [0])

train_x = df_train_marge.drop('平均気温(℃)', axis=1)
train_y = df_train_marge['平均気温(℃)']
test_x = df_test.drop('平均気温(℃)', axis=1)
test_y = df_test['平均気温(℃)']


random_forest = RFR(
    n_estimators = 15,
    random_state = 42,
    n_jobs = 1,
    min_samples_split = 10,
    max_depth = 10,
)
random_forest.fit(train_x, train_y)

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# Train
y_train_pred = random_forest.predict(train_x)

# Test
y_test_pred = random_forest.predict(test_x)

print('RMSE Train: %.2f, Test: %.2f' % (
        mean_squared_error(train_y, y_train_pred, squared=False), # train
        mean_squared_error(test_y, y_test_pred, squared=False)    # test
        ))

print('R^2 Train: %.2f, Test: %.2f' % (
        r2_score(train_y, y_train_pred), # train
        r2_score(test_y, y_test_pred)    # test
    ))

test_y_list = []
for i in test_y:
    float_i = float(i)
    test_y_list.append(float_i)

test_y = np.array(test_y_list)

x = (Horizontal_axis)
y1 = test_y
y2 = y_test_pred

plt.figure(figsize=(16,9))
plt.plot(x,y1, marker="o", color = "red", linestyle = "--", label="Measured_value")
plt.plot(x,y2, marker="v", color = "blue", linestyle = ":", label="Predicted_value")
plt.title('Measured and predicted value graph',fontsize=20)
plt.xlabel('month',fontsize=15)
plt.ylabel('Temperature',fontsize=15)
plt.tick_params(labelsize = 15)
plt.legend()
plt.savefig("result.png", format="png")