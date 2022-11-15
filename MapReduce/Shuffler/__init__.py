# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging


def main(words: list) -> dict:
    grouped_values = {}
    for word_tuple in words:
        (word, count) = word_tuple
        counter = grouped_values.get(word)

        if not counter:
            counter = []
            counter.append(count)
        else:
            counter.append(count)
            
        grouped_values[word] = counter
        
    return grouped_values
