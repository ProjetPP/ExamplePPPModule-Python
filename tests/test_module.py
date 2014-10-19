from ppp_datamodel import Triple, Resource, Missing
from ppp_datamodel.communication import Request, Response
from ppp_core.tests import PPPTestCase
from example_ppp_module import app

class ModuleTest(PPPTestCase(app)):
    def testReplies(self):
        q = Triple(predicate=Resource(value='be'),
                   subject=Resource(value='you'),
                   object=Missing())
        a = []
        for x in {'bot', 'computer', 'flower'}:
            a.append(Response('en', 0.1,
                              Triple(predicate=Resource(value='be'),
                                     subject=Resource(value='I'),
                                     object=Resource(value=x))))
        # Asserts the response to q is in a.
        self.assertResponsesCount(Request('en', q), 1)
        self.assertResponsesIn(Request('en', q), a)
