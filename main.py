
import logging

from fastapi import FastAPI

from models import CarEntry,CarExit,CarEntryresponse,CarExitresponse
from storage import vehStorage
from services import VehService


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI(title="Vehicle Parking")

storage = vehStorage()

service = VehService(storage)


# CREATE
@app.post("/Entryvehicles",response_model=CarEntryresponse,status_code=201)
def apply_Entry(veh):

    logger.info("Vehicle registration started %s",veh.reg_id)
    return service.entry(veh)

@app.post("/Exitvehicles",response_model=CarExitresponse,status_code=201)
def apply_Exit(veh):
    logger.info("Vehicle exit started %s",veh.reg_id)
    return service.exit(veh)


