from marshmallow import Schema, fields
from schemas.shared_schemas import generate_list_schema


class EpisodeSchema(Schema):
    """Schema that represents a season episode"""
    number = fields.Int(description='Episode number')
    name = fields.Str(description='Episode name')
    overview = fields.Str(description='Episode overview')
    air_date = fields.Date(description='Episode air date')
    thumbnail_path = fields.Str(description='Episode thumbnail path')


class SeasonSchema(Schema):
    """Schema that represents a show season"""
    season_number = fields.Int(description='Number of the season.')
    name = fields.Str(description='Name of the season.')
    overview = fields.Str(description='Short summary of the season.')
    air_date = fields.Str(description='Air date of the season.')
    poster_path = fields.Str(description='Path to the poster image of the season.')
    episodes = fields.List(fields.Nested(EpisodeSchema), description='List of episodes of the season.')


class ShowSchema(Schema):
    id = fields.Int(description='Id of the show.')
    name = fields.Str(description='Name of the show.')
    overview = fields.Str(description='Short summary of the show.')
    first_air_date = fields.Date(description='First air date of the show.')
    poster_path = fields.Str(description='Path to the poster image of the show.')


class ShowDetailsSchema(ShowSchema):
    genres = fields.List(fields.Str(), description='Genres of the show.')
    finished_airing = fields.Bool(description='Whether the show has finished airing.')
    seasons = fields.List(fields.Nested(SeasonSchema), description='Seasons of the show.')


ShowListSchema = generate_list_schema(ShowSchema)
