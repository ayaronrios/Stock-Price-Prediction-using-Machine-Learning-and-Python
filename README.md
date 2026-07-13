# Stock Price Prediction Using Machine Learning and Python

An educational machine learning project that trains a **Linear Regression** model on historical stock market data from Yahoo Finance to predict the **next day's closing price**.

The project includes two ways to run the prediction pipeline:

* **Streamlit Web Application** (`app.py`) – Interactive interface for selecting stocks, training the model, and visualizing results.
* **Command-Line Script** (`stockprediction.py`) – Train the model, evaluate its performance, and save predictions from the terminal.

> **Disclaimer:** This project is intended for learning and experimentation only. It should not be used for financial or investment decisions.
> 
---

## 🎥 Demo

Watch the Streamlit web application demo:

[View Website Demo](demo/website-demo.mp4)

The demo shows the process of selecting a stock, training the machine learning model, generating predictions, and visualizing the results.

---

## Features

* Download historical **OHLCV** stock data from Yahoo Finance using `yfinance`
* Perform feature engineering using:
  * 5-day Moving Average (MA5)
  * 20-day Moving Average (MA20)
* Predict the **next day's closing price** using supervised learning
* Apply a chronological train/test split:
  * 80% training data
  * 20% testing data
* Train a **scikit-learn Linear Regression** model
* Evaluate model performance using:
  * R² Score
  * Mean Squared Error (MSE)
  * Mean Absolute Error (MAE)
* Visualize actual vs. predicted stock prices
* Save trained model and prediction results for future use

---

## Repository Structure

```text
.
├── app.py                      # Streamlit web application
├── stockprediction.py          # Command-line prediction script
├── stock_prediction_model.pkl  # Saved trained model (generated)
├── predictions.csv             # Prediction results (generated)
├── requirements.txt            # Project dependencies
├── demo/
│   └── website-demo.mp4        # Application demo video
└── README.md                   # Project documentation
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ayaronrios/Stock-Price-Prediction-using-Machine-Learning-and-Python.git
cd Stock-Price-Prediction-using-Machine-Learning-and-Python
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the environment:

**macOS/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` has not been populated yet:

```bash
pip install streamlit yfinance pandas matplotlib scikit-learn joblib
```

---

## Usage

### Streamlit Web Application (Recommended)

Launch the interactive interface:

```bash
streamlit run app.py
```

The application allows you to:

* Select a stock ticker
* Download historical data
* Train the model
* View evaluation metrics
* Visualize predictions
* Download prediction results as a CSV file

---

### Command-Line Version

Run:

```bash
python stockprediction.py
```

When prompted, enter a stock ticker such as:

```text
AAPL
```

The script will:

* Download historical data
* Train the model
* Display evaluation metrics
* Plot actual vs. predicted prices
* Save the trained model and predictions

---

## Output Files

After execution, the following files are generated:

| File                         | Description                                      |
| ---------------------------- | ------------------------------------------------ |
| `stock_prediction_model.pkl` | Serialized trained Linear Regression model       |
| `predictions.csv`            | Actual vs. predicted prices for the test dataset |
| `demo/website-demo.mp4`      | Streamlit application demonstration video       |

It is recommended to store generated artifacts inside an `outputs/` directory rather than the project root.

---

## Roadmap

### Completed
- ✅ Linear Regression model
- ✅ Streamlit web interface
- ✅ Yahoo Finance integration
- ✅ Model evaluation metrics
- ✅ CSV export

### Planned
- ⏳ Random Forest and XGBoost models
- ⏳ LSTM-based time series forecasting
- ⏳ Additional technical indicators (RSI, MACD, Bollinger Bands)
- ⏳ Hyperparameter tuning
- ⏳ Walk-forward validation
- ⏳ Docker support
- ⏳ Unit tests




