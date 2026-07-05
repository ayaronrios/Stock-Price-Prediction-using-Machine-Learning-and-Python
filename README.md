# Stock Price Prediction Using Machine Learning (Python)

An educational machine learning project that trains a **Linear Regression** model on historical stock market data from Yahoo Finance to predict the **next day's closing price**.

The project includes two ways to run the prediction pipeline:

* **Streamlit Web Application** (`app.py`) – Interactive interface for selecting stocks, training the model, and visualizing results.
* **Command-Line Script** (`stockprediction.py`) – Train the model, evaluate its performance, and save predictions from the terminal.

> **Disclaimer:** This project is intended for learning and experimentation only. It should not be used for financial or investment decisions.

---

## Features

* Download historical **OHLCV** stock data using Yahoo Finance (`yfinance`)
* Perform feature engineering using:

  * 5-day Moving Average (MA5)
  * 20-day Moving Average (MA20)
* Predict the **next day's closing price** using `Close.shift(-1)`
* Chronological train/test split:

  * First 80% for training
  * Last 20% for testing
* Train a **scikit-learn Linear Regression** model
* Evaluate performance using:

  * R² Score
  * Mean Squared Error (MSE)
  * Mean Absolute Error (MAE)
* Visualize actual vs. predicted prices
* Save the trained model and prediction results

---

## Repository Structure

```text
.
├── app.py                      # Streamlit web application
├── stockprediction.py          # Command-line prediction script
├── stock_prediction_model.pkl  # Saved trained model (generated)
├── predictions.csv             # Prediction results (generated)
├── requirements.txt            # Project dependencies
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

It is recommended to store generated artifacts inside an `outputs/` directory rather than the project root.

---

## Future Improvements

Some ideas to extend the project:

* Store generated files inside an `outputs/` directory
* Add `outputs/`, `*.pkl`, and generated CSV files to `.gitignore`
* Pin dependency versions in `requirements.txt` for reproducibility
* Add exception handling around `yfinance` downloads
* Validate downloaded data before training
* Use `st.cache_data` and `st.cache_resource` in the Streamlit application
* Replace `input()` with `argparse` for a more flexible CLI
* Support configurable:

  * Stock ticker
  * Date range
  * Output directory
* Refactor the code into reusable functions:

  * `load_data()`
  * `prepare_features()`
  * `train_model()`
  * `evaluate_model()`
* Add unit tests
* Experiment with more advanced models such as:

  * Random Forest
  * XGBoost
  * LSTM
* Implement proper time-series validation using walk-forward or backtesting techniques

---

## Contributing

Contributions are welcome.

Some beginner-friendly improvements include:

* Add a `.gitignore` file
* Populate `requirements.txt` with pinned package versions
* Create an `outputs/` directory for generated artifacts
* Add CLI arguments using `argparse`
* Improve documentation
* Refactor the project into reusable modules
* Add automated tests

If you have ideas for improving the project, feel free to open an issue or submit a pull request.



