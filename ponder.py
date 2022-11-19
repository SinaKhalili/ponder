import openai
from prompts import prompts


class Ponder:
    """
    A class used to represent an Engine
    """

    def __init__(self, key) -> None:
        openai.api_key = key

    def ask(
        self,
        prompt,
        addon=None,
        engine="davinci-instruct-beta",
        max_tokens=64,
        temperature=0.9,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        verbose=False,
    ):
        """
        Complete a prompt with OpenAI's GPT-3 API.

        Parameters
        ----------
        prompt : str
            The prompt to complete.
        addons : str, optional
            An addon to add to the prompt, by default None.
            Can be "math", "self_ask_with_search", or "reAct"
        engine : str, optional
            The engine to use for completion, by default "davinci-instruct-beta"
        max_tokens : int, optional
            The maximum number of tokens to generate, by default 64
        temperature : float, optional
            The temperature for the probability distribution used to sample
            next tokens, by default 0.9
        top_p : float, optional
            The cumulative probability for top-p sampling, by default 1
        frequency_penalty : float, optional
            The frequency penalty for this request, by default 0.0
        presence_penalty : float, optional
            The presence penalty for this request, by default 0.0
        verbose : bool, optional
            Whether to print the request and response, by default False
        """
        if addon is not None:
            try:
                addon_text = prompts[addon]["text"]
                prompt = addon_text + prompt
            except KeyError:
                print(f"Addon {addon} not found. Skipping.")

        response = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
        )
        if verbose:
            print(response)
        return response["choices"][0]["text"]

    def list_engines():
        """List all available engines."""
        engines = openai.Engine.list()["data"]
        return "\n".join([f"{e['id']}: {e['owner']}" for e in engines])
