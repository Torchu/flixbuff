import marshmallow as ma


def generate_list_schema(base_schema):
    '''Function that generates a list schema from a base schema'''
    atributes = {
        'items': ma.fields.Nested(base_schema, many=True, dump_only=True),
        'total': ma.fields.Int(dump_only=True),
        'Meta': type('Meta', (object,), {'strict': True})
    }

    name = base_schema.__name__ + 'List'
    new_class = type(name, (ma.Schema,), atributes)
    return new_class


class QueryParametersSchema(ma.Schema):
    query = ma.fields.Str(description='Query to search')
