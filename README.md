# ayni
Chat with your codebase

## Install

The package requires tree-sitter c bindings. Since the c bindings can change depending on the os system, they are not included in the repo.

The github actions workflow builds and packages the project for three os systems for ease of use. Simply download the one for your os, and install it.

Alternatively, you can clone this repo and create them using the `Makefile` or `build.py`.
a
1. Download the latest release zip file for your os

    Mac
    ```sh
    curl -LO https://github.com/yemaney/ayni/releases/latest/download/ayni-macos-latest.zip
    ```
    Linux
    ```sh
    curl -LO https://github.com/yemaney/ayni/releases/latest/download/ayni-ubuntu-latest.zip
    ```
    Windows
    ```sh
    curl -LO https://github.com/yemaney/ayni/releases/latest/download/ayni-windows-latest.zip
    ``````

2. Pip install the zip fille

    ```sh
    pip install ayni-<os>-latest.zip
    ```

3. Delete the zip file
    ```sh
    rm ayni-<os>-latest.zip
    ```

## How to Use

1. Create a `.env` file in your working directory

    ```
    AYNI_DIR=ayni
    AYNI_EXTENSIONS=.py
    AYNI_EMBEDDING_PATH=./data.pkl
    OPENAI_KEY=sk-...
    ```

2. Run the help command

    ```sh
    ⬢ [Docker] ❯ ayni --help
    usage: ayni [-h] [-d D] [-e E] [-p P] [-em EM] [-k K] query

    Ayni: Chat with your codebase

    positional arguments:
    query       question for the codebase

    options:
    -h, --help  show this help message and exit
    -d D        codebase root director
    -e E        comma separate list of file extensions to search for. ex) .py,.go
    -p P        Path to .pkl file where the embedding cache will be stored
    -em EM      openai embedding model used to create embeddings
    -k K        openai api ke
    ```
3. Chat with your codebase. It will create a prompt using a relevant function from your codebase and will ask you to confirm before sending a request to GPT.

    ```
    ⬢ [Docker] ❯ ayni "how are embeddings being added to the cache?"
    ```
    ```
    Answer the query given the relevant code as context:

    QUERY: ###
    how are embeddings being added to the cache?
    ###

    CODE: ###
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
    ###

    Make a request with this prompt? Y/N:
    ```
