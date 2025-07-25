from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import model, MODEL_VERSION, predict_output
from schema.prediction_response import PredictionResponse

app = FastAPI()

# ENDPOINT for home page
# This is human readable (i.e. user can see this)
@app.get('/')
def home():
    return {'message': 'Insurance premium prediction API'}

# ENPOINT which is used by cloud platforms like AWS that our API is working and ready to deply
# This ENPOINT is machine readable (i.e. only the clud platforms can hit this enpoint for health check)
@app.get('/health')
def health_check():
    return {
        'status': 'OK',
        'version': MODEL_VERSION,
        'model_loaded': model is not None
    }

# ENDPOINT to predict the premium
@app.post('/predict', response_model=PredictionResponse)
def predict_premium(data: UserInput):

    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200, content={'response': prediction})
    
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)