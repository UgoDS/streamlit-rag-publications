import pickle
from data_model.state import State

from src.utils.date_utils import get_date_today_str


def create_file_name(filename: str, state: State):
    date_str = get_date_today_str()
    return f"data/{state.value}/{filename}_{date_str}.pk"


def save_pickle(file, file_path):
    with open(file_path, "wb") as handle:
        pickle.dump(file, handle, protocol=pickle.HIGHEST_PROTOCOL)
