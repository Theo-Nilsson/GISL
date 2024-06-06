class Libinfo:
    @staticmethod
    def get_name() -> str:
        return "GISL"
    
    @staticmethod
    def get_version() -> str:
        return "1.0.0"
    
    @staticmethod
    def get_author(legal_name: bool = True) -> str:
        return "Theo Nilsson" if legal_name else "Blinken77"
    
    @staticmethod
    def get_author_email() -> str:
        return "theonilsson2012@icloud.com"
    
    @staticmethod
    def get_author_github() -> str:
        return "https://www.github.com/Theo-Nilsson"
    
    @staticmethod
    def get_url() -> str:
        return "https://www.github.com/Theo-Nilsson/GISL"
    
    @staticmethod
    def get_description() -> str:
        return f"{Libinfo.get_name()} is a versatile Python library designed for Geographic Information System (GIS) tasks. It offers methods to retrieve country names and codes, determine continents, geocode IP addresses, calculate distances between coordinates, find time zones, and get addresses from latitude and longitude. {Libinfo.get_name()} also allows users to obtain the public IP address of the current machine, making it an essential toolkit for developers and researchers working with geospatial data."
    
    @staticmethod
    def get_lisence() -> str:
        return "MIT"

    @staticmethod
    def get_requirements() -> list[str]:
        return ["geopy", "pycountry", "pycountry_convert", "timezonefinder"]
