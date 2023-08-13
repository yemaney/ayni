import pickle

from ayni.cache import cache_embedding, set_embedding_cache
from ayni.parse import get_python_functions


def test_embedding_cache(test_directory):
    embedding_cache = set_embedding_cache(f"{test_directory}/embeddings_cache.pkl")

    def rf(x, *args):
        return x

    for func in get_python_functions(f"{test_directory}/file2.py"):
        cache_embedding(func, embedding_cache, path=f"{test_directory}/embeddings_cache.pkl", model="", register_func=rf)

    assert "def func1():\n\tpass" in embedding_cache
    assert "def func2():\n\tpass" in embedding_cache
    assert "def func3():\n\tpass" in embedding_cache

    with open(f"{test_directory}/embeddings_cache.pkl", "rb") as fp:
        embedding_cache_from_disk = pickle.load(fp)

    assert "def func1():\n\tpass" in embedding_cache_from_disk
    assert "def func2():\n\tpass" in embedding_cache_from_disk
    assert "def func3():\n\tpass" in embedding_cache_from_disk
