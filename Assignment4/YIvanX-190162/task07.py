# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tV5j-DRcpPtoJGoMj8v2DSqR_9wyXeiE

**Task 07: Querying RDF(s)**
"""

!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/resources/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""
# TO DO
from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://somewhere#")
print("RDFLib:")
for s,p,o in g.triples((None,RDFS.subClassOf,ns.Person)):
  print(s)

q1 = prepareQuery('''
  SELECT ?Subject WHERE { 
    ?Subject rdfs:subClassOf ns:Person.
  }
  ''',
  initNs = { "rdfs": RDFS, "ns":ns}
)

# Visualize the results
print("SPARQL:")
for r in g.query(q1):
  print(r.Subject)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**"""
# TO DO
print("RDFLib:")
for s,p,o in g.triples((None,RDF.type,ns.Person)):
  print(s)

for s,p,o in g.triples((None,RDFS.subClassOf,ns.Person)):
  for s1,p1,o1 in g.triples((None,RDF.type,s)):
    print(s1)

q2 = prepareQuery('''
  SELECT DISTINCT ?Subject WHERE { 
    {
    ?Subject rdf:type ns:Person.        
    }
    UNION {
        ?Prep rdfs:subClassOf* ns:Person.
        ?Subject rdf:type ?Prep
    }
  }
  ''',
  initNs = { "rdfs": RDFS, "ns":ns,"rdf":RDF}
)

# Visualize the results
print("SPARQL:")
for r in g.query(q2):
  print(r.Subject)

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**"""
# TO DO
print("RDFLib:")
for s,p,o in g.triples((None,RDF.type,ns.Person)):
  print("Person;"+ s)
  print("Properties:")
  for s1,p1,o1 in g.triples((s,None,None)):
    print(p1)

for s,p,o in g.triples((None,RDFS.subClassOf,ns.Person)):
  for s1,p1,o1 in g.triples((None,RDF.type,s)):
    print("Person" +s1)
    print("Properties:")
    for s2,p2,o2 in g.triples((s1,None,None)):
        print(p2)

q2 = prepareQuery('''
  SELECT ?Subject ?Prop ?Value WHERE { 
    {
    ?Subject rdf:type ns:Person.        
    }
    UNION {
        ?Prep rdfs:subClassOf* ns:Person.
        ?Subject rdf:type ?Prep
    }
    ?Subject ?Prop ?Value
  }
  ''',
  initNs = { "rdfs": RDFS, "ns":ns,"rdf":RDF}
)

# Visualize the results
print("SPARQL:")
for r in g.query(q2):
  print(r.Subject,r.Prop,r.Value)