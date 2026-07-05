# Stock Price Prediction Using Machine Learning (Python)

A small project that demonstrates using historical stock data from Yahoo Finance to train a simple Linear Regression model and predict the next-day closing price. It includes two entry points:

- `app.py` — an interactive Streamlit app for selecting a stock, training a Linear Regression model on historical data, showing evaluation metrics and plots, and downloading prediction results.
- `stockprediction.py` — a command-line script that downloads historical data, trains the same Linear Regression model, prints metrics and saves `predictions.csv` and `stock_prediction_model.pkl`.

This repository is intended for learning and demonstration purposes, not for financial advice.

## Stack
- Language(s): Python 3.x
- Framework / runtime: Streamlit (for the web app)
- Notable libraries: yfinance, pandas, scikit-learn, matplotlib, joblib

## Project structure
```text
app.py                 # Streamlit app: interactive UI, model training & visualization
stockprediction.py     # CLI script: train model, print metrics, plot, save predictions
stock_prediction_model.pkl  # Trained LinearRegression model (binary) — consider removing from repo
predictions.csv        # Example output of predictions (stored in repo)
requirements.txt       # (empty) list dependencies here
README.md              # This file (added/updated)
```

How it fits together: Both `app.py` and `stockprediction.py` implement the same pipeline: download historical OHLCV data from Yahoo Finance (via yfinance), compute simple moving averages (MA5, MA20), set the next day's close as the target (shift -1), drop missing rows, split the dataset (first 80% for training, last 20% for testing), train a scikit-learn LinearRegression model, evaluate with R²/MSE/MAE, plot actual vs predicted, and save the predictions and model.

## How to run
The shortest path from a fresh clone to running the Streamlit app:

```bash
# clone
git clone https://github.com/ayaronrios/Stock-Price-Prediction-using-Machine-Learning-and-Python.git
cd Stock-Price-Prediction-using-Machine-Learning-and-Python

# create venv (optional but recommended)
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

# install dependencies
pip install streamlit yfinance pandas matplotlib scikit-learn joblib

# run streamlit app
streamlit run app.py
```

To run the command-line script:

```bash
python stockprediction.py
# then input a ticker when prompted (e.g. AAPL)
```

Outputs:
- `stock_prediction_model.pkl` — saved model
- `predictions.csv` — CSV of test set actual vs predicted prices

## Notes, caveats & recommended improvements
- Model: current implementation uses a vanilla LinearRegression with raw features. Consider adding feature scaling (StandardScaler), time-aware validation (walk-forward / expanding window), or more expressive models (RandomForest, XGBoost, LSTM) for better predictions.
- Data leak / target shift: the target is `Close.shift(-1)` (next day), which is fine for one-step-ahead prediction, but ensure that rolling features do not incorporate the future.
- Training in Streamlit: `app.py` retrains and writes `stock_prediction_model.pkl` each run. Use caching (st.cache_resource or st.cache_data) to avoid unnecessary retraining and file writes, or provide a "Train" button that clearly re-trains.
- Robustness: add try/except around `yf.download` to handle network errors, and validate the presence of required columns before operations.
- Reproducibility: add a properly populated `requirements.txt` (or use `pip freeze > requirements.txt`) and consider adding a `runtime.txt` or Dockerfile for reproducible environments.
- Repo hygiene: remove binary files (`.pkl`) and generated CSVs from the repository and add them to `.gitignore`. Storing generated binaries in git is not recommended.
- Tests & modularity: refactor training/prediction code into functions (e.g., `load_data()`, `prepare_features()`, `train_model()`, `evaluate()`) and add unit tests to validate behavior.
- User input validation: `stockprediction.py` uses an unvalidated `input()` for the symbol; consider adding a CLI argument parser (argparse) and validation.

## Suggestions for quick improvements (small PRs)
- Populate `requirements.txt` with the minimal dependencies:
  - streamlit
  - yfinance
  - pandas
  - matplotlib
  - scikit-learn
  - joblib

- Update `app.py` to use st.cache_resource for the model and avoid saving to repo root on every run.
- Add `.gitignore` to exclude `*.pkl`, `predictions.csv`, `venv/`, `__pycache__/`.

## License
Add a license if you want to make the usage terms explicit (e.g., MIT).

---

If you want, I can:
- open a PR that adds the README (this commit), a populated requirements.txt, and a .gitignore, or
- refactor the code to extract reusable functions and add unit tests.
