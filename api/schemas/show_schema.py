import marshmallow as ma
from schemas.generate_list import generate_list_schema


class SeasonSchema(ma.Schema):
    air_date = ma.fields.Str(description='Air date of the season.')
    id = ma.fields.Int(description='Id of the season.')
    name = ma.fields.Str(description='Name of the season.')
    overview = ma.fields.Str(description='Short summary of the season.')
    poster_path = ma.fields.Str(
        description='Path to the poster image of the season.')
    season_number = ma.fields.Int(description='Number of the season.')


class ShowSchema(ma.Schema):
    id = ma.fields.Int(description='Id of the show.')
    name = ma.fields.Str(description='Name of the show.')
    genres = ma.fields.List(ma.fields.Str(), description='Genres of the show.')
    overview = ma.fields.Str(description='Short summary of the show.')
    poster_path = ma.fields.Str(
        description='Path to the poster image of the show.')
    seasons = ma.fields.List(ma.fields.Nested(
        SeasonSchema), description='Seasons of the show.')


ShowListSchema = generate_list_schema(ShowSchema)
