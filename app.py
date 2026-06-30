
import warnings
warnings.filterwarnings("ignore")

import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

st.set_page_config(page_title="Stock Price Prediction", page_icon="📈", layout="wide")

st.markdown("""
<style>
.block-container{padding-top:2rem;padding-bottom:2rem;max-width:1100px;}
h1{text-align:center;color:#2c5aa0;}
.card{background:#f7f9fc;padding:18px;border-radius:12px;border:1px solid #dde5f0;}
</style>
""", unsafe_allow_html=True)

st.title("📈 Stock Price Prediction Using Machine Learning")
st.caption("Linear Regression model using Yahoo Finance historical data")

stock = st.text_input("Enter Stock Symbol", "AAPL").upper()

if st.button("Predict Stock Price", use_container_width=True):

    with st.spinner("Downloading stock data..."):
        df = yf.download(stock, start="2020-01-01", end="2025-01-01", auto_adjust=True)

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    if df.empty:
        st.error("No stock data found.")
        st.stop()

    st.subheader("First Five Records")
    st.dataframe(df.head(), use_container_width=True)

    c1,c2,c3=st.columns(3)
    c1.metric("Stock",stock)
    c2.metric("Records",len(df))
    c3.metric("Period",f"{df.index.min().date()} → {df.index.max().date()}")

    df["MA5"]=df["Close"].rolling(5).mean()
    df["MA20"]=df["Close"].rolling(20).mean()
    df["Target"]=df["Close"].shift(-1)
    df.dropna(inplace=True)

    features=["Open","High","Low","Close","Volume","MA5","MA20"]
    X=df[features]
    y=df["Target"]

    split=int(len(X)*0.8)
    X_train,X_test=X.iloc[:split],X.iloc[split:]
    y_train,y_test=y.iloc[:split],y.iloc[split:]

    model=LinearRegression()
    model.fit(X_train,y_train)
    joblib.dump(model,"stock_prediction_model.pkl")

    predictions=model.predict(X_test)

    r2=r2_score(y_test,predictions)
    mse=mean_squared_error(y_test,predictions)
    mae=mean_absolute_error(y_test,predictions)

    st.subheader("Model Performance")
    m1,m2,m3=st.columns(3)
    m1.metric("R² Score",f"{r2:.4f}")
    m2.metric("MSE",f"{mse:.2f}")
    m3.metric("MAE",f"{mae:.2f}")

    latest=X.iloc[[-1]]
    next_price=model.predict(latest)[0]

    a,b=st.columns(2)
    a.metric("Latest Closing Price",f"${df['Close'].iloc[-1]:.2f}")
    b.metric("Predicted Next Day Price",f"${next_price:.2f}")

    imp=pd.DataFrame({"Feature":features,"Coefficient":model.coef_}).round(6)
    with st.expander("Feature Importance"):
        st.dataframe(imp,use_container_width=True)

    fig,ax=plt.subplots(figsize=(12,5))
    ax.plot(y_test.index[-50:],y_test.values[-50:],label="Actual")
    ax.plot(y_test.index[-50:],predictions[-50:],"--",label="Predicted")
    ax.set_title(f"{stock} Stock Price Prediction")
    ax.set_xlabel("Date")
    ax.set_ylabel("Closing Price")
    ax.legend()
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)

    results=pd.DataFrame({
        "Date":y_test.index,
        "Actual Price":y_test.values,
        "Predicted Price":predictions
    })
    results["Difference"]=results["Actual Price"]-results["Predicted Price"]
    results=results.round(2)
    results.to_csv("predictions.csv",index=False)

    st.subheader("First 10 Test Predictions")
    st.dataframe(results.head(10),use_container_width=True)

    csv=results.to_csv(index=False).encode()
    st.download_button("📥 Download Predictions CSV",csv,"predictions.csv","text/csv")

    st.success("Project completed successfully!")

