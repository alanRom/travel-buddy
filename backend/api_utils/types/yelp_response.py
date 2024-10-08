# Generated by https://quicktype.io
#
# To change quicktype's target language, run command:
#
#   "Set quicktype target language"

from enum import Enum
from typing import List, Any, Optional
from datetime import datetime


class Category:
    alias: str
    title: str

    def __init__(self, alias: str, title: str) -> None:
        self.alias = alias
        self.title = title


class Center:
    latitude: float
    longitude: float

    def __init__(self, latitude: float, longitude: float) -> None:
        self.latitude = latitude
        self.longitude = longitude


class Country(Enum):
    US = "US"


class State(Enum):
    NJ = "NJ"


class Location:
    address1: str
    address2: Optional[str]
    address3: Optional[str]
    city: str
    country: Country
    display_address: List[str]
    state: State
    zip_code: str

    def __init__(self, address1: str, address2: Optional[str], address3: Optional[str], city: str, country: Country, display_address: List[str], state: State, zip_code: str) -> None:
        self.address1 = address1
        self.address2 = address2
        self.address3 = address3
        self.city = city
        self.country = country
        self.display_address = display_address
        self.state = state
        self.zip_code = zip_code


class Price(Enum):
    EMPTY = "$$"
    PRICE = "$"


class Transaction(Enum):
    DELIVERY = "delivery"
    PICKUP = "pickup"
    RESTAURANT_RESERVATION = "restaurant_reservation"


class Business:
    alias: str
    categories: List[Category]
    coordinates: Center
    display_phone: str
    distance: float
    id: str
    image_url: str
    is_closed: bool
    location: Location
    name: str
    phone: str
    price: Optional[Price]
    rating: float
    review_count: int
    transactions: List[Transaction]
    url: str

    def __init__(self, alias: str, categories: List[Category], coordinates: Center, display_phone: str, distance: float, id: str, image_url: str, is_closed: bool, location: Location, name: str, phone: str, price: Optional[Price], rating: float, review_count: int, transactions: List[Transaction], url: str) -> None:
        self.alias = alias
        self.categories = categories
        self.coordinates = coordinates
        self.display_phone = display_phone
        self.distance = distance
        self.id = id
        self.image_url = image_url
        self.is_closed = is_closed
        self.location = location
        self.name = name
        self.phone = phone
        self.price = price
        self.rating = rating
        self.review_count = review_count
        self.transactions = transactions
        self.url = url


class Region:
    center: Center

    def __init__(self, center: Center) -> None:
        self.center = center


class SampleYelpResponse:
    businesses: List[Business]
    region: Region
    total: int

    def __init__(self, businesses: List[Business], region: Region, total: int) -> None:
        self.businesses = businesses
        self.region = region
        self.total = total

class Coordinates:
    latitude: float
    longitude: float

    def __init__(self, latitude: float, longitude: float) -> None:
        self.latitude = latitude
        self.longitude = longitude


class Open:
    is_overnight: bool
    start: int
    end: int
    day: int

    def __init__(self, is_overnight: bool, start: int, end: int, day: int) -> None:
        self.is_overnight = is_overnight
        self.start = start
        self.end = end
        self.day = day


class SpecialHour:
    date: datetime
    is_closed: None
    start: int
    end: int
    is_overnight: bool

    def __init__(self, date: datetime, is_closed: None, start: int, end: int, is_overnight: bool) -> None:
        self.date = date
        self.is_closed = is_closed
        self.start = start
        self.end = end
        self.is_overnight = is_overnight

class Hour:
    open: List[Open]
    hours_type: str
    is_open_now: bool

    def __init__(self, open: List[Open], hours_type: str, is_open_now: bool) -> None:
        self.open = open
        self.hours_type = hours_type
        self.is_open_now = is_open_now

class Coordinates:
    latitude: float
    longitude: float

    def __init__(self, latitude: float, longitude: float) -> None:
        self.latitude = latitude
        self.longitude = longitude


class SampleYelpBusiness:
    id: str
    alias: str
    name: str
    image_url: str
    is_claimed: bool
    is_closed: bool
    url: str
    phone: str
    display_phone: str
    review_count: int
    categories: List[Category]
    rating: float
    location: Location
    coordinates: Coordinates
    photos: List[str]
    price: str
    hours: List[Hour]
    transactions: List[Any]
    special_hours: List[SpecialHour]

    def __init__(self, id: str, alias: str, name: str, image_url: str, is_claimed: bool, is_closed: bool, url: str, phone: str, display_phone: str, review_count: int, categories: List[Category], rating: float, location: Location, coordinates: Coordinates, photos: List[str], price: str, hours: List[Hour], transactions: List[Any], special_hours: List[SpecialHour]) -> None:
        self.id = id
        self.alias = alias
        self.name = name
        self.image_url = image_url
        self.is_claimed = is_claimed
        self.is_closed = is_closed
        self.url = url
        self.phone = phone
        self.display_phone = display_phone
        self.review_count = review_count
        self.categories = categories
        self.rating = rating
        self.location = location
        self.coordinates = coordinates
        self.photos = photos
        self.price = price
        self.hours = hours
        self.transactions = transactions
        self.special_hours = special_hours

