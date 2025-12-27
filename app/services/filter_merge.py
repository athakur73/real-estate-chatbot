from app.services.query_schema import PropertyQuery

def merge_filters(
    old: PropertyQuery | None,
    new: PropertyQuery
) -> PropertyQuery:
    if not old:
        return new

    return PropertyQuery(
        location=new.location or old.location,
        bedrooms=new.bedrooms or old.bedrooms,
        min_price=new.min_price or old.min_price,
        max_price=new.max_price or old.max_price,
        amenities=list(set((old.amenities or []) + (new.amenities or [])))
        if new.amenities or old.amenities else None
    )
