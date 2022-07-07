from rdflib import *

alexithymia = Graph()

alexithymia.parse("alexont.ttl", format="ttl")

cq1 = '''
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX alex: <http://www.alexontology.com#>
select ?statisticalTest where {?statisticalTest a alex:StatisticalTest}
'''

cq2 = '''
PREFIX alex: <http://www.alexontology.com#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

select ?clinicalDisorders where {?clinicalDisorders a alex:ClinicalDisorder}
'''

cq3 = '''
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX alex: <http://www.alexontology.com#>

 select ?questionnaires where {?questionnaires a alex:Questionnaire}
 '''

cq4 = '''
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX alex: <http://www.alexontology.com#>

select ?interoceptionBranches WHERE {?interoceptionBranches a alex:Interoception.
                        FILTER (?interoceptionBranches != alex:InteroceptiveConfusion)
                        FILTER (?interoceptionBranches != alex:Interoception)
                        }

'''

cq5 = '''
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX alex: <http://www.alexontology.com#>

select ?nonAffectiveState where {?nonAffectiveState a alex:PhysicalState.
                        ?nonAffectiveState alex:isConnectedTo alex:StateEmotionSImilarityQuestionnaire
                        }

'''

cq6 = '''

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX alex: <http://www.alexontology.com#>

select ?emotion where{ ?emotion a alex:Emotion.
                        ?emotion alex:isConnectedTo alex:StateEmotionSImilarityQuestionnaire
}
'''

cq7 = '''

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX alex: <http://www.alexontology.com#>

select ?brainRegion where{?brainRegion a alex:BrainRegion.
                    ?brainRegion alex:isInvolvedIn alex:Interoception
}
'''

cq8 = '''

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX alex: <http://www.alexontology.com#>

select ?social where{alex:Participant alex:isRecruitedVia ?social}
'''

cq9 = '''

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX alex: <http://www.alexontology.com#>

select DISTINCT ?number where{?questionnaire a alex:Questionnaire.
                            ?questionnaire alex:hasParticipantNumber ?number}
'''

cq10 = '''

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX alex: <http://www.alexontology.com#>

select ?scale where {
                    ?scale a alex:Scale.
                    FILTER (?scale != alex:StateEmotionSImilarityQuestionnaire)
                    FILTER (?scale != alex:InteroceptiveConfusionScore)
                    }
'''

cq11 = '''
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX alex: <http://www.alexontology.com#>

select DISTINCT ?age where{?questionnaire a alex:Questionnaire.
                            ?questionnaire alex:hasRangeOfAge ?age}
'''

cqs = [cq1, cq2, cq3, cq4, cq5, cq6, cq7, cq8, cq9, cq10, cq11]

for idx, cq in enumerate(cqs):
    print("Results for cq " + str(idx + 1) + ":")
    results = alexithymia.query(cq)
    for result in results:
        print(result)
