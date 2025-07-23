import requests
from typing import Optional

class TimezoneHelper:
    def __init__(self, api_key: str = 'CPA8DG44IP5Z'):
        self.api_key = api_key
    
    def get_timezone(self, latitude: float, longitude: float) -> str:
        """Get timezone for given coordinates using TimeZoneDB API."""
        params = {
            'key': self.api_key,
            'format': 'json',
            'by': 'position',
            'lat': latitude,
            'lng': longitude
        }
        
        try:
            response = requests.get("http://api.timezonedb.com/v2.1/get-time-zone", params=params)
            response.raise_for_status()
            data = response.json()
            
            if data.get('status') == 'OK':
                return data['zoneName']
            else:
                raise ValueError(f"TimeZoneDB API error: {data.get('message', 'Unknown error')}")
                
        except requests.RequestException as e:
            raise ValueError(f"Failed to fetch timezone: {str(e)}")
    
    def get_timezone_with_fallback(self, latitude: float, longitude: float, fallback: str = "UTC") -> str:
        """Get timezone with fallback option."""
        try:
            return self.get_timezone(latitude, longitude)
        except Exception as e:
            print(f"Warning: Could not determine timezone for coordinates ({latitude}, {longitude}): {e}")
            return fallback

# Global instance
timezone_helper = TimezoneHelper()