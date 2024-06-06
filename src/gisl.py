from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import geocoder
import pycountry
import pycountry_convert
import requests
import timezonefinder

class GISL:
    """
    A class to perform various Geographic Information System (GIS) related tasks.

    Methods
    -------
    get_country(country_code: str) -> str:
        Returns the country name corresponding to the given country code.

    get_country(country_name: str) -> str:
        Returns the country code corresponding to the given country name.
        
    get_continent(country_code: str) -> str:
        Returns the continent name corresponding to the given country code.

    get_lat_lng(ip: str) -> list[float]:
        Returns the latitude and longitude of the given IP address.

    get_address(lat: float, lng: float) -> str:
        Returns the address corresponding to the given latitude and longitude.

    get_public_ip() -> str:
        Returns the public IP address of the current machine.

    get_timezone(lat: float, lng: float) -> str:
        Returns the timezone corresponding to the given latitude and longitude.
    """
    
    def get_country(self, country_code: str) -> str:
        """
        Returns the country name corresponding to the given country code.

        Parameters
        ----------
        country_code : str
            The two-letter country code (ISO 3166-1 alpha-2).

        Returns
        -------
        str
            The name of the country if found, otherwise an empty string.
        """
        try:
            country = pycountry.countries.get(alpha_2=country_code)
            try: 
                country = country.name
            except AttributeError: 
                print(f"The country code \"{country_code}\" could not be found")
                return ""
            return country
        except LookupError as e:
            print(f"A LookupError occurred: {e}")
            return ""
        
    def get_country_code(self, country_name: str) -> str:
        """
        Returns the country code corresponding to the given country name.

        Parameters
        ----------
        country_name : str
            The name of the country.

        Returns
        -------
        str
            The two-letter country code (ISO 3166-1 alpha-2) if found, otherwise an empty string.
        """
        try:
            country = pycountry.countries.lookup(country_name)
            try: 
                country = country.alpha_2
            except AttributeError: 
                print(f"The country \"{country_name}\" could not be found")
                return ""
            return country
        except LookupError as e:
            print(f"A LookupError occurred: {e}")
            return ""
        
    def get_continent(self, country_code: str) -> str:
        """
        Returns the continent name corresponding to the given country code.

        Parameters
        ----------
        country_code : str
            The two-letter country code (ISO 3166-1 alpha-2).

        Returns
        -------
        str
            The name of the continent if found, otherwise an empty string.
        """
        try:
            continent_code = pycountry_convert.country_alpha2_to_continent_code(country_code)
            continent = pycountry_convert.convert_continent_code_to_continent_name(continent_code)
            return continent
        except KeyError:
            print(f"The country code \"{country_code}\" could not be converted to a continent code.")
            return ""
        
    def get_lat_lng(self, ip: str) -> list[float]:
        """
        Returns the latitude and longitude of the given IP address.

        Parameters
        ----------
        ip : str
            The IP address to look up.

        Returns
        -------
        list[float]
            A list containing the latitude and longitude if found, otherwise an empty list.
        """
        g = geocoder.ip(ip)
        return g.latlng
    
    def get_distance_between_coords(self, lat_lng: tuple[float] | list[float], lat_lng_: tuple[float] | list[float], km: bool = True) -> float:
        """
        Returns the distance between two sets of coordinates.

        Parameters
        ----------
        lat_lng : tuple[float] | list[float]
            The first set of latitude and longitude coordinates.
        lat_lng_ : tuple[float] | list[float]
            The second set of latitude and longitude coordinates.
        km : bool, optional
            If True, returns distance in kilometers, else in miles. Default is True.

        Returns
        -------
        float
            The distance between the coordinates in kilometers if km is True, otherwise in miles.
        """

        try:
            return great_circle(lat_lng, lat_lng_).km if km else great_circle(lat_lng, lat_lng_).miles
        except ValueError as e:
            print(f"A ValueError occurred: {e}")
    
    def get_timezone(self, lat: float, lng: float) -> str:
        """
        Returns the timezone corresponding to the given latitude and longitude.

        Parameters
        ----------
        lat : float
            The latitude coordinate.
        lng : float
            The longitude coordinate.

        Returns
        -------
        str
            The timezone name if found, otherwise an empty string.
        """
        tf = timezonefinder.TimezoneFinder()
        try:
            timezone_str = tf.certain_timezone_at(lat=lat, lng=lng)
            if not timezone_str:
                print(f"Could not determine the time zone for ({lat}, {lng}).")
                return ""
            return timezone_str
        except ValueError:
            print(f"Could not determine the time zone for ({lat}, {lng}) or the coordinates were out of bounds.")
    
    def get_address(self, lat: float, lng: float) -> str:
        """
        Returns the address corresponding to the given latitude and longitude.

        Parameters
        ----------
        lat : float
            The latitude coordinate.
        lng : float
            The longitude coordinate.

        Returns
        -------
        str
            The address corresponding to the given coordinates if found, otherwise an empty string.
        """
        geolocator = Nominatim(user_agent="GISL")
        try:
            location = geolocator.reverse(f"{lat}, {lng}")
            location = location.address
            return location
        except Exception as e:
            print(f"An error occurred: {e}")     
            return ""
    
    def get_public_ip(self) -> str:
        """
        Returns the public IP address of the current machine.

        Returns
        -------
        str
            The public IP address if found, otherwise an empty string.
        """
        try:
            ip = requests.get('https://api64.ipify.org?format=json').json()['ip']
            return ip
        except Exception as e:
            print(f"Could not get public IP address: {e}")
            return ""
