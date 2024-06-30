from typing import Optional, List
from enum import Enum
from datetime import datetime


class AccessibilityOptions:
    wheelchair_accessible_parking: bool
    wheelchair_accessible_entrance: bool
    wheelchair_accessible_restroom: Optional[bool]
    wheelchair_accessible_seating: Optional[bool]

    def __init__(self, wheelchair_accessible_parking: bool, wheelchair_accessible_entrance: bool, wheelchair_accessible_restroom: Optional[bool], wheelchair_accessible_seating: Optional[bool]) -> None:
        self.wheelchair_accessible_parking = wheelchair_accessible_parking
        self.wheelchair_accessible_entrance = wheelchair_accessible_entrance
        self.wheelchair_accessible_restroom = wheelchair_accessible_restroom
        self.wheelchair_accessible_seating = wheelchair_accessible_seating


class LanguageCode(Enum):
    EN = "en"
    EN_US = "en-US"


class AddressComponent:
    long_text: str
    short_text: str
    types: List[str]
    language_code: LanguageCode

    def __init__(self, long_text: str, short_text: str, types: List[str], language_code: LanguageCode) -> None:
        self.long_text = long_text
        self.short_text = short_text
        self.types = types
        self.language_code = language_code


class Date:
    year: int
    month: int
    day: int

    def __init__(self, year: int, month: int, day: int) -> None:
        self.year = year
        self.month = month
        self.day = day


class Open:
    day: int
    hour: int
    minute: int
    date: Optional[Date]
    truncated: Optional[bool]

    def __init__(self, day: int, hour: int, minute: int, date: Optional[Date], truncated: Optional[bool]) -> None:
        self.day = day
        self.hour = hour
        self.minute = minute
        self.date = date
        self.truncated = truncated


class Period:
    open: Open
    close: Optional[Open]

    def __init__(self, open: Open, close: Optional[Open]) -> None:
        self.open = open
        self.close = close


class OpeningHours:
    open_now: bool
    periods: List[Period]
    weekday_descriptions: List[str]

    def __init__(self, open_now: bool, periods: List[Period], weekday_descriptions: List[str]) -> None:
        self.open_now = open_now
        self.periods = periods
        self.weekday_descriptions = weekday_descriptions


class SecondaryOpeningHour:
    open_now: bool
    periods: List[Period]
    weekday_descriptions: List[str]
    secondary_hours_type: str

    def __init__(self, open_now: bool, periods: List[Period], weekday_descriptions: List[str], secondary_hours_type: str) -> None:
        self.open_now = open_now
        self.periods = periods
        self.weekday_descriptions = weekday_descriptions
        self.secondary_hours_type = secondary_hours_type


class DisplayName:
    text: str
    language_code: LanguageCode

    def __init__(self, text: str, language_code: LanguageCode) -> None:
        self.text = text
        self.language_code = language_code


class AuthorAttribution:
    display_name: str
    uri: str
    photo_uri: str

    def __init__(self, display_name: str, uri: str, photo_uri: str) -> None:
        self.display_name = display_name
        self.uri = uri
        self.photo_uri = photo_uri


class Review:
    name: str
    relative_publish_time_description: str
    rating: int
    text: DisplayName
    original_text: DisplayName
    author_attribution: AuthorAttribution
    publish_time: datetime

    def __init__(self, name: str, relative_publish_time_description: str, rating: int, text: DisplayName, original_text: DisplayName, author_attribution: AuthorAttribution, publish_time: datetime) -> None:
        self.name = name
        self.relative_publish_time_description = relative_publish_time_description
        self.rating = rating
        self.text = text
        self.original_text = original_text
        self.author_attribution = author_attribution
        self.publish_time = publish_time


class References:
    reviews: List[Review]

    def __init__(self, reviews: List[Review]) -> None:
        self.reviews = reviews


class GenerativeSummary:
    overview: DisplayName
    description: Optional[DisplayName]
    references: Optional[References]

    def __init__(self, overview: DisplayName, description: Optional[DisplayName], references: Optional[References]) -> None:
        self.overview = overview
        self.description = description
        self.references = references


class Location:
    latitude: float
    longitude: float

    def __init__(self, latitude: float, longitude: float) -> None:
        self.latitude = latitude
        self.longitude = longitude


class ParkingOptions:
    paid_parking_lot: Optional[bool]
    paid_street_parking: Optional[bool]
    valet_parking: bool
    paid_garage_parking: Optional[bool]

    def __init__(self, paid_parking_lot: Optional[bool], paid_street_parking: Optional[bool], valet_parking: bool, paid_garage_parking: Optional[bool]) -> None:
        self.paid_parking_lot = paid_parking_lot
        self.paid_street_parking = paid_street_parking
        self.valet_parking = valet_parking
        self.paid_garage_parking = paid_garage_parking


class PaymentOptions:
    accepts_credit_cards: Optional[bool]
    accepts_debit_cards: bool
    accepts_cash_only: Optional[bool]
    accepts_nfc: Optional[bool]

    def __init__(self, accepts_credit_cards: Optional[bool], accepts_debit_cards: bool, accepts_cash_only: Optional[bool], accepts_nfc: Optional[bool]) -> None:
        self.accepts_credit_cards = accepts_credit_cards
        self.accepts_debit_cards = accepts_debit_cards
        self.accepts_cash_only = accepts_cash_only
        self.accepts_nfc = accepts_nfc


class Photo:
    name: str
    width_px: int
    height_px: int
    author_attributions: List[AuthorAttribution]

    def __init__(self, name: str, width_px: int, height_px: int, author_attributions: List[AuthorAttribution]) -> None:
        self.name = name
        self.width_px = width_px
        self.height_px = height_px
        self.author_attributions = author_attributions


class PlusCode:
    global_code: str
    compound_code: str

    def __init__(self, global_code: str, compound_code: str) -> None:
        self.global_code = global_code
        self.compound_code = compound_code


class Viewport:
    low: Location
    high: Location

    def __init__(self, low: Location, high: Location) -> None:
        self.low = low
        self.high = high


class Place:
    name: str
    id: str
    types: List[str]
    national_phone_number: str
    international_phone_number: str
    formatted_address: str
    address_components: List[AddressComponent]
    plus_code: PlusCode
    location: Location
    viewport: Viewport
    rating: float
    google_maps_uri: str
    website_uri: str
    regular_opening_hours: Optional[OpeningHours]
    utc_offset_minutes: int
    adr_format_address: str
    business_status: str
    price_level: Optional[str]
    user_rating_count: int
    icon_mask_base_uri: str
    icon_background_color: str
    display_name: DisplayName
    primary_type_display_name: DisplayName
    takeout: Optional[bool]
    delivery: Optional[bool]
    dine_in: Optional[bool]
    reservable: Optional[bool]
    serves_lunch: Optional[bool]
    serves_dinner: Optional[bool]
    serves_beer: Optional[bool]
    serves_wine: Optional[bool]
    serves_vegetarian_food: Optional[bool]
    current_opening_hours: Optional[OpeningHours]
    primary_type: str
    short_formatted_address: str
    editorial_summary: DisplayName
    reviews: List[Review]
    photos: List[Photo]
    outdoor_seating: Optional[bool]
    menu_for_children: Optional[bool]
    serves_cocktails: Optional[bool]
    serves_dessert: Optional[bool]
    good_for_children: bool
    allows_dogs: Optional[bool]
    restroom: Optional[bool]
    good_for_groups: Optional[bool]
    good_for_watching_sports: Optional[bool]
    payment_options: PaymentOptions
    parking_options: Optional[ParkingOptions]
    accessibility_options: AccessibilityOptions
    generative_summary: Optional[GenerativeSummary]
    serves_breakfast: Optional[bool]
    serves_brunch: Optional[bool]
    current_secondary_opening_hours: Optional[List[SecondaryOpeningHour]]
    regular_secondary_opening_hours: Optional[List[SecondaryOpeningHour]]
    live_music: Optional[bool]
    serves_coffee: Optional[bool]
    curbside_pickup: Optional[bool]

    def __init__(self, name: str, id: str, types: List[str], national_phone_number: str, international_phone_number: str, formatted_address: str, address_components: List[AddressComponent], plus_code: PlusCode, location: Location, viewport: Viewport, rating: float, google_maps_uri: str, website_uri: str, regular_opening_hours: Optional[OpeningHours], utc_offset_minutes: int, adr_format_address: str, business_status: str, price_level: Optional[str], user_rating_count: int, icon_mask_base_uri: str, icon_background_color: str, display_name: DisplayName, primary_type_display_name: DisplayName, takeout: Optional[bool], delivery: Optional[bool], dine_in: Optional[bool], reservable: Optional[bool], serves_lunch: Optional[bool], serves_dinner: Optional[bool], serves_beer: Optional[bool], serves_wine: Optional[bool], serves_vegetarian_food: Optional[bool], current_opening_hours: Optional[OpeningHours], primary_type: str, short_formatted_address: str, editorial_summary: DisplayName, reviews: List[Review], photos: List[Photo], outdoor_seating: Optional[bool], menu_for_children: Optional[bool], serves_cocktails: Optional[bool], serves_dessert: Optional[bool], good_for_children: bool, allows_dogs: Optional[bool], restroom: Optional[bool], good_for_groups: Optional[bool], good_for_watching_sports: Optional[bool], payment_options: PaymentOptions, parking_options: Optional[ParkingOptions], accessibility_options: AccessibilityOptions, generative_summary: Optional[GenerativeSummary], serves_breakfast: Optional[bool], serves_brunch: Optional[bool], current_secondary_opening_hours: Optional[List[SecondaryOpeningHour]], regular_secondary_opening_hours: Optional[List[SecondaryOpeningHour]], live_music: Optional[bool], serves_coffee: Optional[bool], curbside_pickup: Optional[bool]) -> None:
        self.name = name
        self.id = id
        self.types = types
        self.national_phone_number = national_phone_number
        self.international_phone_number = international_phone_number
        self.formatted_address = formatted_address
        self.address_components = address_components
        self.plus_code = plus_code
        self.location = location
        self.viewport = viewport
        self.rating = rating
        self.google_maps_uri = google_maps_uri
        self.website_uri = website_uri
        self.regular_opening_hours = regular_opening_hours
        self.utc_offset_minutes = utc_offset_minutes
        self.adr_format_address = adr_format_address
        self.business_status = business_status
        self.price_level = price_level
        self.user_rating_count = user_rating_count
        self.icon_mask_base_uri = icon_mask_base_uri
        self.icon_background_color = icon_background_color
        self.display_name = display_name
        self.primary_type_display_name = primary_type_display_name
        self.takeout = takeout
        self.delivery = delivery
        self.dine_in = dine_in
        self.reservable = reservable
        self.serves_lunch = serves_lunch
        self.serves_dinner = serves_dinner
        self.serves_beer = serves_beer
        self.serves_wine = serves_wine
        self.serves_vegetarian_food = serves_vegetarian_food
        self.current_opening_hours = current_opening_hours
        self.primary_type = primary_type
        self.short_formatted_address = short_formatted_address
        self.editorial_summary = editorial_summary
        self.reviews = reviews
        self.photos = photos
        self.outdoor_seating = outdoor_seating
        self.menu_for_children = menu_for_children
        self.serves_cocktails = serves_cocktails
        self.serves_dessert = serves_dessert
        self.good_for_children = good_for_children
        self.allows_dogs = allows_dogs
        self.restroom = restroom
        self.good_for_groups = good_for_groups
        self.good_for_watching_sports = good_for_watching_sports
        self.payment_options = payment_options
        self.parking_options = parking_options
        self.accessibility_options = accessibility_options
        self.generative_summary = generative_summary
        self.serves_breakfast = serves_breakfast
        self.serves_brunch = serves_brunch
        self.current_secondary_opening_hours = current_secondary_opening_hours
        self.regular_secondary_opening_hours = regular_secondary_opening_hours
        self.live_music = live_music
        self.serves_coffee = serves_coffee
        self.curbside_pickup = curbside_pickup


class GoogleNearbySearch:
    places: List[Place]

    def __init__(self, places: List[Place]) -> None:
        self.places = places
