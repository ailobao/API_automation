import json
import os

def load_test_data(file_name):

    current_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'data', file_name)

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data