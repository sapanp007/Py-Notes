import json

json1 = {
    4: {90: 5},
    1: [2, 3, 4],
    3: {81: 9, 98: 0}
}

json2 = {
    4: {90: 5},
    1: [2, 3, 4],
    3: [{81: 9, 98: 0}, {81: 9, 98: 1}]
}


class JsonParse:
    def __init__(self, json_data):
        self.json_data = json_data
        self.keys = []
        self.values = []
        self.get_keys_and_values(self.json_data)

    def get_keys_and_values(self, json_data):
        if isinstance(json_data, dict):
            for key, value in json_data.items():
                self.keys.append(key)
                self.values.append(value)
                if isinstance(value, dict) or isinstance(value, list):
                    self.get_keys_and_values(value)
        elif isinstance(json_data, list):
            for data in json_data:
                self.get_keys_and_values(data)


if __name__ == "__main__":
    j1 = JsonParse(json1)
    print(json1)
    print(j1.keys)
    print(j1.values)

    # j2 = JsonParse(json2)
    # print(json2)
    # print(j2.keys)
    # print(j2.values)


