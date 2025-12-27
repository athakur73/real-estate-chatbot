from fastapi import APIRouter
from pydantic import BaseModel

from app.repositories.saved_properties_repo import save_property

router = APIRouter()


class SaveRequest(BaseModel):
    session_id: str
    property_id: int


@router.post("/save")
def save_property_api(request: SaveRequest):
    save_property(
        session_id=request.session_id,
        property_id=request.property_id
    )
    return {"status": "saved"}
