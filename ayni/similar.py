"""This module is concerned with code related to finding the most similar context for given queries
"""

from openai.embeddings_utils import (
    distances_from_embeddings,
    get_embedding,
    indices_of_nearest_neighbors_from_distances,
)


def get_most_similar(query: str, model: str, embedding_cache: dict) -> str:
    """get_most_similar finds the most similar function in the embedding_cache to a given query.

    Parameters
    ----------
    query : str
        A string representing a question a user has for the code
    model : str
        The name of the openai embedding model to use for generating embeddings
    embedding_cache : dict
        A dictionary containing the cached embeddings

    Returns
    -------
    string
        the most similar function to the query
    """
    query_embedding = get_embedding(query, model)

    functions = [k for k, _ in embedding_cache.items()]
    embeddings = [v for _, v in embedding_cache.items()]

    distances = distances_from_embeddings(query_embedding, embeddings)
    indices_of_nearest_neighbors = indices_of_nearest_neighbors_from_distances(distances)

    return [functions[i] for i in indices_of_nearest_neighbors][0]
