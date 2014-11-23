"""Router of the module."""

import random

from ppp_datamodel import Triple, Resource, Missing
from ppp_datamodel.communication import TraceItem, Response

from ppp_core.exceptions import ClientError

class RequestHandler:
    def __init__(self, request):
        assert request.language == 'en'
        self._request = request.tree

    def answer(self):
        if self._request == Triple(predicate=Resource(value='identity'),
                                   subject=Resource(value='you'),
                                   object=Missing()):
            # If the question has the form “You are ?.”
            # (ie. what the NLP should give from “What are you?”)
            answer = random.choice(['bot', 'computer', 'flower'])

            t = Resource(value=answer)
            m = {'accuracy': 1, 'relevance': 0.1}
            r = Response('en', t, m, [TraceItem('ExampleModule', t, m)])
            return [r]
        else:
            return []
