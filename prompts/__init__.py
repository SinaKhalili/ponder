from .math import math_prompt
from .self_ask_with_search import self_ask_with_search_prompt
from .reAct import reAct_prompt

prompts = {
    "math": math_prompt,
    "self_ask_with_search": self_ask_with_search_prompt,
    "sa": self_ask_with_search_prompt,
    "reAct": reAct_prompt,
    "act": reAct_prompt,
    "react": reAct_prompt,
}
