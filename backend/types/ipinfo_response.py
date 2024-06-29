class SampleIpinfoResponse:
    ip: str
    hostname: str
    city: str
    region: str
    country: str
    loc: str
    org: str
    postal: str
    timezone: str

    def __init__(self, ip: str, hostname: str, city: str, region: str, country: str, loc: str, org: str, postal: str, timezone: str) -> None:
        self.ip = ip
        self.hostname = hostname
        self.city = city
        self.region = region
        self.country = country
        self.loc = loc
        self.org = org
        self.postal = postal
        self.timezone = timezone