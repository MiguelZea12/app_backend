from marshmallow import Schema, pre_load

class BaseSchema(Schema):
    @pre_load(pass_many=True)
    def string_to_none(self, data, many, **kwargs):
        def turn_to_none(x):
            return None if (x == "" or (x == 0 and type(x) == int)) else x

        if isinstance(data, dict):
            for k, v in data.items():
                data[k] = turn_to_none(v)
        elif isinstance(data, list):
            for i in range(len(data)):
                for k, v in data[i].items():
                    data[i][k] = turn_to_none(v)
        return data
