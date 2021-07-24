class PersonAPI:
    def get_person(self) -> dict:
        return {
            "age": 35,
            "name": "Bob",
            "favorite_color": "Blue",
            "address": {
                "street": "123 Foobar Lane",
                "state": "PA",
                "country": "CA",
                "zip": 12345,
                "lat": 40.0228994,
                "long": -78.5173465,
            },
        }
