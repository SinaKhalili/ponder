# ponder

yet another GPT [C] [L] [I] addon prompts inspired by [this project](https://github.com/hwchase17/langchain)

```
➜ ponder ask "what should I write in the heading section of the README of my OpenAI GPT CLI tool?" --engine text-davinci-002
```
gives

## OpenAI GPT CLI tool

nice.

## Installation

```bash
$ git clone
$ cd ponder
$ pip install -r requirements.txt
```

## Usage

```bash
ponder ask QUESTION <FLAGS>

Where <FLAGS> are:
    --addon=ADDON
        Type: str, optional
        Default: None
        Addon to use. Can be "math", "react", or "sa"
    --engine=ENGINE
        Default: 'davinci-instruct-beta'
        The engine to use for completion, by default "davinci-instruct-beta"
    --max_tokens=MAX_TOKENS
        Default: 256
        The maximum number of tokens to generate, by default 64
    --temperature=TEMPERATURE
        Default: 1
        The temperature for the probability distribution used to sample next tokens, by default 0.9
    --top_p=TOP_P
        Default: 0.9
        The cumulative probability for top-p sampling, by default 1
    --frequency_penalty=FREQUENCY_PENALTY
        Default: 0.0
        The frequency penalty for this request, by default 0.0
    --presence_penalty=PRESENCE_PENALTY
        Default: 0.0
        The presence penalty for this request, by default 0.0
    --verbose=VERBOSE
        Default: False
        Whether to print the request and response, by default False
```

## Example

```bash
$ ponder ask "convert a ts to a mp4 in ffmepg"
# =>  ffmpeg -i input.ts -c copy output.mp4  <-- sometimes this
# =>  ffmpeg -i ts.ts -c:a copy -acodec copy -vcodec copy -ac 1 mp4.mp4 <-- sometimes this
```

Addon is some text before the prompt to prime it for some skill.

So far
- `--addon math` uses this legendary math prompt: https://twitter.com/goodside/status/1568448128495534081
- `--addon sa` "search_ask" uses a prompt from https://github.com/ofirpress/self-ask, of https://arxiv.org/abs/2210.03350
- `--addon reAct` uses a prompt from https://arxiv.org/pdf/2210.03629.pdf implemented in https://github.com/hwchase17/langchain

**Example**
    
```bash
$ ponder ask "how can I reverse engineer an API?" --engine text-davinci-002
# => There is no definitive answer to this question as it depends on the API and the level of reverse engineering 
#  > required. However, some tips on how to reverse engineer an API include:
#  > -Examining the API documentation to understand how the API works
#  > -Using a tool like Fiddler or Charles Proxy to intercept and examine API calls
#  > -Disassembling the API code using a tool like ILSpy or Reflector to understand how it works internally
```


[C]: https://gist.github.com/thesephist/28786aa80ac6e26241116c5ed2be97ca
[L]: https://github.com/abhagsain/ai-cli
[I]: https://github.com/hwchase17/langchain