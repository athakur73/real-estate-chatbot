from datetime import datetime
from app.db.mongo import saved_properties_collection

def save_property(session_id: str, property_id: int):
    saved_properties_collection.update_one(
        {
            "session_id": session_id,
            "property_id": property_id
        },
        {
            "$setOnInsert": {
                "saved_at": datetime.utcnow()
            }
        },
        upsert=True
    )


def get_saved_properties(session_id: str):
    return list(
        saved_properties_collection.find(
            {"session_id": session_id},
            {"_id": 0}
        )
    )
