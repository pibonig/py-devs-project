import copy
import pickle


class Storage:
    @classmethod
    def save(cls, file_path, data):
        deep_data = copy.deepcopy(data)
        with open(file_path, 'wb') as f:
            pickle.dump(deep_data, f)

    @classmethod
    def load(cls, file_path):
        try:
            with open(file_path, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return None
