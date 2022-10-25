import uuid
import json

from rentomatic.domain.room import Room
from rentomatic.serializers.room import RoomJsonEncoder

def test_serialize_domain_room():
    code = uuid.uuid4()
    init_dict = {
        "code": code,
        "size": 200,
        "price": 10,
        "longitude": 242.24,
        "latitude": 25.24,
    }

    room = Room.from_dict(init_dict)


    expected_json = f"""
        {{
        "code": "{code}",
        "size": 200,
        "price": 10,
        "longitude": 242.24,
        "latitude": 25.24
        }}
    """

    json_room = json.dumps(room, cls=RoomJsonEncoder)
    
    assert json.loads(json_room) == json.loads(expected_json)