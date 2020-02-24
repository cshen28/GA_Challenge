#!/usr/bin/env python

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import cross_val_score

### CHEN: Cross_val_score is from sklearn.model_selection
### Thus it should be corrected to: from sklearn.model_selection import cross_val_score

# Load data
data = pd.read_csv('../data/train.csv')

# Setup data for prediction
y = data.SalaryNormalized
X = pd.get_dummies(data.ContractType)

# Setup model
model = LinearRegression()

# Evaluate model
scores = cross_val_score(model, X, y, cv=5, scoring='mean_absolute_error')
print(scores.mean())

### CHEN: To use mean_absolute_error scoring function, the proper string should be
### scoring = 'neg_mean_absolute_error'