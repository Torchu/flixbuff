from marshmallow import Schema, fields
from schemas.shared_schemas import generate_list_schema


class EpisodeSchema(Schema):
    """Schema that represents a season episode"""
    number = fields.Int(metadata={'description': 'Episode number'})
    name = fields.Str(metadata={'description': 'Episode name'})
    overview = fields.Str(metadata={'description': 'Episode overview'})
    air_date = fields.Date(metadata={'description': 'Episode air date'})
    thumbnail_path = fields.Str(metadata={'description': 'Episode thumbnail path'})


class SeasonSchema(Schema):
    """Schema that represents a show season"""
    season_number = fields.Int(metadata={'description': 'Number of the season.'})
    name = fields.Str(metadata={'description': 'Name of the season.'})
    overview = fields.Str(metadata={'description': 'Short summary of the season.'})
    air_date = fields.Str(metadata={'description': 'Air date of the season.'})
    poster_path = fields.Str(metadata={'description': 'Path to the poster image of the season.'})
    episodes = fields.List(fields.Nested(EpisodeSchema), metadata={'description': 'List of episodes of the season.'})


class ShowSchema(Schema):
    id = fields.Int(metadata={'description': 'Id of the show.'})
    name = fields.Str(metadata={'description': 'Name of the show.'})
    overview = fields.Str(metadata={'description': 'Short summary of the show.'})
    first_air_date = fields.Date(metadata={'description': 'First air date of the show.'})
    poster_path = fields.Str(metadata={'description': 'Path to the poster image of the show.'})


class ShowDetailsSchema(ShowSchema):
    genres = fields.List(fields.Str(), metadata={'description': 'Genres of the show.'})
    finished_airing = fields.Bool(metadata={'description': 'Whether the show has finished airing.'})
    seasons = fields.List(fields.Nested(SeasonSchema), metadata={'description': 'Seasons of the show.'})


ShowListSchema = generate_list_schema(ShowSchema)
