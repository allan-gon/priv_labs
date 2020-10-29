import logging
import random

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()


class Item(BaseModel):
    """Use this data model to parse the request body JSON."""

    longitude: float = Field(..., example=3.14)
    latitude: float = Field(..., example=-42.16)

    # def to_df(self):
    #     """Convert pydantic object to pandas dataframe with 1 row."""
    #     return pd.DataFrame([dict(self)])

    # @validator('x1')
    # def x1_must_be_positive(cls, value):
    #     """Validate that x1 is a positive number."""
    #     assert value > 0, f'x1 == {value}, must be > 0'
    #     return value


@router.post('/dummy_predict')
async def predict(item: Item):
    """
    Make random baseline predictions for classification problem 🔮

    ### Request Body
    - `longitude`: float
    - `latitude`: float
    ### Response
    - `prediction`: boolean, at random
    - `predict_proba`: float between 0.0 and 1.0,
    representing the predicted class's probability

    """

    # X_new = item.to_df()
    # log.info(X_new)
    y_pred = random.choice(["Feasible", "Not feasible"])
    y_pred_proba = random.random()
    return {
        'prediction': y_pred,
        'probability': y_pred_proba
    }
