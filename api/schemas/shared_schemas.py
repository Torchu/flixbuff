from marshmallow import Schema, fields


def generate_list_schema(base_schema):
    '''Function that generates a list schema from a base schema'''
    atributes = {
        'items': fields.Nested(base_schema, many=True, dump_only=True),
        'total': fields.Int(dump_only=True),
        'Meta': type('Meta', (object,), {'strict': True})
    }

    name = base_schema.__name__ + 'List'
    new_class = type(name, (Schema,), atributes)
    return new_class


class QueryParametersSchema(Schema):
    query = fields.Str(description='Query to search')
