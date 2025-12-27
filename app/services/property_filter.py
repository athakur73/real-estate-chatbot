from typing import List
from app.services.query_schema import PropertyQuery

def normalize(text: str) -> str:
    return text.lower().strip()

def filter_properties(properties: List[dict], query: PropertyQuery) -> List[dict]:
    results = []

    for prop in properties:
        # Location filter
        if query.location:
            if query.location.lower() not in prop.get("location", "").lower():
                continue

        # Bedrooms filter
        if query.bedrooms:
            if prop.get("bedrooms") != query.bedrooms:
                continue

        # Price filters
        if query.min_price:
            if prop.get("price", 0) < query.min_price:
                continue

        if query.max_price:
            if prop.get("price", 0) > query.max_price:
                continue

        # Amenities filter
        if query.amenities:
            prop_amenities = [normalize(a) for a in prop.get("amenities", [])]
            required = [normalize(a) for a in query.amenities]

            if not all(a in prop_amenities for a in required):
                continue

        results.append(prop)

    return results
