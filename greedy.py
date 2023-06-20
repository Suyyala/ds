# learning greedy algorithm in python

class greedy:
    def __init__(self):
        pass

    def greedy(self, states_needed, stations):
        final_stations = set()

        while states_needed:
            best_station = None
            states_covered = set()

            for station, states in stations.items():
                covered = states_needed & states
                if len(covered) > len(states_covered):
                    best_station = station
                    states_covered = covered

            states_needed -= states_covered
            final_stations.add(best_station)

        return final_stations
    

if __name__ == '__main__':
    states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
    stations = {}
    stations['kone'] = set(['id', 'nv', 'ut'])
    stations['ktwo'] = set(['wa', 'id', 'mt'])
    stations['kthree'] = set(['or', 'nv', 'ca'])
    stations['kfour'] = set(['nv', 'ut'])
    stations['kfive'] = set(['ca', 'az'])

    print(greedy().greedy(states_needed, stations))

