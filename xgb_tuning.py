
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV   #Perforing grid search

train = pd.read_csv('train_modified.csv')
target = (train['target'] > 0).astype(int)
train.drop('targer', axis=1, inplace=True)

param_test1 = {
 'max_depth':[3, 5, 7],
 'min_child_weight':[3,5,7],
 'gamma': [i / 10.0 for i in range(0, 5)],
 'subsample':[i/10.0 for i in range(6,10)],
 'colsample_bytree':[i/10.0 for i in range(6,10)],
 'objective': ['binary:logistic']
}
model = XGBClassifier()
gsearch1 = GridSearchCV(estimator = XGBClassifier(), param_grid = param_test1, scoring='roc_auc',n_jobs=-1, cv=5, verbose=10)
gsearch1.fit(train,target)
print(gsearch1.best_params_, gsearch1.best_score_)