import streamlit as st
from data_model.loader import LoaderDescription
from src.utils.config_utils import load_config


def display_loader_description(config_path: str):
    list_loaders = config_to_loader_description(config_path)
    cols = st.columns(len(list_loaders))
    for idx, loader_ in enumerate(list_loaders):
        cols[idx].divider()
        cols[idx].markdown(
            f"# [{loader_.name}]({loader_.url}) \n :star: {loader_.github_stars}"
        )
        cols[idx].write(loader_.description)


def config_to_loader_description(config_path: str) -> LoaderDescription:
    configs = load_config(config_path)
    return [LoaderDescription(**v) for k, v in configs.items()]
