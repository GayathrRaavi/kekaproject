
class vehStorage:

    def __init__(self):

        self.slots = {}
        self.slot={"b1"=0,
            "b2"=0,
            "c1"=0,
            "c2"=0,}
        self.slot_id ="a"

    # CREATE
    def add_veh(self, veh):
        self.slots[veh.regid] = veh
        for i in self.slot:
            if self.slot[i]==0 and self.slots[slot]=="Byke":
                self.slots=self.slot[i]

        return self.slots[veh.regid]

    def exit_veh(self,veh):
        
        if veh.slot in self.slots:
            self.slot[veh.slot[veh.regid]]=0
            
        self.slots.pop(veh.regid)
        return self.slots[veh.regid]
    def get_all(self):
        return list(self.slots)
            