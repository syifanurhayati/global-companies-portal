import rdflib
from rdflib.store import NO_STORE, VALID_STORE
from rdflib import plugin, ConjunctiveGraph
from rdflib.store import Store

g = ConjunctiveGraph('Sleepycat')
g.open('./company', create=False)
# g.serialize(format='nt')

# g = Graph()
# g.parse("companies_sorted_test.ntriples", format="nt")

stringquery = """SELECT ?sub ?obj 
                WHERE { ?sub <http://globalcompany.org/hasName> ?obj . }
                LIMIT 50"""

qres = g.query(stringquery)

print(len(g))
for row in qres:
    print(str(row.sub) + '\t' + str(row.obj))

g.close()