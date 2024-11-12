# mocktail
Python data mocking package that can be used for:

* Unit testing
* Data quality testing
* Mocking data for API responses
* Generating seed data for databases

This package lets you define data models in a way similar to Django or Pydantic models and generate data that conforms to those models.

> [!WARNING]
> When I started preparing to publish this package to PyPi, I found out the name was already taken, so I’ll be renaming it soon. I’m still searching for a good name—if you have any ideas, please share them in  https://github.com/prudnikov/mocktail/issues/4

## Examples

See the playground.ipynb for examples.

## Fields (WIP)

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
