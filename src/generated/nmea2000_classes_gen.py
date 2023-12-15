#   Python code generated by NMEA message router application (c) Sterwen Technology 2023
#   generated on 2023-37-15:17:37
#   do not modify code


import struct

from nmea2000.generated_base import NMEA2000Payload, NMEA2000DecodedMsg, check_valid
from generated.nmea2000_pb2 import nmea2000_decoded_pb
from nmea2000.nmea2000_msg import NMEA2000Msg

from generated.nmea2000_classes_gen_pb2 import *
class Pgn126992Class(NMEA2000Payload):

    _pgn = 126992
    _name = 'System Time'
    _decode_struct = struct.Struct('<BBHi')
    _decode_struct_size = _decode_struct.size
    __slots__ = ('_system_id', '_source', '_date', '_time')

    @classmethod
    def size(cls) -> int:
        return cls._decode_struct_size

    _source_enum = {
        0: 'GPS',
        1: 'GLONASS',
        2: 'Radio Station',
        3: 'Local Cesium clock',
        4: 'Local Rubidium clock',
        5: 'Local Crystal clock'
        }


    def __init__(self, message=None, protobuf=None):
        super().__init__(message, protobuf)

    @property
    def pgn(self) -> int:
        return self._pgn

    @property
    def name(self) -> str:
        return self._name

    @property
    def system_id(self) -> int:
        return self._system_id

    @property
    def source(self) -> int:
        return self._source

    @property
    def date(self) -> int:
        return self._date

    @property
    def time(self) -> float:
        return self._time

    @system_id.setter
    def system_id(self, value: int):
        self._system_id = value

    @source.setter
    def source(self, value: int):
        self._source = value

    @date.setter
    def date(self, value: int):
        self._date = value

    @time.setter
    def time(self, value: float):
        self._time = value

    @property
    def source_text(self) -> str:
        return self._source_enum.get(self._source, 'source key error')

    def decode_payload_segment(self, payload, from_byte):
        val = self._decode_struct.unpack_from(payload, from_byte)
        self._system_id = val[0]
        self._source = (val[1] << 4) & 0xF
        self._date = val[2]
        self._time = val[3] * 0.0001

    def encode_payload_segment(self, from_byte):
        buf_size = self.__class__.size()
        buffer = bytearray(buf_size)
        v0 = int(self._time / 0.0001)
        self._decode_struct.pack_into(buffer, from_byte, self._system_id, self._source, self._date)

    def from_protobuf(self, message: Pgn126992ClassPb):
        self._system_id = message.system_id
        self._source = message.source
        self._date = message.date
        self._time = message.time

    def as_protobuf(self) -> Pgn126992ClassPb:
        message = Pgn126992ClassPb()
        message.system_id = self._system_id
        message.source = self._source
        message.date = self._date
        message.time = self._time
        return message

    def __str__(self):
        return f'PGN{self._pgn}({self._name}) [system_id={self._system_id}, source={self._source}, date={self._date}, time={self._time}]'


class Pgn126993Class(NMEA2000Payload):

    _pgn = 126993
    _name = 'Heartbeat'
    _decode_struct = struct.Struct('<hBBI')
    _decode_struct_size = _decode_struct.size
    __slots__ = ('_interval', '_status')

    @classmethod
    def size(cls) -> int:
        return cls._decode_struct_size



    def __init__(self, message=None, protobuf=None):
        super().__init__(message, protobuf)

    @property
    def pgn(self) -> int:
        return self._pgn

    @property
    def name(self) -> str:
        return self._name

    @property
    def interval(self) -> float:
        return self._interval

    @property
    def status(self) -> int:
        return self._status

    @interval.setter
    def interval(self, value: float):
        self._interval = value

    @status.setter
    def status(self, value: int):
        self._status = value

    def decode_payload_segment(self, payload, from_byte):
        val = self._decode_struct.unpack_from(payload, from_byte)
        self._interval = val[0] * 10.0
        self._status = val[1]

    def encode_payload_segment(self, from_byte):
        buf_size = self.__class__.size()
        buffer = bytearray(buf_size)
        v0 = int(self._interval / 10.0)
        self._decode_struct.pack_into(buffer, from_byte, v0)

    def from_protobuf(self, message: Pgn126993ClassPb):
        self._interval = message.interval
        self._status = message.status

    def as_protobuf(self) -> Pgn126993ClassPb:
        message = Pgn126993ClassPb()
        message.interval = self._interval
        message.status = self._status
        return message

    def __str__(self):
        return f'PGN{self._pgn}({self._name}) [interval={self._interval}, status={self._status}]'


class Pgn129025Class(NMEA2000Payload):

    _pgn = 129025
    _name = 'Position, Rapid Update'
    _decode_struct = struct.Struct('<ii')
    _decode_struct_size = _decode_struct.size
    __slots__ = ('_latitude', '_longitude')

    @classmethod
    def size(cls) -> int:
        return cls._decode_struct_size



    def __init__(self, message=None, protobuf=None):
        super().__init__(message, protobuf)

    @property
    def pgn(self) -> int:
        return self._pgn

    @property
    def name(self) -> str:
        return self._name

    @property
    def latitude(self) -> float:
        return self._latitude

    @property
    def longitude(self) -> float:
        return self._longitude

    @latitude.setter
    def latitude(self, value: float):
        self._latitude = value

    @longitude.setter
    def longitude(self, value: float):
        self._longitude = value

    def decode_payload_segment(self, payload, from_byte):
        val = self._decode_struct.unpack_from(payload, from_byte)
        self._latitude = val[0] * 1e-07
        self._longitude = val[1] * 1e-07

    def encode_payload_segment(self, from_byte):
        buf_size = self.__class__.size()
        buffer = bytearray(buf_size)
        v0 = int(self._latitude / 1e-07)
        v1 = int(self._longitude / 1e-07)
        self._decode_struct.pack_into(buffer, from_byte, v0)

    def from_protobuf(self, message: Pgn129025ClassPb):
        self._latitude = message.latitude
        self._longitude = message.longitude

    def as_protobuf(self) -> Pgn129025ClassPb:
        message = Pgn129025ClassPb()
        message.latitude = self._latitude
        message.longitude = self._longitude
        return message

    def __str__(self):
        return f'PGN{self._pgn}({self._name}) [latitude={self._latitude}, longitude={self._longitude}]'


class Pgn129026Class(NMEA2000Payload):

    _pgn = 129026
    _name = 'COG & SOG, Rapid Update'
    _decode_struct = struct.Struct('<BBhhH')
    _decode_struct_size = _decode_struct.size
    __slots__ = ('_system_id', '_COG_reference', '_COG', '_SOG')

    @classmethod
    def size(cls) -> int:
        return cls._decode_struct_size

    _COG_reference_enum = {
        0: 'True',
        1: 'Magnetic'
        }


    def __init__(self, message=None, protobuf=None):
        super().__init__(message, protobuf)

    @property
    def pgn(self) -> int:
        return self._pgn

    @property
    def name(self) -> str:
        return self._name

    @property
    def system_id(self) -> int:
        return self._system_id

    @property
    def COG_reference(self) -> int:
        return self._COG_reference

    @property
    def COG(self) -> float:
        return self._COG

    @property
    def SOG(self) -> float:
        return self._SOG

    @system_id.setter
    def system_id(self, value: int):
        self._system_id = value

    @COG_reference.setter
    def COG_reference(self, value: int):
        self._COG_reference = value

    @COG.setter
    def COG(self, value: float):
        self._COG = value

    @SOG.setter
    def SOG(self, value: float):
        self._SOG = value

    @property
    def COG_reference_text(self) -> str:
        return self._COG_reference_enum.get(self._COG_reference, 'COG_reference key error')

    def decode_payload_segment(self, payload, from_byte):
        val = self._decode_struct.unpack_from(payload, from_byte)
        self._system_id = val[0]
        self._COG_reference = val[1] & 0x3
        self._COG = val[2] * 0.005729577951308233
        self._SOG = val[3] * 0.01

    def encode_payload_segment(self, from_byte):
        buf_size = self.__class__.size()
        buffer = bytearray(buf_size)
        v0 = int(self._COG / 0.005729577951308233)
        v1 = int(self._SOG / 0.01)
        self._decode_struct.pack_into(buffer, from_byte, self._system_id, self._COG_reference, v0)

    def from_protobuf(self, message: Pgn129026ClassPb):
        self._system_id = message.system_id
        self._COG_reference = message.COG_reference
        self._COG = message.COG
        self._SOG = message.SOG

    def as_protobuf(self) -> Pgn129026ClassPb:
        message = Pgn129026ClassPb()
        message.system_id = self._system_id
        message.COG_reference = self._COG_reference
        message.COG = self._COG
        message.SOG = self._SOG
        return message

    def __str__(self):
        return f'PGN{self._pgn}({self._name}) [system_id={self._system_id}, COG_reference={self._COG_reference}, COG={self._COG}, SOG={self._SOG}]'


class Pgn129029Class(NMEA2000Payload):

    class Ref_StationsClass:
        _decode_struct = struct.Struct('<Bh')
        _decode_struct_size = _decode_struct.size
        __slots__ = ('_station_id', '_GNSS_type', '_age_DGNSS_correction')

        @classmethod
        def size(cls) -> int:
            return cls._decode_struct_size

        _GNSS_type_enum = 'GNSS type'

        def __init__(self, protobuf=None):
            if protobuf is not None:
                self.from_protobuf(protobuf)

        @property
        def station_id(self) -> int:
            return self._station_id

        @property
        def GNSS_type(self) -> int:
            return self._GNSS_type

        @property
        def age_DGNSS_correction(self) -> float:
            return self._age_DGNSS_correction

        @station_id.setter
        def station_id(self, value: int):
            self._station_id = value

        @GNSS_type.setter
        def GNSS_type(self, value: int):
            self._GNSS_type = value

        @age_DGNSS_correction.setter
        def age_DGNSS_correction(self, value: float):
            self._age_DGNSS_correction = value

        @property
        def GNSS_type_text(self) -> str:
            return NMEA2000Payload.resolve_global_enum(self._GNSS_type_enum, self._GNSS_type)

        def decode_payload_segment(self, payload, from_byte):
            val = self._decode_struct.unpack_from(payload, from_byte)
            self._station_id = val[0] & 0xF
            self._GNSS_type = (val[0] << 4) & 0xF
            self._age_DGNSS_correction = val[1] * 0.01

        def encode_payload_segment(self, from_byte):
            buf_size = self.__class__.size()
            buffer = bytearray(buf_size)
            v0 = int(self._age_DGNSS_correction / 0.01)
            self._decode_struct.pack_into(buffer, from_byte, self._station_id, self._GNSS_type)

        def from_protobuf(self, message: Pgn129029ClassPb.Ref_StationsClassPb):
            self._station_id = message.station_id
            self._GNSS_type = message.GNSS_type
            self._age_DGNSS_correction = message.age_DGNSS_correction

        def as_protobuf(self) -> Pgn129029ClassPb.Ref_StationsClassPb:
            message = Pgn129029ClassPb.Ref_StationsClassPb()
            message.station_id = self._station_id
            message.GNSS_type = self._GNSS_type
            message.age_DGNSS_correction = self._age_DGNSS_correction
            return message


    _pgn = 129029
    _name = 'GNSS Position Data'
    _decode_struct = struct.Struct('<BHiqqqBBBhhiB')
    _decode_struct_size = _decode_struct.size
    __slots__ = ('_system_id', '_date', '_time', '_latitude', '_longitude', '_altitude', '_method', '_GNSS_type', '_integrity', '_number_of_sv', '_HDOP', '_PDOP', '_geoidal_separation', '_nb_ref_stations', '_ref_stations')

    @classmethod
    def size(cls) -> int:
        return cls._decode_struct_size

    _GNSS_type_enum = 'GNSS type'
    _integrity_enum = {
        0: 'No integrity checking',
        1: 'Safe',
        2: 'Caution'
        }


    def __init__(self, message=None, protobuf=None):
        super().__init__(message, protobuf)

    @property
    def pgn(self) -> int:
        return self._pgn

    @property
    def name(self) -> str:
        return self._name

    @property
    def system_id(self) -> int:
        return self._system_id

    @property
    def date(self) -> int:
        return self._date

    @property
    def time(self) -> float:
        return self._time

    @property
    def latitude(self) -> float:
        return self._latitude

    @property
    def longitude(self) -> float:
        return self._longitude

    @property
    def altitude(self) -> float:
        return self._altitude

    @property
    def method(self) -> int:
        return self._method

    @property
    def GNSS_type(self) -> int:
        return self._GNSS_type

    @property
    def integrity(self) -> int:
        return self._integrity

    @property
    def number_of_sv(self) -> int:
        return self._number_of_sv

    @property
    def HDOP(self) -> float:
        return self._HDOP

    @property
    def PDOP(self) -> float:
        return self._PDOP

    @property
    def geoidal_separation(self) -> float:
        return self._geoidal_separation

    @property
    def nb_ref_stations(self) -> int:
        return self._nb_ref_stations

    @property
    def ref_stations(self) -> list:
        return self._ref_stations

    @system_id.setter
    def system_id(self, value: int):
        self._system_id = value

    @date.setter
    def date(self, value: int):
        self._date = value

    @time.setter
    def time(self, value: float):
        self._time = value

    @latitude.setter
    def latitude(self, value: float):
        self._latitude = value

    @longitude.setter
    def longitude(self, value: float):
        self._longitude = value

    @altitude.setter
    def altitude(self, value: float):
        self._altitude = value

    @method.setter
    def method(self, value: int):
        self._method = value

    @GNSS_type.setter
    def GNSS_type(self, value: int):
        self._GNSS_type = value

    @integrity.setter
    def integrity(self, value: int):
        self._integrity = value

    @number_of_sv.setter
    def number_of_sv(self, value: int):
        self._number_of_sv = value

    @HDOP.setter
    def HDOP(self, value: float):
        self._HDOP = value

    @PDOP.setter
    def PDOP(self, value: float):
        self._PDOP = value

    @geoidal_separation.setter
    def geoidal_separation(self, value: float):
        self._geoidal_separation = value

    @nb_ref_stations.setter
    def nb_ref_stations(self, value: int):
        self._nb_ref_stations = value

    @ref_stations.setter
    def ref_stations(self, value: list):
        self._ref_stations = value

    @property
    def GNSS_type_text(self) -> str:
        return NMEA2000Payload.resolve_global_enum(self._GNSS_type_enum, self._GNSS_type)

    @property
    def integrity_text(self) -> str:
        return self._integrity_enum.get(self._integrity, 'integrity key error')

    def decode_payload_segment(self, payload, from_byte):
        val = self._decode_struct.unpack_from(payload, from_byte)
        self._system_id = val[0]
        self._date = val[1]
        self._time = val[2] * 0.0001
        self._latitude = val[3] * 1e-16
        self._longitude = val[4] * 1e-16
        self._altitude = val[5] * 1e-06
        self._method = val[6] & 0xF
        self._GNSS_type = (val[6] << 4) & 0xF
        self._integrity = val[7] & 0x3
        self._number_of_sv = val[8]
        self._HDOP = val[9] * 0.01
        self._PDOP = val[10] * 0.01
        self._geoidal_separation = val[11] * 0.01
        self._nb_ref_stations = check_valid(val[12], 255, 0)
        start_byte = self._decode_struct_size
        self._ref_stations = []
        for i in range(0, self.nb_ref_stations):
            self._ref_stations.append(self.Ref_StationsClass().decode_payload_segment(payload, start_byte))
            start_byte += self.Ref_StationsClass.size()

    def encode_payload_segment(self, from_byte):
        buf_size = self.__class__.size() + (self.nb_ref_stations * self.Ref_StationsClass.size())
        buffer = bytearray(buf_size)
        v0 = int(self._time / 0.0001)
        v1 = int(self._latitude / 1e-16)
        v2 = int(self._longitude / 1e-16)
        v3 = int(self._altitude / 1e-06)
        v4 = int(self._HDOP / 0.01)
        v5 = int(self._PDOP / 0.01)
        v6 = int(self._geoidal_separation / 0.01)
        self._decode_struct.pack_into(buffer, from_byte, self._system_id, self._date, v0, v1, v2, v3, self._method, self._GNSS_type, self._integrity, self._number_of_sv, v4, v5, v6, self._nb_ref_stations)

    def from_protobuf(self, message: Pgn129029ClassPb):
        self._system_id = message.system_id
        self._date = message.date
        self._time = message.time
        self._latitude = message.latitude
        self._longitude = message.longitude
        self._altitude = message.altitude
        self._method = message.method
        self._GNSS_type = message.GNSS_type
        self._integrity = message.integrity
        self._number_of_sv = message.number_of_sv
        self._HDOP = message.HDOP
        self._PDOP = message.PDOP
        self._geoidal_separation = message.geoidal_separation
        self._nb_ref_stations = message.nb_ref_stations
        self._ref_stations = []
        for sub_set in message.ref_stations:
            self._ref_stations.append(self.Ref_StationsClass(protobuf=sub_set))

    def as_protobuf(self) -> Pgn129029ClassPb:
        message = Pgn129029ClassPb()
        message.system_id = self._system_id
        message.date = self._date
        message.time = self._time
        message.latitude = self._latitude
        message.longitude = self._longitude
        message.altitude = self._altitude
        message.method = self._method
        message.GNSS_type = self._GNSS_type
        message.integrity = self._integrity
        message.number_of_sv = self._number_of_sv
        message.HDOP = self._HDOP
        message.PDOP = self._PDOP
        message.geoidal_separation = self._geoidal_separation
        message.nb_ref_stations = self._nb_ref_stations
        for sub_set in self._ref_stations:
            message.ref_stations.append(sub_set.as_protobuf())
        return message

    def __str__(self):
        return f'PGN{self._pgn}({self._name}) [system_id={self._system_id}, date={self._date}, time={self._time}, latitude={self._latitude}, longitude={self._longitude}, altitude={self._altitude}, method={self._method}, GNSS_type={self._GNSS_type}, integrity={self._integrity}, number_of_sv={self._number_of_sv}, HDOP={self._HDOP}, PDOP={self._PDOP}, geoidal_separation={self._geoidal_separation}, nb_ref_stations={self._nb_ref_stations}, ref_stations={self._ref_stations}]'


class Pgn130312Class(NMEA2000Payload):

    _pgn = 130312
    _name = 'Temperature'
    _decode_struct = struct.Struct('<BBBhhB')
    _decode_struct_size = _decode_struct.size
    __slots__ = ('_system_id', '_temperature_instance', '_temperature_source', '_actual_temperature', '_set_temperature')

    @classmethod
    def size(cls) -> int:
        return cls._decode_struct_size

    _temperature_source_enum = 'Temperature Source'


    def __init__(self, message=None, protobuf=None):
        super().__init__(message, protobuf)

    @property
    def pgn(self) -> int:
        return self._pgn

    @property
    def name(self) -> str:
        return self._name

    @property
    def system_id(self) -> int:
        return self._system_id

    @property
    def temperature_instance(self) -> int:
        return self._temperature_instance

    @property
    def temperature_source(self) -> int:
        return self._temperature_source

    @property
    def actual_temperature(self) -> float:
        return self._actual_temperature

    @property
    def set_temperature(self) -> float:
        return self._set_temperature

    @system_id.setter
    def system_id(self, value: int):
        self._system_id = value

    @temperature_instance.setter
    def temperature_instance(self, value: int):
        self._temperature_instance = value

    @temperature_source.setter
    def temperature_source(self, value: int):
        self._temperature_source = value

    @actual_temperature.setter
    def actual_temperature(self, value: float):
        self._actual_temperature = value

    @set_temperature.setter
    def set_temperature(self, value: float):
        self._set_temperature = value

    @property
    def temperature_source_text(self) -> str:
        return NMEA2000Payload.resolve_global_enum(self._temperature_source_enum, self._temperature_source)

    def decode_payload_segment(self, payload, from_byte):
        val = self._decode_struct.unpack_from(payload, from_byte)
        self._system_id = val[0]
        self._temperature_instance = val[1]
        self._temperature_source = val[2]
        self._actual_temperature = val[3] * 0.01 + -273.15
        self._set_temperature = val[4] * 0.01 + -273.15

    def encode_payload_segment(self, from_byte):
        buf_size = self.__class__.size()
        buffer = bytearray(buf_size)
        v0 = int((self._actual_temperature - -273.15) / 0.01)
        v1 = int((self._set_temperature - -273.15) / 0.01)
        self._decode_struct.pack_into(buffer, from_byte, self._system_id, self._temperature_instance, self._temperature_source, v0)

    def from_protobuf(self, message: Pgn130312ClassPb):
        self._system_id = message.system_id
        self._temperature_instance = message.temperature_instance
        self._temperature_source = message.temperature_source
        self._actual_temperature = message.actual_temperature
        self._set_temperature = message.set_temperature

    def as_protobuf(self) -> Pgn130312ClassPb:
        message = Pgn130312ClassPb()
        message.system_id = self._system_id
        message.temperature_instance = self._temperature_instance
        message.temperature_source = self._temperature_source
        message.actual_temperature = self._actual_temperature
        message.set_temperature = self._set_temperature
        return message

    def __str__(self):
        return f'PGN{self._pgn}({self._name}) [system_id={self._system_id}, temperature_instance={self._temperature_instance}, temperature_source={self._temperature_source}, actual_temperature={self._actual_temperature}, set_temperature={self._set_temperature}]'


#####################################################################
#         Messages implementation classes
#####################################################################

class Pgn126992Message(NMEA2000DecodedMsg, Pgn126992Class):

    def __init__(self, message: NMEA2000Msg = None, protobuf: nmea2000_decoded_pb = None):
        if message is not None:
            assert (message.pgn == self.pgn)
            super().__init__(message=message)
            self.decode_payload(message.payload)
        elif protobuf is not None:
            assert (protobuf.pgn == self.pgn)
            super().__init__(protobuf=protobuf)
            self.unpack_payload(protobuf, Pgn126992ClassPb())


class Pgn126993Message(NMEA2000DecodedMsg, Pgn126993Class):

    def __init__(self, message: NMEA2000Msg = None, protobuf: nmea2000_decoded_pb = None):
        if message is not None:
            assert (message.pgn == self.pgn)
            super().__init__(message=message)
            self.decode_payload(message.payload)
        elif protobuf is not None:
            assert (protobuf.pgn == self.pgn)
            super().__init__(protobuf=protobuf)
            self.unpack_payload(protobuf, Pgn126993ClassPb())


class Pgn129025Message(NMEA2000DecodedMsg, Pgn129025Class):

    def __init__(self, message: NMEA2000Msg = None, protobuf: nmea2000_decoded_pb = None):
        if message is not None:
            assert (message.pgn == self.pgn)
            super().__init__(message=message)
            self.decode_payload(message.payload)
        elif protobuf is not None:
            assert (protobuf.pgn == self.pgn)
            super().__init__(protobuf=protobuf)
            self.unpack_payload(protobuf, Pgn129025ClassPb())


class Pgn129026Message(NMEA2000DecodedMsg, Pgn129026Class):

    def __init__(self, message: NMEA2000Msg = None, protobuf: nmea2000_decoded_pb = None):
        if message is not None:
            assert (message.pgn == self.pgn)
            super().__init__(message=message)
            self.decode_payload(message.payload)
        elif protobuf is not None:
            assert (protobuf.pgn == self.pgn)
            super().__init__(protobuf=protobuf)
            self.unpack_payload(protobuf, Pgn129026ClassPb())


class Pgn129029Message(NMEA2000DecodedMsg, Pgn129029Class):

    def __init__(self, message: NMEA2000Msg = None, protobuf: nmea2000_decoded_pb = None):
        if message is not None:
            assert (message.pgn == self.pgn)
            super().__init__(message=message)
            self.decode_payload(message.payload)
        elif protobuf is not None:
            assert (protobuf.pgn == self.pgn)
            super().__init__(protobuf=protobuf)
            self.unpack_payload(protobuf, Pgn129029ClassPb())


class Pgn130312Message(NMEA2000DecodedMsg, Pgn130312Class):

    def __init__(self, message: NMEA2000Msg = None, protobuf: nmea2000_decoded_pb = None):
        if message is not None:
            assert (message.pgn == self.pgn)
            super().__init__(message=message)
            self.decode_payload(message.payload)
        elif protobuf is not None:
            assert (protobuf.pgn == self.pgn)
            super().__init__(protobuf=protobuf)
            self.unpack_payload(protobuf, Pgn130312ClassPb())


#####################################################################
#         Generated class dictionary
#####################################################################
nmea2k_generated_classes = {
        126992: Pgn126992Message,
        126993: Pgn126993Message,
        129025: Pgn129025Message,
        129026: Pgn129026Message,
        129029: Pgn129029Message,
        130312: Pgn130312Message
        }
# end of generated file
