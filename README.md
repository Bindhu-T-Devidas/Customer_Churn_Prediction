## Customer Churn Prediction

This project is a web-based application designed to predict customer churn using a **machine learning model**. The application is built using **Streamlit** and leverages a pre-trained model to classify whether a customer is likely to churn or not.

### Project Structure
```
Customer_Churn_Prediction/
├── app.py                  # Streamlit app for customer churn prediction
├── churn_prediction_pipeline.pkl  # Trained machine learning model
├── README.md               # Project documentation
```

## Project Description
This project aims to predict customer churn based on various input features, such as tenure, internet service type, online security, tech support availability, contract type, and payment method. The model calculates the churn probability and compares it with a user-defined threshold to determine the final prediction.

### Technologies Used
- **Python**
- **Streamlit**: For building the interactive web app.
- **Pandas**: For data manipulation.
- **NumPy**: For numerical computations.
- **Joblib**: For loading the machine learning model.

---

## How to Run the Project

### Step 1: Clone the Repository
```
git clone https://github.com/Bindhu-T-Devidas/Customer_Churn_Prediction.git
cd Customer_Churn_Prediction
```

### Step 2: Install Required Libraries
```
pip install streamlit pandas numpy joblib
```

### Step 3: Run the Streamlit App
```
streamlit run app.py
```

---

## App Features

### 1. Threshold Explanation
- The app explains how the churn probability threshold works.
- Adjusting the threshold makes the model more or less sensitive to predicting churn.

### 2. Interactive User Inputs
- **Tenure (months)**: Slider to select customer tenure.
- **Internet Service**: Dropdown to choose the type of internet service.
- **Online Security**: Dropdown to select whether online security is enabled.
- **Tech Support**: Dropdown to choose whether tech support is available.
- **Contract Type**: Dropdown for selecting the contract duration.
- **Payment Method**: Dropdown to choose the payment method.
- **Churn Probability Threshold**: Slider to set the sensitivity.

### 3. Prediction Output
- Displays whether the customer will churn or not.
- Shows the churn probability.
- Uses color-coded feedback (Success for "No", Error for "Yes").

---

## Model Details
- The model is loaded using `joblib` from the file `churn_prediction_pipeline.pkl`.
- Uses **logistic regression** for classification.
- The prediction threshold can be adjusted to increase or decrease sensitivity.

### Prediction Logic
- If the predicted churn probability is **greater than the set threshold**, the app displays **"Yes"** (customer will churn).
- If it is **less than or equal to the threshold**, the app displays **"No"** (customer will stay).

---

## Example Usage
1. Set the **tenure** to 24 months.
2. Choose **Fiber optic** as the internet service.
3. Select **Yes** for online security and tech support.
4. Choose **One year** as the contract type.
5. Set **Credit card (automatic)** as the payment method.
6. Adjust the **churn probability threshold** to 0.5.
7. Click **"Predict Churn"** to get the result.

---


## License
This project is licensed under the **MIT License**.

## Contact
For any queries or issues, please contact:  
**Bindhu T Devidas**  
Email: bindutaragolli@gmail.com

