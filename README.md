# mocktail
Python data mocking package. It can be used in 
* Unit testing
* Data quality testing
* Mocking data for API response 
* Generating seed data for the database

It allows you to define data models similar to how Django or Pydantic models are defined and generate data that follows the that model.

## Examples

```python
import random
from mocktail import providers, models, fields, mocktail


class NameProvider(providers.Provider[str]):
    def provide(self, *args, **kwargs) -> str:
        return random.choice(["John", "Martin", "Peter", "Gary"])

    
class User(models.Model):
    first_name = fields.Str(min_length=3, max_length=20, provider=NameProvider)
    age = fields.Int(min_value=18, max_length=120)

    
users = mocktail(User, quantity=1000)

# [{"first_name": "Martin", "age": 23}, {"first_name": "Gary", "age": 41}, {"first_name": "John", "age": 62}, ...]

```

## Fields

### `mocktail.fields.Int`
Generates a random integer value within a specified range using `random.randint` function by default.

Arguments:
- `min_value` (int): Minimum value of the field (inclusive)
- `max_value` (int): Maximum value of the field (inclusive)
- `provider` (Provider): Custom provider class. It must conform to the `mocktail.providers.Provider` protocol.
- `generator` (Callable[[int, int], int]): Custom generator function. It is `random.randint` by default.

### `mocktail.fields.Str`
Generates a random string value within a specified length range. 

Arguments:
- `min_length` (int): Minimum length of the field (inclusive)
- `max_length` (int): Maximum length of the field (inclusive)
- `provider` (Provider): Custom provider class. It must conform to the `mocktail.providers.Provider` protocol.
- `generator` (Callable[[int, int], int]): Custom generator function. It is `random.randint` by default.

### `mocktail.fields.Bool`
Generates a random boolean. 

Arguments:
- `true_percentage` (int): Percentage of True value. Default is 50%.
- `provider` (Provider): Custom provider class. It must conform to the `mocktail.providers.Provider` protocol.

### `mocktail.fields.Date`
Generates a random `datetime.date` object. 

Arguments:
- `provider` (Provider): Custom provider class. It must conform to the `mocktail.providers.Provider` protocol.
- ?`serializer` (Serializer): Custom serializer class. It must conform to the `mocktail.serializers.Serializer` protocol. Can be used to serialize in the custom format. Default implementation uses `datetime.date.isoformat()` by default. 

### `mocktail.fields.Time`
Generates a random `datetime.time` object. 

Arguments:
- `provider` (Provider): Custom provider class. It must conform to the `mocktail.providers.Provider` protocol.
- ?`serializer` (Serializer): Custom serializer class. It must conform to the `mocktail.serializers.Serializer` protocol. Can be used to serialize in the custom format. Default implementation uses `datetime.time.isoformat()` by default. 

### `mocktail.fields.Datetime`
Generates a random `datetime.datetime` object. 

Arguments:
- `provider` (Provider): Custom provider class. It must conform to the `mocktail.providers.Provider` protocol.
- ?`serializer` (Serializer): Custom serializer class. It must conform to the `mocktail.serializers.Serializer` protocol. Can be used to serialize in the custom format. Default implementation uses `datetime.datetime.isoformat()` by default. 

## Providers

### `mocktail.providers.Provider`
A protocol that should be used to create any custom providers 

This is generic with generic type `T` that indicates type if generated values.

Methods:
- `Provider.provide(*args, **kwargs) -> T`: generate a single value of type `T`

### Here is the list of providers that are available in Mocktail:

### `mocktail.providers.FirstNameProvider`
Provider that generates first names. 

### `mocktail.providers.LastNameProvider`
Provider that generates last names. 

### `mocktail.providers.EmailProvider`
Provider that generates emails. 

### `mocktail.providers.ColorNameProvider`
Provider that generates color names. 

### `mocktail.providers.ColorCodeProvider`
Provider that generates color as hex number like #F342E1. 

### `mocktail.providers.UuidV4Provider`
Provider that generates a random UUID v4. 
