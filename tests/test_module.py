from ppp_datamodel import Triple, Resource, Missing
from ppp_datamodel.communication import Request, TraceItem, Response
from ppp_libmodule.tests import PPPTestCase
from example_ppp_module import app

class ModuleTest(PPPTestCase(app)):
    def testReplies(self):
        q = Triple(predicate=Resource(value='be'),
                   subject=Resource(value='you'),
                   object=Missing())
        a = []
        m = {'accuracy': 1, 'relevance': 0.1}
        for x in {'bot', 'computer', 'flower'}:
            t = Triple(predicate=Resource(value='be'),
                                          subject=Resource(value='I'),
                                          object=Resource(value=x))
            a.append(Response('en', t, m, [TraceItem('ExampleModule', t, m)]))
        # Asserts the response to q is in a.
        self.assertResponsesCount(Request('42', 'en', q, {}, []), 1)
        self.assertResponsesIn(Request('42', 'en', q, {}, []), a)
