from spaceone.monitoring.manager.incident import Incident


class Incident_1_2(Incident):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _parse(self):
        print(self.incident)
