# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df

from functools import reduce

def orchestrator_function(context: df.DurableOrchestrationContext):
    blob_text = yield context.call_activity('GetInputDataFn', "text")

    all_text = []
    for i in blob_text:
        all_text.append(context.call_activity('Mapper', i))
    prep = yield context.task_all(all_text) 
    result1 = reduce(lambda z, y :z + y, prep) 

    result2 = yield context.call_activity('Shuffler', result1)
    
    result3 = []
    for i in result2:
        x = yield context.call_activity('Reducer', (i, result2[i]))
        result3.append(x)
    return [result3]

main = df.Orchestrator.create(orchestrator_function)