🏠 House Price Prediction Web App 🏠

   -A user-friendly web application built with Flask and scikit-learn to predict house prices based on area and number of bedrooms.

💡 Introduction 💡

   -This web application simplifies house price prediction.  Just enter the area (in sq. ft) and the number of bedrooms, and the app will predict the price (in Rs.) using a pre-trained Linear Regression model.  
   -The model is trained on a dataset of house prices for accurate and efficient predictions.

🛠️ Installation 🛠️

1. Clone this repository:

   -git clone https://github.com/your-repository/house-price-prediction.git
   -cd house-price-prediction

2. Install required dependencies:

   -pip install -r requirements.txt

3. Ensure that you have the dataset (House_Price.json) inside the Data/ folder.

4. Train the model (if not already trained):

   -python train_model.py

   -This will generate the model.pkl file.

💻 Usage 💻   

1. Start the Flask server:

   -python app.py

2. Open a web browser and go to:

   -http://127.0.0.1:5000/

3. Enter the required input values and click Predict Price to get the predicted house price.


📂 File Structure 📂
.
├── app.py             # Flask web app
├── model.pkl          # Trained model (from model_training.py)
├── model_training.py  # Model training script
├── requirements.txt   # Required packages
├── templates/         # HTML templates
│   └── index.html     # Main template
├── Data/              # Data files
│   └── House_Price.json  # House price data
└── README.md          # This file
└── static/            # Static files
    └── house_icon.png # Example icon/image (replace with your own)
    └── Test H.jpg     # Background image (example)


📸 Screenshots 📸

With the required buttons and inputs
![image](https://github.com/user-attachments/assets/f0ac3ac5-0ddd-42c5-a10e-18199c7a7e53)

Once the inputs are given
![image](https://github.com/user-attachments/assets/202f1a27-d0f7-4212-9bc9-2605b65f85bb)






