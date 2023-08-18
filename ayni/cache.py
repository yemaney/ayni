"""This module is concerned with code responsible managing the cache for storing embeddings.
"""

import pickle
from typing import Callable

from .similar import get_embedding


def set_embedding_cache(path: str) -> dict:
    """set_embedding_cache sets up cache used to store embeddings. It tries to
    load a cache from a pickle file, and creates a new one if it can find one.
    The new cache will be stored as a pickle file.

    Parameters
    ----------
    path : str, optional
        Path to the file where the embedding cache dictionary will be stored

    Returns
    -------
    dict
        A dictionary containing cached embeddings.
    """
    try:
        with open(path, "rb") as fp:
            embedding_cache = pickle.load(fp)
    except FileNotFoundError:
        embedding_cache = {}
    with open(path, "wb") as fp:
        pickle.dump(embedding_cache, fp)
    return embedding_cache


def cache_embedding(
    function: str,
    embedding_cache: dict,
    path: str,
    model: str,
    register_func: Callable = get_embedding,
) -> None:
    """cache_embedding adds the embeddings for a function to the embedding_cache dictionary
    in memory and persists it to the pickle file.

    Parameters
    ----------
    function : str
        The string representation of the function for which embeddings are being cached
    embedding_cache : dict
        A dictionary containing the cached embeddings
    path : str, optional
        Path to the file where the embedding cache dictionary will be stored
    model : str, optional
        The name of the openai embedding model to use for generating embeddings
    register_func : Callable, optional
        A function used to generate embeddings, by default get_embedding
    """
    if function not in embedding_cache.keys():
        embedding_cache[function] = register_func(function, model)
        with open(path, "wb") as embedding_cache_file:
            pickle.dump(embedding_cache, embedding_cache_file)
