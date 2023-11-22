import pandas as pd
import pickle
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Import the clean random sample of 10k data
df = pd.read_csv('/home/eugenehsiung/datasci_9_data_prep/model_dev2/data/processed/processed_female_teen_birth_rate.csv')
len(df)

# Dropping rows with missing values
df.dropna(inplace=True)
len(df)

# Define the features and the target variable
X = df.drop('birth_rate', axis=1)  # Features (all columns except 'birth_rate')
y = df['birth_rate']               # Target variable (birth_rate)

# Initializing the StandardScaler
scaler = StandardScaler()
scaler.fit(X) # Fit the scaler to the features and transform
X_scaled = scaler.transform(X) # Scaling the feature matrix
X_scaled
pickle.dump(scaler, open('model_dev2/models/scaler.sav', 'wb')) # Save the scaler for later use

# Splitting the scaled data into training, validation, and testing sets (70%, 15%, 15%)
X_train, X_temp, y_train, y_temp = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Checking the size of each set
(X_train.shape, X_val.shape, X_test.shape)

# Pkle the X_train for later use in explanation
pickle.dump(X_train, open('model_dev2/models/X_train.sav', 'wb'))
pickle.dump(X.columns, open('model_dev2/models/X_columns.sav', 'wb'))


