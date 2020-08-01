from pydantic import BaseModel
from typing import List,Dict,Tuple

class Prediction(BaseModel):
  filename: str
  contenttype: str
  prediction: List[Tuple[float, float, float]] = []