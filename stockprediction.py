import warnings
warnings.filterwarnings("ignore")

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import joblib

#from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# -------------------------------
# Get Stock Symbol
# -------------------------------
stock = input("Enter Stock Symbol (Example: AAPL, MSFT, TSLA): ").upper()

print("\nDownloading stock data...")

df = yf.download(
    stock,
    start="2020-01-01",
    end="2025-01-01",
    auto_adjust=True
)

# -------------------------------
# Handle MultiIndex Columns
# -------------------------------
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

if df.empty:
    print("No stock data found.")
    exit()

print("\nFirst Five Records")
print(df.head())


# -------------------------------
# Stock Information
# -------------------------------
print("\n==============================")
print("STOCK INFORMATION")
print("==============================")
print(f"Stock Symbol : {stock}")
print(f"Start Date   : {df.index.min().date()}")
print(f"End Date     : {df.index.max().date()}")
print(f"Total Records: {len(df)}")

# -------------------------------
# Feature Engineering
# -------------------------------
df["MA5"] = df["Close"].rolling(5).mean()
df["MA20"] = df["Close"].rolling(20).mean()

# Target = Tomorrow's Close
df["Target"] = df["Close"].shift(-1)

# Remove missing values
df.dropna(inplace=True)

# -------------------------------
# Input Features
# -------------------------------
features = [
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",
    "MA5",
    "MA20"
]

X = df[features]
y = df["Target"]

# -------------------------------
# Train-Test Split
# -------------------------------
# Use the first 80% of the data for training
split = int(len(X) * 0.8)

X_train = X.iloc[:split]
X_test = X.iloc[split:]

y_train = y.iloc[:split]
y_test = y.iloc[split:]

print("\n==============================")
print("DATASET SPLIT")
print("==============================")
print(f"Training Samples : {len(X_train)}")
print(f"Testing Samples  : {len(X_test)}")

# -------------------------------
# Train Model
# -------------------------------
model = LinearRegression()
model.fit(X_train, y_train)
# Save trained model
joblib.dump(model, "stock_prediction_model.pkl")
print("\nModel saved as stock_prediction_model.pkl")



# -------------------------------
# Prediction
# -------------------------------
predictions = model.predict(X_test)

# -------------------------------
# Evaluation
# -------------------------------
r2 = r2_score(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)

print("\n==============================")
print("MODEL PERFORMANCE")
print("==============================")
print(f"Accuracy (R² Score): {r2:.4f}")
print(f"Mean Squared Error : {mse:.4f}")
print(f"Mean Absolute Error: {mae:.4f}")
print("\n==============================")
print("FEATURE IMPORTANCE")
print("==============================")

importance = pd.DataFrame({
    "Feature": features,
    "Coefficient": model.coef_
})

print(importance)



# -------------------------------
# Predict Next Day Price
# -------------------------------
latest_features = X.iloc[[-1]]

next_price = model.predict(latest_features)[0]

print("\n==============================")
print("NEXT DAY PREDICTION")
print("==============================")
print(f"Latest Closing Price      : {df['Close'].iloc[-1]:.2f}")
print(f"Predicted Next Day Price  : {next_price:.2f}")




# -------------------------------
# Actual vs Predicted Graph
# -------------------------------
plt.figure(figsize=(14,6))

plt.plot(
    y_test.index[-50:],
    y_test.values[-50:],
    label="Actual Price",
    linewidth=2
)

plt.plot(
    y_test.index[-50:],
    predictions[-50:],
    '--',
    label="Predicted Price",
    linewidth=2
)

plt.title(f"{stock} Stock Price Prediction")
plt.xlabel("Date")
plt.ylabel("Closing Price ($)")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# -------------------------------
# Prediction Results with Dates
# -------------------------------
results = pd.DataFrame({
    "Date": y_test.index,
    "Actual Price": y_test.values,
    "Predicted Price": predictions
})

results["Difference"] = results["Actual Price"] - results["Predicted Price"]
results = results.round(2)

print("\n========================================")
print(" FIRST 10 TEST PREDICTIONS")
print("========================================\n")

print(results.head(10))

results.to_csv("predictions.csv", index=False)

print("\nPredictions have been saved as 'predictions.csv'.")

print("\n========================================")
print("PROJECT COMPLETED SUCCESSFULLY")
print("========================================")