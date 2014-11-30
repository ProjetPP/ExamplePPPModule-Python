"""Router of the module."""

import random

from ppp_datamodel import Triple, Resource, Missing
from ppp_datamodel.communication import TraceItem, Response

from ppp_core.exceptions import ClientError

YOU_ARE = ['an artificial intelligence', 'a computer', 'a program',
           'a something great', 'a question-answering tool']
I_AM = ['someone asking questions', 'someone great', 'an internaut']

class RequestHandler:
    def __init__(self, request):
        self._request = request.tree

    def answer(self):
        if self._request == Triple(predicate=Resource(value='identity'),
                                   subject=Resource(value='you'),
                                   object=Missing()):
            # If the question has the form “You identity ?.”
            # (ie. what the NLP should give from “What are you?”)
            return self.produce_answer(random.choice(YOU_ARE))
        elif self._request == Triple(predicate=Resource(value='identity'),
                                   subject=Resource(value='I'),
                                   object=Missing()):
            return self.produce_answer(random.choice(I_AM))
        else:
            return []

    def produce_answer(self, answer):
        t = Resource(value=answer)
        m = {'accuracy': 1, 'relevance': 0.1}
        r = Response('en', t, m, [TraceItem('ExampleModule', t, m)])
        return [r]
