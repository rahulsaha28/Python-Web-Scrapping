from Project_demo import GraphData

c = GraphData('https://digital.ucas.com/coursedisplay/results/providers?destination=Undergraduate&distanceFromPostcode=25&studyYear=2021&sort=MostRelevant')
c.gel_all_link()
c.made_data()
c.save_as_csv_file()











