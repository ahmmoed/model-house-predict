# from fastapi import FastAPI
# from pydantic import BaseModel
# import joblib
# import pandas as pd

# model = joblib.load("model_predict_house_value_1.joblib")

# app = FastAPI()

# class HouseData(BaseModel):
#     longitude: float
#     latitude: float
#     housing_median_age: float
#     total_rooms: float
#     total_bedrooms: float
#     households: float
#     median_income: float

# @app.post("/predict")
# def predict(data: HouseData):

#     input_data = pd.DataFrame([data.model_dump()])

#     prediction = model.predict(input_data)

#     return {
#         "predicted_price": float(prediction[0])
#     }

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

model = joblib.load("model_predict_house_value_1.joblib")

app = FastAPI()

class HouseData(BaseModel):
    خط_الطول: float
    خط_العرض: float
    عمر_المنازل: float
    إجمالي_الغرف: float
    غرف_النوم: float
    عدد_الأسر: float
    متوسط_الدخل: float


@app.post("/predict")
def predict(data: HouseData):

    input_data = pd.DataFrame([{
        "longitude": data.خط_الطول,
        "latitude": data.خط_العرض,
        "housing_median_age": data.عمر_المنازل,
        "total_rooms": data.إجمالي_الغرف,
        "total_bedrooms": data.غرف_النوم,
        "households": data.عدد_الأسر,
        "median_income": data.متوسط_الدخل
    }])

    prediction = model.predict(input_data)

    return {
        "السعر_المتوقع": float(prediction[0])
    }