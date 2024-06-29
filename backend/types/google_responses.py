from enum import Enum
from typing import List, Any, Optional
from datetime import datetime

class AddressComponent:
    long_name: str
    short_name: str
    types: List[str]

    def __init__(self, long_name: str, short_name: str, types: List[str]) -> None:
        self.long_name = long_name
        self.short_name = short_name
        self.types = types


class Location:
    lat: float
    lng: float

    def __init__(self, lat: float, lng: float) -> None:
        self.lat = lat
        self.lng = lng


class Viewport:
    northeast: Location
    southwest: Location

    def __init__(self, northeast: Location, southwest: Location) -> None:
        self.northeast = northeast
        self.southwest = southwest


class Geometry:
    location: Location
    location_type: str
    viewport: Viewport

    def __init__(self, location: Location, location_type: str, viewport: Viewport) -> None:
        self.location = location
        self.location_type = location_type
        self.viewport = viewport


class PlusCode:
    compound_code: str
    global_code: str

    def __init__(self, compound_code: str, global_code: str) -> None:
        self.compound_code = compound_code
        self.global_code = global_code


class Result:
    address_components: List[AddressComponent]
    formatted_address: str
    geometry: Geometry
    place_id: str
    plus_code: PlusCode
    types: List[str]

    def __init__(self, address_components: List[AddressComponent], formatted_address: str, geometry: Geometry, place_id: str, plus_code: PlusCode, types: List[str]) -> None:
        self.address_components = address_components
        self.formatted_address = formatted_address
        self.geometry = geometry
        self.place_id = place_id
        self.plus_code = plus_code
        self.types = types


class SampleGoogleGeocodingResponse:
    results: List[Result]
    status: str

    def __init__(self, results: List[Result], status: str) -> None:
        self.results = results
        self.status = status