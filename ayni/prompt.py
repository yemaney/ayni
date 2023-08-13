"""This module is concerned with code related to creating prompts and making GPT requests.
"""
import sys

import openai


def create_prompt(query: str, function: str) -> str:
    """create_prompt creates a structured prompt for GPT using the users
    query and the most similar function as context

    Parameters
    ----------
    query : str
        A string representing a question a user has for the code
    function : str
        The string representation of the most simlar function to the query

    Returns
    -------
    str
        a formated prompt for GPT
    """
    return f"""Answer the query given the relevant code as context:

QUERY: ###
{query}
###

CODE: ###
{function}
###
"""


def gpt_request(prompt: str) -> str:
    """gpt_request attemps to make a request to GPT chat completions api

    Parameters
    ----------
    prompt : str
        The prompt sent to GPT

    Returns
    -------
    str
        GPT's response to the prompt
    """
    try:
        res = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
        return res["choices"][0]["message"]["content"]
    except Exception as e:
        print(e)
        sys.exit(1)
