from pydantic import BaseModel
from server.types.fakebool import FakeBool


class ReservationsParameters(BaseModel):
    regime: str

    repasmidi_1: FakeBool
    repassoir_1: FakeBool

    repasmidi_2: FakeBool
    repassoir_2: FakeBool

    repasmidi_3: FakeBool
    repassoir_3: FakeBool

    repasmidi_4: FakeBool
    repassoir_4: FakeBool

    repasmidi_5: FakeBool
    repassoir_5: FakeBool

    repasmidi_6: FakeBool
    repassoir_6: FakeBool

    repasmidi_7: FakeBool
    repassoir_7: FakeBool
