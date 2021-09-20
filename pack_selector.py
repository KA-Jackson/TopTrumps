from pack import Pack
from cricket_pack_factory import CricketPackFactory

def __create_cricket_pack():
    factory = CricketPackFactory()
    pack = factory.create_pack()
    return pack

def __not_known():
    raise ValueError('Pack name not recognised')

def get_pack(name) -> Pack:

    pack_switch = {
        'cricket': __create_cricket_pack
    }

    func = pack_switch.get(name, __not_known)
    return func()