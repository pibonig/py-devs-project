import pickle


class Storage:
    @classmethod
    def save(cls, file_path, data):
        with open(file_path, 'wb') as f:
            pickle.dump(data, f)

    @classmethod
    def load(cls, file_path):
        with open(file_path, 'rb') as f:
            return pickle.load(f)
