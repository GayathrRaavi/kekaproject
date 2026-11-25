
from fastapi import HTTPException
from models import LeaveStatus


class LeaveService:

    def __init__(self, storage):

        self.storage = storage

    
    def entry(self,veh):
        for i in self.storage.get_all():
            if self.veh.vehtype not in ("CAR","BYKE"):
                return ValueError("only car or bike  parked")
        self.storage.add_veh(veh)
    def exit(self,veh):
        time=veh.minutesparked/20
        if  self.veh.vehtype=="CAR":
                        price=time*40
        if  self.veh.vehtype=="BIKE":
                        price=time*20
        veh.fee=price
        self.storage.exit_veh(veh)
                    

   