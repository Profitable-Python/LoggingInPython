# **kwargs example
from pprint import pprint


def main():
    # create dict
    key_word_arguments = {}

    # load dict with data
    key_word_arguments["name"] = "Ben McNeill"
    key_word_arguments["email"] = "ben@profitablepython.fm"
    key_word_arguments["podcast_name"] = "Profitable Python FM"
    key_word_arguments["social_media"] = {
        "instagram": "@bfmcneill",
        "twitter": ["@pypodcst", "@bfmcneill"],
        "twitch": "@bfmcneill",
        "linkedin": "@bfmcneill",
        "facebook": "@bfmcneill",
    }

    print_the_kwargs(**key_word_arguments)


def print_the_kwargs(**kwargs):
    pprint(kwargs)
    # print(kwargs["podcast_name"])


if __name__ == "__main__":
    main()
