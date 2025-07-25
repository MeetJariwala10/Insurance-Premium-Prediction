# 🛡️ Insurance Premium Prediction

A production-grade, containerized API and web app for predicting insurance premium categories using machine learning. Built with **FastAPI** (backend) and **Streamlit** (frontend).

---

## 🚀 Features

- **API**: FastAPI backend for insurance premium prediction.
- **ML Model**: Pre-trained scikit-learn model for classification.
- **User Interface**: Streamlit web app for easy, interactive predictions.
- **Validation**: Robust input validation using Pydantic.
- **Dockerized**: Ready for deployment with Docker.
- **Health Check**: `/health` endpoint for cloud readiness.
- **Confidence & Probabilities**: Returns prediction confidence and class probabilities.

---

## 🏗️ Project Structure

```
insurance-premium-prediction/
│
├── app.py                  # FastAPI app (API endpoints)
├── temp.py                 # Streamlit UI for predictions
├── model/
│   ├── model.pkl           # Trained ML model (scikit-learn)
│   └── predict.py          # Model loading & prediction logic
├── schema/
│   ├── user_input.py       # Input schema & feature engineering
│   └── prediction_response.py # Output schema
├── config/
│   └── city_tier.py        # City tier definitions
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker containerization
└── README.md               # Project documentation
```

---

## 🖥️ How It Works

### 1. **API Endpoints** (`app.py`)

- `GET /` — Home, returns a welcome message.
- `GET /health` — Health check for deployment.
- `POST /predict` — Accepts user details, returns predicted premium category, confidence, and class probabilities.

### 2. **Prediction Logic** (`model/predict.py`)

- Loads a pre-trained model (`model.pkl`).
- Accepts engineered features (BMI, age group, lifestyle risk, city tier, etc.).
- Returns:
  - `predicted_category`: e.g., "High", "Medium", "Low"
  - `confidence`: Model's confidence in the prediction
  - `class_probabilities`: Probability for each class

### 3. **Input & Output Schemas** (`schema/`)

- **Input**: Age, weight, height, income, smoker status, city, occupation.
- **Feature Engineering**: BMI, age group, lifestyle risk, city tier are computed automatically.
- **Output**: Structured response with category, confidence, and probabilities.

### 4. **Streamlit UI** (`temp.py`)

- User-friendly web interface for predictions.
- Collects user input, calls the API, and displays results in a readable format (category, confidence %, probability table).

---

## 🏃‍♂️ Quickstart

### 1. **Clone the Repo**

```bash
git clone <repo-url>
cd insurance-premium-prediction
```

### 2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 3. **Run the API**

```bash
uvicorn app:app --reload
```

### 4. **Run the Streamlit App**

```bash
streamlit run temp.py
```

### 5. **(Optional) Run with Docker**

```bash
docker build -t insurance-premium .
docker run -p 8000:8000 insurance-premium
```

---

## 📝 Example API Request

**POST** `/predict`
```json
{
  "age": 35,
  "weight": 70,
  "height": 1.75,
  "income_lpa": 120000,
  "smoker": false,
  "city": "Surat",
  "occupation": "private_job"
}
```

**Response:**
```json
{
  "response": {
    "predicted_category": "High",
    "confidence": 0.46,
    "class_probabilities": {
      "High": 0.46,
      "Low": 0.13,
      "Medium": 0.41
    }
  }
}
```

---

## 🧩 Dependencies

- fastapi
- uvicorn
- streamlit
- scikit-learn
- pandas
- pydantic
- pillow
- (see `requirements.txt` for full list)

---

## 🐳 Docker Usage

1. Build the image:
   ```bash
   docker build -t insurance-premium .
   ```
2. Run the container:
   ```bash
   docker run -p 8000:8000 insurance-premium
   ```

---

## 📁 Notes

- The ML model (`model/model.pkl`) must be present for predictions.
- The Streamlit app expects the FastAPI server to be running at `http://127.0.0.1:8000`.
- For deployment, update CORS settings and API URLs as needed.

---

## 📚 Credits

- Built with FastAPI, Streamlit, and scikit-learn.
- Author: [Your Name]