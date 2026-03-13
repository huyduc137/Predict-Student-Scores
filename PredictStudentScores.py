# %%
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# clean up data
data = pd.read_csv("StudentScore.xls", sep=',', quotechar='"')
colOne = data.columns[0]
dataNew = data[colOne].str.split(',', expand=True)
listCols = colOne.replace('"', '').split(',')
dataNew.columns = listCols
dataNew = dataNew.replace('"', '', regex=True)
colToConvert = ['math score', 'reading score', 'writing score']
dataNew[colToConvert] = dataNew[colToConvert].astype('int64')
# %%
# preprocessing
target = "math score"
x = dataNew.drop(target, axis=1)
y = dataNew[target]
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=42)
educationValues = ["some high school", "high school", "some college", 
                   "associate's degree", "bachelor's degree", "master's degree"]
lunchValues = x_train["lunch"].unique()
testValues = x_train["test preparation course"].unique()
genderValues = ["male", "female"]
num_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy='median')),
    ("scaler", StandardScaler())
])
ordinal_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy='most_frequent')),
    ("ordinal", OrdinalEncoder(categories=[educationValues, genderValues, lunchValues, testValues]))
])
nominal_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy='most_frequent')),
    ("nominal", OneHotEncoder(sparse_output=False))
])

preprocessor = ColumnTransformer(transformers=[
    ("num_features", num_transformer, ["reading score", "writing score"]),
    ("odinal_features", ordinal_transformer, ["parental level of education", "gender", "lunch", "test preparation course"]),
    ("nominal_features", nominal_transformer, ["race/ethnicity"])
])

reg = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])
reg.fit(x_train, y_train)
y_predict = reg.predict(x_test)
print("MAE {}".format(mean_absolute_error(y_test, y_predict)))
print("MSE {}".format(mean_squared_error(y_test, y_predict)))
print("R2 {}".format(r2_score(y_test, y_predict)))
# for i, j in zip(y_test, y_predict):
#     print("Actual {}. Predict {}".format(i, j))
# %%
