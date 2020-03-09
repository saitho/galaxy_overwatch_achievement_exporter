# galaxy_overwatch_achievement_exporter
Exports achievements of Overwatch to GOG-compatible format

## Feature

This provides a Python API for fetching a user's achievements from their player profile on the Overwatch website.
Note that this requires the user to have a public profile.

It also provides a method to generate the achievement JSON export for GOG:

```shell script
inv update
```

### api_key

`api_key` is the id of the achievement. Blizzard does not directly provide IDs on their website.
That's the reason we're generating an own id from the achievement name, which seems to be the only constant.
The ID is a lowercase name where all special characters are removed.

## Development

Install dependencies:
```shell script
pip install -r requirements/dev.txt
```

Run tests:
```shell script
inv test
```