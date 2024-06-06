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
    def get_description() -> str:
        return "Not Written"
    
    @staticmethod
    def get_lisence() -> str:
        return "MIT"

    @staticmethod
    def get_requirements() -> list[str]:
        return ["geopy", "pycountry", "pycountry_convert", "pytz", "timezonefinder"]
