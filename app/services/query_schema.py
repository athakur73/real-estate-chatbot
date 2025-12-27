from typing import List, Optional
from pydantic import BaseModel, Field

class PropertyQuery(BaseModel):
    location: Optional[str] = Field(
        None, description="City or city, state (e.g., Dallas or Dallas, TX)"
    )
    bedrooms: Optional[int] = Field(
        None, description="Number of bedrooms"
    )
    min_price: Optional[int] = Field(
        None, description="Minimum property price"
    )
    max_price: Optional[int] = Field(
        None, description="Maximum property price"
    )
    amenities: Optional[List[str]] = Field(
        None, description="Desired amenities like backyard, pool, parking"
    )
