import marshmallow as ma
from schemas.shared_schemas import generate_list_schema


class EpisodeSchema(ma.Schema):
    """Schema that represents a season episode"""
    number = ma.fields.Int(description='Episode number')
    name = ma.fields.Str(description='Episode name')
    overview = ma.fields.Str(description='Episode overview')
    air_date = ma.fields.Date(description='Episode air date')
    thumbnail_path = ma.fields.Str(description='Episode thumbnail path')


class SeasonSchema(ma.Schema):
    """Schema that represents a show season"""
    season_number = ma.fields.Int(description='Number of the season.')
    name = ma.fields.Str(description='Name of the season.')
    overview = ma.fields.Str(description='Short summary of the season.')
    air_date = ma.fields.Str(description='Air date of the season.')
    poster_path = ma.fields.Str(description='Path to the poster image of the season.')
    episodes = ma.fields.List(ma.fields.Nested(EpisodeSchema), description='List of episodes of the season.')


class ShowSchema(ma.Schema):
    id = ma.fields.Int(description='Id of the show.')
    name = ma.fields.Str(description='Name of the show.')
    overview = ma.fields.Str(description='Short summary of the show.')
    first_air_date = ma.fields.Date(description='First air date of the show.')
    poster_path = ma.fields.Str(description='Path to the poster image of the show.')


class ShowDetailsSchema(ShowSchema):
    genres = ma.fields.List(ma.fields.Str(), description='Genres of the show.')
    finished_airing = ma.fields.Bool(description='Whether the show has finished airing.')
    seasons = ma.fields.List(ma.fields.Nested(SeasonSchema), description='Seasons of the show.')


ShowListSchema = generate_list_schema(ShowSchema)
