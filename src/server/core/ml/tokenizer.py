import re, enchant

# Preprocessing #
#################

# English dictionary
en_US = None

# Special characters inserted on preprocessor
special_characters = [
    ("{space}", " "),
    ("{comma}", ","),
    ("{dot}", "."),
    ("{colon}", ":")
]

tags = ["name", "number", "email", "phone", "url", "phrase"]

# Regexes used in preprocessor
regexes = {
    # preprocessor regexes
    "number": r"[0-9]+((\.|,)([0-9]+)+)+",
    "email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "phone": r"(\(?[0-9]{3,5}\)?)[\s]?([\-\/])?\s?([0-9-]{4,10})(?![0-9])",
    "url": r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
    "name": r"((Mrs|Ms|Mr|Dr)\.? ?)?((([A-Z][a-z]+)(\-[A-Z][a-z]+)?)|([A-Z](\.|’)))( ?(([A-Z][a-z]+)(\-[A-Z][a-z]+)?))?",
    #            title                  first name                                 last name

    # processing regexes
    "tag": r"(<((name)|(number)|(email)|(phone)|(url)|(phrase))>)([^<]+)(<\/((name)|(number)|(email)|(phone)|(url)|(phrase))>)",
    "punctuation": r"([\.,:;!?'\"“”()]+)?([^\.,:;!?'\"“”()]+)?([\.,:;!?'\"“”()]+)?([^\.,:;!?'\"“”()]+)?",
    "hyphen_joined": r"[A-Za-z]([a-z]+)?(\-[a-z]+)+"
}

# Borrowed phrases
phrases = ["a priori", "BC", "piece of shit"]


# Preprocessing phrases
def phrases_preprocessing(text):
    for phrase in phrases:
        modified_phrase = phrase.replace(" ", "{space}")
        text = re.sub(re.compile(phrase, re.IGNORECASE),
                      " <phrase>" + modified_phrase.replace(" ", "{space}") + "</phrase> ", text)

    return text


# Preprocessing regexes
def more_preprocessing(text):
    phone_matches = re.finditer(regexes["phone"], text)
    for match in phone_matches:
        modified_phone = " <phone>" + match.group(0).replace(" ", "{space}") + "</phone> "
        text = text.replace(match.group(0), modified_phone, 1)

    number_matches = re.finditer(regexes["number"], text)
    for match in number_matches:
        modified_number = " <number>" + match.group(0).replace(",", "{comma}").replace(".", "{dot}") + "</number> "
        text = text.replace(match.group(0), modified_number, 1)

    email_matches = re.finditer(regexes["email"], text)
    for match in email_matches:
        modified_email = " <email>" + match.group(0).replace(".", "{dot}") + "</email> "
        text = text.replace(match.group(0), modified_email, 1)

    url_matches = re.finditer(regexes["url"], text)
    for match in url_matches:
        modified_url = " <url>" + match.group(0).replace(".", "{dot}").replace(":", "{colon}") + "</url> "
        text = text.replace(match.group(0), modified_url, 1)

    return text


# Preprocessing name regex
def name_preprocessing(text):
    name_matches = re.finditer(regexes["name"], text)
    for match in name_matches:

        group_count = 0
        replace_string = ""

        if match.group(2):
            replace_string += match.group(2) + "."
            group_count += 1

        if match.group(3):
            if group_count != 0:
                replace_string += "{space}"
            replace_string += match.group(3)
            group_count += 1

        if match.group(10):
            if group_count != 0:
                replace_string += "{space}"
            replace_string += match.group(10)
            group_count += 1

        if group_count > 1:
            text = text.replace(match.group(0), " <name>" + replace_string + "</name> ", 1)

    return text


# Preprocessing function
def preprocessing(text):
    text = re.sub(r"\r?\n", " ", text)
    text = phrases_preprocessing(text)
    text = name_preprocessing(text)
    text = more_preprocessing(text)

    return text


# Token processing #
####################

def process_token(token):
    global en_US

    # Process tagged tokens
    if "<" in token and ">" in token:
        token = re.sub(regexes["tag"], r"\9", token)
        for special_character in special_characters:
            token = token.replace(special_character[0], special_character[1])
        return [token]
    # Process untagged tokens
    else:
        ret_tokens = []
        match = re.match(regexes["punctuation"], token)
        for i in range(1, 5):
            if match.group(i):
                if i % 2 == 1:
                    for c in match.group(i):
                        ret_tokens.append(c)
                else:
                    ret_tokens.append(match.group(i))

        # Split by hyphens
        tmp_tokens = ret_tokens
        ret_tokens = []
        for ret_token in tmp_tokens:
            if re.match(regexes["hyphen_joined"], ret_token):
                for word in ret_token.split("-"):
                    ret_tokens.append(word)
            else:
                ret_tokens.append(ret_token)

        return ret_tokens


def process_tokens(tokens):
    final_tokens = []

    global en_US
    en_US = enchant.Dict("en_US")

    idx = 0
    while idx < len(tokens):

        token = tokens[idx]
        if token == " " or token == "":
            pass
        else:
            ret_tokens = process_token(token)
            for ret_idx in range(0, len(ret_tokens) - 1):
                final_tokens.append(ret_tokens[ret_idx])

            # Check if full word is splitted by hyphen #
            ############################################
            last_token = ret_tokens[len(ret_tokens) - 1]

            # Word ending in hyphen
            if last_token[len(last_token) - 1] == "-":

                next_ret_tokens = process_token(tokens[idx + 1])
                joined_word = last_token.replace("-", "", -1) + next_ret_tokens[0]

                # Joined word is in dictionary
                if (en_US.check(joined_word)):
                    final_tokens.append(joined_word)
                    for i in range(1, len(next_ret_tokens)):
                        final_tokens.append(next_ret_tokens[i])
                    idx += 1
                else:
                    final_tokens.append(last_token)

            else:
                final_tokens.append(last_token)

            ###########################################

        idx += 1

    return final_tokens


def tokenize(text):
    text = preprocessing(text)
    initial_tokens = text.split(" ")
    tokens = process_tokens(initial_tokens)

    return tokens
####################
