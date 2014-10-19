"""Router of the module."""

import random

from ppp_datamodel import Triple, Resource, Missing
from ppp_datamodel.communication import Response

from ppp_core.exceptions import ClientError

class RequestHandler:
    def __init__(self, request):
        assert request.language == 'en'
        self._request = request.tree

    def answer(self):
        if self._request == Triple(predicate=Resource(value='be'),
                                   subject=Resource(value='you'),
                                   object=Missing()):
            # If the question has the form “You are ?.”
            # (ie. what the NLP should give from “What are you?”)
            answer = random.choice(['bot', 'computer', 'flower'])
            r =  Response('en', 0.1,
                          Triple(predicate=Resource(value='be'),
                                 subject=Resource(value='I'),
                                 object=Resource(value=answer)))
            return [r]
        else:
            return []
