

# 🧠👃 AI Powered Virtual Nose

An **AI-powered system** that simulates the human nose by detecting and classifying different gases or odors using machine learning models and (optionally) physical gas sensors like MQ-series. This project can run both with real sensor data or simulated data for testing.

---

## 📌 Features


* Simulates human-like smell detection.
* Works with real MQ-series sensors or simulated data.
* Machine learning model for odor classification.
* Modular structure: train model, simulate data, run real-time detection.
* Extensible for custom gases/odors.

---


## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Shariq-14/AI_Power_Virtual_Nose.git
cd AI_Power_Virtual_Nose
```

### 2. Create Virtual Environment (optional but recommended)


```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

If `requirements.txt` is available:

```bash
pip install -r requirements.txt
```

If not, install common dependencies manually:

```bash
pip install numpy pandas scikit-learn
```

(Additional libraries may be required depending on hardware support, e.g., `smbus` for I2C communication with sensors.)

---

## 🚀 Usage

### 1. Simulate Data

To generate test input data without hardware:

```bash
python simulate_data.py
```

### 2. Train the Model

Trains a machine learning model and saves it as `model.pkl`:

```bash
python train_model.py
```

### 3. Run the Application

Start real-time classification:

```bash
python app.py
```

or (if named differently):

```bash
python virtual_nose_app.py
```

---

## 📂 Project Structure

```
AI_Power_Virtual_Nose/
│── app.py                # Main application (odor detection)
│── train_model.py        # Train and save ML model
│── simulate_data.py      # Generate simulated sensor data
│── model.pkl             # Pre-trained model (generated after training)
│── README.md             # Project documentation
```

---

## 🔧 Hardware Support

* **Optional**: MQ-series gas sensors (MQ-2, MQ-135, etc.)
* **Alternative**: Use `simulate_data.py` for testing without hardware.

---

## 🤝 Contributing

Pull requests are welcome! If you’d like to add new features (e.g., more gases, deep learning models, or GUI), feel free to fork and contribute.

---

## 📜 License

This project is licensed under the **MIT License** – free to use and modify.

---
