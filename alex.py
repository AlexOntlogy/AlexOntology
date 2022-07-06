from rdflib import *

alexithymia = Graph()

alexithymia.parse("alexont.ttl", format="ttl")

cq1 = '''
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX alex: <http://www.alexontology.com#>
select ?vacation where {?vacation a onto:Vacation}
'''

cq2 = '''
PREFIX alex: <http://www.alexontology.com#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>

select ?train ?plane where {?train a onto:Train.
                            ?plane a onto:Plane }
'''

cq3 = '''
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX alex: <http://www.alexontology.com#>

select ?Trip where {?Trip a onto:Trip.
                    ?Trip a onto:Group}
'''

cq4 = '''
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX alex: <http://www.alexontology.com#>

select ?trainTrip ?planeTrip  where {?trainTrip a onto:trainTrip.
                        ?trainTrip onto:hasBookedHotel ?hotel.
                        ?planeTrip a onto:planeTrip.
                        ?planeTrip onto:hasBookedHotel ?albergo
                        }

'''

cq5 = '''
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX alex: <http://www.alexontology.com#>

select ?vacation ?vacation2 ?vacation3 ?vacation4 where {?vacation a onto:Vacation.
                        ?vacation onto:hasTrip onto:DV_BolognaMadrid.
                        ?vacation2 a onto:Vacation.
                        ?vacation2 onto:hasTrip onto:DV_MadridAmsterdam.
                        ?vacation3 a onto:Vacation.
                        ?vacation3 onto:hasTrip onto:SV_AmstedamMadrid.
                        ?vacation4 a onto:Vacation.
                        ?vacation4 onto:hasTrip onto:SV_RomeAmsterdam   
                        }

'''

cq6 = '''

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX alex: <http://www.alexontology.com#>

select ?trainTrip ?duration where{ ?trainTrip a onto:trainTrip.
                        ?trainTrip onto:HourDuration ?duration.
}
'''

cq7 = '''

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX alex: <http://www.alexontology.com#>

select ?stars where{?Hotel a onto:Hotel.
                    ?Hotel onto:StarIndicator ?stars
}
'''

cq8 = '''

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX alex: <http://www.alexontology.com#>

select ?Hotel where{?Hotel a onto:Hotel.
                    ?Hotel onto:hasBreakfastIncluded true}
'''

cq9 = '''

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX alex: <http://www.alexontology.com#>

select ?Hotel ?trip where{
                    ?Hotel a onto:Hotel.
                    ?trip onto:hasBookedHotel ?Hotel;
                     onto:FisherVacation_FV
                    }
'''

cq10 = '''

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX alex: <http://www.alexontology.com#>

select ?trainTrip ?duration where {
                    ?trainTrip a onto:trainTrip.
                    ?trainTrip onto:hasBookedHotel onto:Multimedhostel.
                    ?trainTrip onto:HourDuration ?duration.
                    }
'''

cqs = [cq1, cq2, cq3, cq4, cq5, cq6, cq7, cq8, cq9, cq10]

for idx, cq in enumerate(cqs):
    print("Results for cq " + str(idx + 1) + ":")
    results = vacation_trips.query(cq)
    for result in results:
        print(result)
