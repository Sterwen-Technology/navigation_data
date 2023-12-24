# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nmea2000_classes_gen.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1anmea2000_classes_gen.proto\"[\n\x16Pgn65359Mfg1851ClassPb\x12\x11\n\tsystem_id\x18\x01 \x01(\r\x12\x14\n\x0ctrue_heading\x18\x02 \x01(\x02\x12\x18\n\x10magnetic_heading\x18\x03 \x01(\x02\"j\n\x16Pgn65379Mfg1851ClassPb\x12\x11\n\tsystem_id\x18\x01 \x01(\r\x12\x12\n\npilot_mode\x18\x02 \x01(\r\x12\x10\n\x08sub_mode\x18\x03 \x01(\r\x12\x17\n\x0fpilot_mode_data\x18\x04 \x01(\r\"Q\n\x10Pgn126992ClassPb\x12\x11\n\tsystem_id\x18\x01 \x01(\r\x12\x0e\n\x06source\x18\x02 \x01(\r\x12\x0c\n\x04\x64\x61te\x18\x03 \x01(\r\x12\x0c\n\x04time\x18\x04 \x01(\x02\"4\n\x10Pgn126993ClassPb\x12\x10\n\x08interval\x18\x01 \x01(\x02\x12\x0e\n\x06status\x18\x02 \x01(\r\"\xd7\x01\n\x10Pgn126996ClassPb\x12\x18\n\x10nmea2000_version\x18\x01 \x01(\r\x12\x14\n\x0cproduct_code\x18\x02 \x01(\r\x12\x10\n\x08model_id\x18\x03 \x01(\t\x12\x18\n\x10software_version\x18\x04 \x01(\t\x12\x15\n\rmodel_version\x18\x05 \x01(\t\x12\x19\n\x11model_serial_code\x18\x06 \x01(\t\x12\x1b\n\x13\x63\x65rtification_level\x18\x07 \x01(\r\x12\x18\n\x10load_equivalency\x18\x08 \x01(\r\"]\n\x10Pgn126998ClassPb\x12\x16\n\x0einstallation_1\x18\x01 \x01(\t\x12\x16\n\x0einstallation_2\x18\x02 \x01(\t\x12\x19\n\x11manufacturer_info\x18\x03 \x01(\t\"X\n\x10Pgn127245ClassPb\x12\x10\n\x08instance\x18\x01 \x01(\r\x12\x11\n\tdirection\x18\x02 \x01(\r\x12\r\n\x05\x61ngle\x18\x03 \x01(\x02\x12\x10\n\x08position\x18\x04 \x01(\x02\"o\n\x10Pgn127250ClassPb\x12\x11\n\tsystem_id\x18\x01 \x01(\r\x12\x0f\n\x07heading\x18\x02 \x01(\x02\x12\x11\n\tdeviation\x18\x03 \x01(\x02\x12\x11\n\tvariation\x18\x04 \x01(\x02\x12\x11\n\treference\x18\x05 \x01(\r\"`\n\x10Pgn127258ClassPb\x12\x11\n\tsystem_id\x18\x01 \x01(\r\x12\x0e\n\x06source\x18\x02 \x01(\r\x12\x16\n\x0e\x61ge_of_service\x18\x03 \x01(\r\x12\x11\n\tvariation\x18\x04 \x01(\x02\"A\n\x10Pgn127488ClassPb\x12\x17\n\x0f\x65ngine_instance\x18\x01 \x01(\r\x12\x14\n\x0c\x65ngine_speed\x18\x02 \x01(\x02\"\xba\x01\n\x10Pgn127489ClassPb\x12\x17\n\x0f\x65ngine_instance\x18\x01 \x01(\r\x12\x14\n\x0coil_pressure\x18\x02 \x01(\x02\x12\x17\n\x0foil_temperature\x18\x03 \x01(\x02\x12\x13\n\x0btemperature\x18\x04 \x01(\x02\x12\x1a\n\x12\x61lternator_voltage\x18\x05 \x01(\x02\x12\x11\n\tfuel_rate\x18\x06 \x01(\x02\x12\x1a\n\x12total_engine_hours\x18\x07 \x01(\x02\"v\n\x10Pgn127508ClassPb\x12\x18\n\x10\x62\x61ttery_instance\x18\x01 \x01(\r\x12\x0f\n\x07voltage\x18\x02 \x01(\x02\x12\x0f\n\x07\x63urrent\x18\x03 \x01(\x02\x12\x13\n\x0btemperature\x18\x04 \x01(\x02\x12\x11\n\tsystem_id\x18\x05 \x01(\r\"\x88\x01\n\x10Pgn128259ClassPb\x12\x11\n\tsystem_id\x18\x01 \x01(\r\x12\x1b\n\x13speed_through_water\x18\x02 \x01(\x02\x12\x1d\n\x15speed_over_ground_ref\x18\x03 \x01(\x02\x12%\n\x1dspeed_through_water_reference\x18\x04 \x01(\r\"S\n\x10Pgn128267ClassPb\x12\x11\n\tsystem_id\x18\x01 \x01(\r\x12\r\n\x05\x64\x65pth\x18\x02 \x01(\x02\x12\x0e\n\x06offset\x18\x03 \x01(\x02\x12\r\n\x05range\x18\x04 \x01(\x02\"7\n\x10Pgn129025ClassPb\x12\x10\n\x08latitude\x18\x01 \x01(\x02\x12\x11\n\tlongitude\x18\x02 \x01(\x02\"V\n\x10Pgn129026ClassPb\x12\x11\n\tsystem_id\x18\x01 \x01(\r\x12\x15\n\rCOG_reference\x18\x02 \x01(\r\x12\x0b\n\x03\x43OG\x18\x03 \x01(\x02\x12\x0b\n\x03SOG\x18\x04 \x01(\x02\"\xae\x03\n\x10Pgn129029ClassPb\x12\x11\n\tsystem_id\x18\x01 \x01(\r\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\r\x12\x0c\n\x04time\x18\x03 \x01(\x02\x12\x10\n\x08latitude\x18\x04 \x01(\x01\x12\x11\n\tlongitude\x18\x05 \x01(\x01\x12\x10\n\x08\x61ltitude\x18\x06 \x01(\x01\x12\x0e\n\x06method\x18\x07 \x01(\r\x12\x11\n\tGNSS_type\x18\x08 \x01(\r\x12\x11\n\tintegrity\x18\t \x01(\r\x12\x14\n\x0cnumber_of_sv\x18\n \x01(\r\x12\x0c\n\x04HDOP\x18\x0b \x01(\x02\x12\x0c\n\x04PDOP\x18\x0c \x01(\x02\x12\x1a\n\x12geoidal_separation\x18\r \x01(\x02\x12\x17\n\x0fnb_ref_stations\x18\x0e \x01(\r\x12;\n\x0cref_stations\x18\x0f \x03(\x0b\x32%.Pgn129029ClassPb.Ref_StationsClassPb\x1aZ\n\x13Ref_StationsClassPb\x12\x12\n\nstation_id\x18\x01 \x01(\r\x12\x11\n\tGNSS_type\x18\x02 \x01(\r\x12\x1c\n\x14\x61ge_DGNSS_correction\x18\x03 \x01(\x02\"\xc9\x02\n\x10Pgn129038ClassPb\x12\x12\n\nmessage_id\x18\x01 \x01(\r\x12\x18\n\x10repeat_indicator\x18\x02 \x01(\r\x12\x0c\n\x04mmsi\x18\x03 \x01(\x05\x12\x11\n\tlongitude\x18\x04 \x01(\x02\x12\x10\n\x08latitude\x18\x05 \x01(\x02\x12\x19\n\x11position_accuracy\x18\x06 \x01(\r\x12\x0c\n\x04RAIM\x18\x07 \x01(\r\x12\x11\n\ttimestamp\x18\x08 \x01(\r\x12\x0b\n\x03\x43OG\x18\t \x01(\x02\x12\x0b\n\x03SOG\x18\n \x01(\x02\x12\x1b\n\x13\x63ommunication_state\x18\x0b \x01(\r\x12\x1f\n\x17transceiver_information\x18\x0c \x01(\r\x12\x0f\n\x07heading\x18\r \x01(\x02\x12\x14\n\x0crate_of_turn\x18\x0e \x01(\x02\x12\x19\n\x11navigation_status\x18\x0f \x01(\r\"\xfb\x02\n\x10Pgn129039ClassPb\x12\x12\n\nmessage_id\x18\x01 \x01(\r\x12\x18\n\x10repeat_indicator\x18\x02 \x01(\r\x12\x0c\n\x04mmsi\x18\x03 \x01(\x05\x12\x11\n\tlongitude\x18\x04 \x01(\x02\x12\x10\n\x08latitude\x18\x05 \x01(\x02\x12\x19\n\x11position_accuracy\x18\x06 \x01(\r\x12\x0c\n\x04RAIM\x18\x07 \x01(\r\x12\x11\n\ttimestamp\x18\x08 \x01(\r\x12\x0b\n\x03\x43OG\x18\t \x01(\x02\x12\x0b\n\x03SOG\x18\n \x01(\x02\x12\x1b\n\x13\x63ommunication_state\x18\x0b \x01(\r\x12\x18\n\x10transceiver_info\x18\x0c \x01(\r\x12\x0f\n\x07heading\x18\r \x01(\x02\x12\x11\n\tunit_type\x18\x0e \x01(\r\x12\x0c\n\x04\x62\x61nd\x18\x0f \x01(\r\x12\x14\n\x0chandle_msg22\x18\x10 \x01(\r\x12\x10\n\x08\x41IS_mode\x18\x11 \x01(\r\x12\x1f\n\x17\x41IS_communication_state\x18\x12 \x01(\r\"c\n\x10Pgn129283ClassPb\x12\x11\n\tsystem_id\x18\x01 \x01(\r\x12\x1d\n\x15navigation_terminated\x18\x02 \x01(\r\x12\x10\n\x08XTE_mode\x18\x03 \x01(\r\x12\x0b\n\x03XTE\x18\x04 \x01(\x02\"\xac\x03\n\x10Pgn129284ClassPb\x12\x11\n\tsystem_id\x18\x01 \x01(\r\x12\x1c\n\x14\x64istance_to_waypoint\x18\x02 \x01(\x02\x12\x19\n\x11\x62\x65\x61ring_reference\x18\x03 \x01(\r\x12\x1d\n\x15perpendicular_crossed\x18\x04 \x01(\r\x12\x1e\n\x16\x61rrival_circle_entered\x18\x05 \x01(\r\x12\x18\n\x10\x63\x61lculation_type\x18\x06 \x01(\r\x12\x10\n\x08\x45TA_time\x18\x07 \x01(\x02\x12\x10\n\x08\x45TA_date\x18\x08 \x01(\r\x12%\n\x1d\x62\x65\x61ring_origin_to_destination\x18\t \x01(\x02\x12\'\n\x1f\x62\x65\x61ring_position_to_destination\x18\n \x01(\x02\x12\x17\n\x0forigin_waypoint\x18\x0b \x01(\r\x12\x1c\n\x14\x64\x65stination_waypoint\x18\x0c \x01(\r\x12\x1c\n\x14\x64\x65stination_latitude\x18\r \x01(\x02\x12\x1d\n\x15\x64\x65stination_longitude\x18\x0e \x01(\x02\x12\x0b\n\x03WCV\x18\x0f \x01(\x02\"\xec\x02\n\x10Pgn129285ClassPb\x12\x14\n\x0cstart_rps_nb\x18\x01 \x01(\r\x12\x10\n\x08nb_items\x18\x02 \x01(\r\x12\x13\n\x0b\x64\x61tabase_id\x18\x03 \x01(\r\x12\x10\n\x08route_id\x18\x04 \x01(\r\x12\x1a\n\x12supplementary_data\x18\x05 \x01(\r\x12\x1c\n\x14navigation_direction\x18\x06 \x01(\r\x12\x12\n\nroute_name\x18\x07 \x01(\t\x12?\n\x0eWP_definitions\x18\x08 \x03(\x0b\x32\'.Pgn129285ClassPb.Wp_DefinitionsClassPb\x1az\n\x15Wp_DefinitionsClassPb\x12\x13\n\x0bwaypoint_id\x18\x01 \x01(\r\x12\x15\n\rwaypoint_name\x18\x02 \x01(\t\x12\x19\n\x11waypoint_latitude\x18\x03 \x01(\x02\x12\x1a\n\x12waypoint_longitude\x18\x04 \x01(\x02\"z\n\x10Pgn129539ClassPb\x12\x11\n\tsystem_id\x18\x01 \x01(\r\x12\x14\n\x0c\x64\x65sired_mode\x18\x02 \x01(\r\x12\x13\n\x0b\x61\x63tual_mode\x18\x03 \x01(\r\x12\x0c\n\x04HDOP\x18\x04 \x01(\x02\x12\x0c\n\x04VDOP\x18\x05 \x01(\x02\x12\x0c\n\x04TDOP\x18\x06 \x01(\x02\"\xaa\x02\n\x10Pgn129540ClassPb\x12\x11\n\tsystem_id\x18\x01 \x01(\r\x12\x0c\n\x04mode\x18\x02 \x01(\r\x12\x14\n\x0csats_in_view\x18\x03 \x01(\r\x12\x41\n\x0fsatellites_data\x18\x04 \x03(\x0b\x32(.Pgn129540ClassPb.Satellites_DataClassPb\x1a\x9b\x01\n\x16Satellites_DataClassPb\x12\x18\n\x10satellite_number\x18\x01 \x01(\r\x12\x11\n\televation\x18\x02 \x01(\x02\x12\x0f\n\x07\x61zimuth\x18\x03 \x01(\x02\x12\x1a\n\x12signal_noise_ratio\x18\x04 \x01(\x02\x12\x17\n\x0frange_residuals\x18\x05 \x01(\r\x12\x0e\n\x06status\x18\x06 \x01(\r\"\x92\x03\n\x10Pgn129794ClassPb\x12\x12\n\nmessage_id\x18\x01 \x01(\r\x12\x18\n\x10repeat_indicator\x18\x02 \x01(\r\x12\x0c\n\x04mmsi\x18\x03 \x01(\x05\x12\x12\n\nIMO_number\x18\x04 \x01(\x05\x12\x10\n\x08\x63\x61llsign\x18\x05 \x01(\t\x12\x11\n\tship_name\x18\x06 \x01(\t\x12\x14\n\x0ctype_of_ship\x18\x07 \x01(\r\x12\x0e\n\x06length\x18\x08 \x01(\x02\x12\x0c\n\x04\x62\x65\x61m\x18\t \x01(\x02\x12\x1f\n\x17position_from_starboard\x18\n \x01(\x02\x12\x19\n\x11position_from_bow\x18\x0b \x01(\x02\x12\x10\n\x08\x45TA_date\x18\x0c \x01(\r\x12\x10\n\x08\x45TA_time\x18\r \x01(\x02\x12\r\n\x05\x64raft\x18\x0e \x01(\x02\x12\x13\n\x0b\x64\x65stination\x18\x0f \x01(\t\x12\x13\n\x0b\x41IS_version\x18\x10 \x01(\r\x12\x11\n\tGNSS_type\x18\x11 \x01(\r\x12\x0b\n\x03\x44TE\x18\x12 \x01(\r\x12\x1c\n\x14\x41IS_transceiver_info\x18\x13 \x01(\r\"a\n\x10Pgn129809ClassPb\x12\x12\n\nmessage_id\x18\x01 \x01(\r\x12\x18\n\x10repeat_indicator\x18\x02 \x01(\r\x12\x0c\n\x04mmsi\x18\x03 \x01(\x05\x12\x11\n\tship_name\x18\x04 \x01(\t\"\xfd\x01\n\x10Pgn129810ClassPb\x12\x12\n\nmessage_id\x18\x01 \x01(\r\x12\x18\n\x10repeat_indicator\x18\x02 \x01(\r\x12\x0c\n\x04mmsi\x18\x03 \x01(\x05\x12\x14\n\x0ctype_of_ship\x18\x04 \x01(\r\x12\x11\n\tvendor_id\x18\x05 \x01(\t\x12\x11\n\tcall_sign\x18\x06 \x01(\t\x12\x0e\n\x06length\x18\x07 \x01(\x02\x12\x0c\n\x04\x62\x65\x61m\x18\x08 \x01(\x02\x12\x1f\n\x17position_from_starboard\x18\t \x01(\x02\x12\x19\n\x11position_from_bow\x18\n \x01(\x02\x12\x17\n\x0fmothership_mmsi\x18\x0b \x01(\x05\"`\n\x10Pgn130306ClassPb\x12\x11\n\tsystem_id\x18\x01 \x01(\r\x12\x12\n\nwind_speed\x18\x02 \x01(\x02\x12\x12\n\nwind_angle\x18\x03 \x01(\x02\x12\x11\n\treference\x18\x04 \x01(\r\"\x7f\n\x10Pgn130310ClassPb\x12\x11\n\tsystem_id\x18\x01 \x01(\r\x12\x19\n\x11water_temperature\x18\x02 \x01(\x02\x12\x1f\n\x17outside_air_temperature\x18\x03 \x01(\x02\x12\x1c\n\x14\x61tmospheric_pressure\x18\x04 \x01(\x02\"\xa3\x01\n\x10Pgn130311ClassPb\x12\x11\n\tsystem_id\x18\x01 \x01(\r\x12\x1c\n\x14temperature_instance\x18\x02 \x01(\r\x12\x19\n\x11humidity_instance\x18\x03 \x01(\r\x12\x13\n\x0btemperature\x18\x04 \x01(\x02\x12\x10\n\x08humidity\x18\x05 \x01(\x02\x12\x1c\n\x14\x61tmospheric_pressure\x18\x06 \x01(\x02\"\x94\x01\n\x10Pgn130312ClassPb\x12\x11\n\tsystem_id\x18\x01 \x01(\r\x12\x1c\n\x14temperature_instance\x18\x02 \x01(\r\x12\x1a\n\x12temperature_source\x18\x03 \x01(\r\x12\x1a\n\x12\x61\x63tual_temperature\x18\x04 \x01(\x02\x12\x17\n\x0fset_temperature\x18\x05 \x01(\x02\"k\n\x10Pgn130314ClassPb\x12\x11\n\tsystem_id\x18\x01 \x01(\r\x12\x19\n\x11pressure_instance\x18\x02 \x01(\r\x12\x17\n\x0fpressure_source\x18\x03 \x01(\r\x12\x10\n\x08pressure\x18\x04 \x01(\x02\"\x94\x01\n\x10Pgn130316ClassPb\x12\x11\n\tsystem_id\x18\x01 \x01(\r\x12\x1c\n\x14temperature_instance\x18\x02 \x01(\r\x12\x1a\n\x12temperature_source\x18\x03 \x01(\r\x12\x1a\n\x12\x61\x63tual_temperature\x18\x04 \x01(\x02\x12\x17\n\x0fset_temperature\x18\x05 \x01(\x02\"\xcf\x01\n\x10Pgn130578ClassPb\x12 \n\x18longitudinal_speed_water\x18\x01 \x01(\x02\x12\x1e\n\x16transverse_speed_water\x18\x02 \x01(\x02\x12!\n\x19longitudinal_speed_ground\x18\x03 \x01(\x02\x12\x1f\n\x17transverse_speed_ground\x18\x04 \x01(\x02\x12\x19\n\x11stern_speed_water\x18\x05 \x01(\x02\x12\x1a\n\x12stern_speed_ground\x18\x06 \x01(\x02\"\xd0\x01\n\x17Pgn130842Mfg1857ClassPb\x12\x12\n\nmessage_id\x18\x01 \x01(\r\x12\x18\n\x10repeat_indicator\x18\x02 \x01(\r\x12\x0c\n\x04mmsi\x18\x03 \x01(\x05\x12\x14\n\x0ctype_of_ship\x18\x04 \x01(\r\x12\x11\n\tvendor_id\x18\x05 \x01(\t\x12\x11\n\tcall_sign\x18\x06 \x01(\t\x12\x0e\n\x06length\x18\x07 \x01(\x02\x12\x0c\n\x04\x62\x65\x61m\x18\x08 \x01(\x02\x12\x1f\n\x17position_from_starboard\x18\t \x01(\x02\x62\x06proto3')



_PGN65359MFG1851CLASSPB = DESCRIPTOR.message_types_by_name['Pgn65359Mfg1851ClassPb']
_PGN65379MFG1851CLASSPB = DESCRIPTOR.message_types_by_name['Pgn65379Mfg1851ClassPb']
_PGN126992CLASSPB = DESCRIPTOR.message_types_by_name['Pgn126992ClassPb']
_PGN126993CLASSPB = DESCRIPTOR.message_types_by_name['Pgn126993ClassPb']
_PGN126996CLASSPB = DESCRIPTOR.message_types_by_name['Pgn126996ClassPb']
_PGN126998CLASSPB = DESCRIPTOR.message_types_by_name['Pgn126998ClassPb']
_PGN127245CLASSPB = DESCRIPTOR.message_types_by_name['Pgn127245ClassPb']
_PGN127250CLASSPB = DESCRIPTOR.message_types_by_name['Pgn127250ClassPb']
_PGN127258CLASSPB = DESCRIPTOR.message_types_by_name['Pgn127258ClassPb']
_PGN127488CLASSPB = DESCRIPTOR.message_types_by_name['Pgn127488ClassPb']
_PGN127489CLASSPB = DESCRIPTOR.message_types_by_name['Pgn127489ClassPb']
_PGN127508CLASSPB = DESCRIPTOR.message_types_by_name['Pgn127508ClassPb']
_PGN128259CLASSPB = DESCRIPTOR.message_types_by_name['Pgn128259ClassPb']
_PGN128267CLASSPB = DESCRIPTOR.message_types_by_name['Pgn128267ClassPb']
_PGN129025CLASSPB = DESCRIPTOR.message_types_by_name['Pgn129025ClassPb']
_PGN129026CLASSPB = DESCRIPTOR.message_types_by_name['Pgn129026ClassPb']
_PGN129029CLASSPB = DESCRIPTOR.message_types_by_name['Pgn129029ClassPb']
_PGN129029CLASSPB_REF_STATIONSCLASSPB = _PGN129029CLASSPB.nested_types_by_name['Ref_StationsClassPb']
_PGN129038CLASSPB = DESCRIPTOR.message_types_by_name['Pgn129038ClassPb']
_PGN129039CLASSPB = DESCRIPTOR.message_types_by_name['Pgn129039ClassPb']
_PGN129283CLASSPB = DESCRIPTOR.message_types_by_name['Pgn129283ClassPb']
_PGN129284CLASSPB = DESCRIPTOR.message_types_by_name['Pgn129284ClassPb']
_PGN129285CLASSPB = DESCRIPTOR.message_types_by_name['Pgn129285ClassPb']
_PGN129285CLASSPB_WP_DEFINITIONSCLASSPB = _PGN129285CLASSPB.nested_types_by_name['Wp_DefinitionsClassPb']
_PGN129539CLASSPB = DESCRIPTOR.message_types_by_name['Pgn129539ClassPb']
_PGN129540CLASSPB = DESCRIPTOR.message_types_by_name['Pgn129540ClassPb']
_PGN129540CLASSPB_SATELLITES_DATACLASSPB = _PGN129540CLASSPB.nested_types_by_name['Satellites_DataClassPb']
_PGN129794CLASSPB = DESCRIPTOR.message_types_by_name['Pgn129794ClassPb']
_PGN129809CLASSPB = DESCRIPTOR.message_types_by_name['Pgn129809ClassPb']
_PGN129810CLASSPB = DESCRIPTOR.message_types_by_name['Pgn129810ClassPb']
_PGN130306CLASSPB = DESCRIPTOR.message_types_by_name['Pgn130306ClassPb']
_PGN130310CLASSPB = DESCRIPTOR.message_types_by_name['Pgn130310ClassPb']
_PGN130311CLASSPB = DESCRIPTOR.message_types_by_name['Pgn130311ClassPb']
_PGN130312CLASSPB = DESCRIPTOR.message_types_by_name['Pgn130312ClassPb']
_PGN130314CLASSPB = DESCRIPTOR.message_types_by_name['Pgn130314ClassPb']
_PGN130316CLASSPB = DESCRIPTOR.message_types_by_name['Pgn130316ClassPb']
_PGN130578CLASSPB = DESCRIPTOR.message_types_by_name['Pgn130578ClassPb']
_PGN130842MFG1857CLASSPB = DESCRIPTOR.message_types_by_name['Pgn130842Mfg1857ClassPb']
Pgn65359Mfg1851ClassPb = _reflection.GeneratedProtocolMessageType('Pgn65359Mfg1851ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN65359MFG1851CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn65359Mfg1851ClassPb)
  })
_sym_db.RegisterMessage(Pgn65359Mfg1851ClassPb)

Pgn65379Mfg1851ClassPb = _reflection.GeneratedProtocolMessageType('Pgn65379Mfg1851ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN65379MFG1851CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn65379Mfg1851ClassPb)
  })
_sym_db.RegisterMessage(Pgn65379Mfg1851ClassPb)

Pgn126992ClassPb = _reflection.GeneratedProtocolMessageType('Pgn126992ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN126992CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn126992ClassPb)
  })
_sym_db.RegisterMessage(Pgn126992ClassPb)

Pgn126993ClassPb = _reflection.GeneratedProtocolMessageType('Pgn126993ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN126993CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn126993ClassPb)
  })
_sym_db.RegisterMessage(Pgn126993ClassPb)

Pgn126996ClassPb = _reflection.GeneratedProtocolMessageType('Pgn126996ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN126996CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn126996ClassPb)
  })
_sym_db.RegisterMessage(Pgn126996ClassPb)

Pgn126998ClassPb = _reflection.GeneratedProtocolMessageType('Pgn126998ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN126998CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn126998ClassPb)
  })
_sym_db.RegisterMessage(Pgn126998ClassPb)

Pgn127245ClassPb = _reflection.GeneratedProtocolMessageType('Pgn127245ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN127245CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn127245ClassPb)
  })
_sym_db.RegisterMessage(Pgn127245ClassPb)

Pgn127250ClassPb = _reflection.GeneratedProtocolMessageType('Pgn127250ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN127250CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn127250ClassPb)
  })
_sym_db.RegisterMessage(Pgn127250ClassPb)

Pgn127258ClassPb = _reflection.GeneratedProtocolMessageType('Pgn127258ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN127258CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn127258ClassPb)
  })
_sym_db.RegisterMessage(Pgn127258ClassPb)

Pgn127488ClassPb = _reflection.GeneratedProtocolMessageType('Pgn127488ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN127488CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn127488ClassPb)
  })
_sym_db.RegisterMessage(Pgn127488ClassPb)

Pgn127489ClassPb = _reflection.GeneratedProtocolMessageType('Pgn127489ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN127489CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn127489ClassPb)
  })
_sym_db.RegisterMessage(Pgn127489ClassPb)

Pgn127508ClassPb = _reflection.GeneratedProtocolMessageType('Pgn127508ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN127508CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn127508ClassPb)
  })
_sym_db.RegisterMessage(Pgn127508ClassPb)

Pgn128259ClassPb = _reflection.GeneratedProtocolMessageType('Pgn128259ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN128259CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn128259ClassPb)
  })
_sym_db.RegisterMessage(Pgn128259ClassPb)

Pgn128267ClassPb = _reflection.GeneratedProtocolMessageType('Pgn128267ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN128267CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn128267ClassPb)
  })
_sym_db.RegisterMessage(Pgn128267ClassPb)

Pgn129025ClassPb = _reflection.GeneratedProtocolMessageType('Pgn129025ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN129025CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn129025ClassPb)
  })
_sym_db.RegisterMessage(Pgn129025ClassPb)

Pgn129026ClassPb = _reflection.GeneratedProtocolMessageType('Pgn129026ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN129026CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn129026ClassPb)
  })
_sym_db.RegisterMessage(Pgn129026ClassPb)

Pgn129029ClassPb = _reflection.GeneratedProtocolMessageType('Pgn129029ClassPb', (_message.Message,), {

  'Ref_StationsClassPb' : _reflection.GeneratedProtocolMessageType('Ref_StationsClassPb', (_message.Message,), {
    'DESCRIPTOR' : _PGN129029CLASSPB_REF_STATIONSCLASSPB,
    '__module__' : 'nmea2000_classes_gen_pb2'
    # @@protoc_insertion_point(class_scope:Pgn129029ClassPb.Ref_StationsClassPb)
    })
  ,
  'DESCRIPTOR' : _PGN129029CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn129029ClassPb)
  })
_sym_db.RegisterMessage(Pgn129029ClassPb)
_sym_db.RegisterMessage(Pgn129029ClassPb.Ref_StationsClassPb)

Pgn129038ClassPb = _reflection.GeneratedProtocolMessageType('Pgn129038ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN129038CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn129038ClassPb)
  })
_sym_db.RegisterMessage(Pgn129038ClassPb)

Pgn129039ClassPb = _reflection.GeneratedProtocolMessageType('Pgn129039ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN129039CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn129039ClassPb)
  })
_sym_db.RegisterMessage(Pgn129039ClassPb)

Pgn129283ClassPb = _reflection.GeneratedProtocolMessageType('Pgn129283ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN129283CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn129283ClassPb)
  })
_sym_db.RegisterMessage(Pgn129283ClassPb)

Pgn129284ClassPb = _reflection.GeneratedProtocolMessageType('Pgn129284ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN129284CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn129284ClassPb)
  })
_sym_db.RegisterMessage(Pgn129284ClassPb)

Pgn129285ClassPb = _reflection.GeneratedProtocolMessageType('Pgn129285ClassPb', (_message.Message,), {

  'Wp_DefinitionsClassPb' : _reflection.GeneratedProtocolMessageType('Wp_DefinitionsClassPb', (_message.Message,), {
    'DESCRIPTOR' : _PGN129285CLASSPB_WP_DEFINITIONSCLASSPB,
    '__module__' : 'nmea2000_classes_gen_pb2'
    # @@protoc_insertion_point(class_scope:Pgn129285ClassPb.Wp_DefinitionsClassPb)
    })
  ,
  'DESCRIPTOR' : _PGN129285CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn129285ClassPb)
  })
_sym_db.RegisterMessage(Pgn129285ClassPb)
_sym_db.RegisterMessage(Pgn129285ClassPb.Wp_DefinitionsClassPb)

Pgn129539ClassPb = _reflection.GeneratedProtocolMessageType('Pgn129539ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN129539CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn129539ClassPb)
  })
_sym_db.RegisterMessage(Pgn129539ClassPb)

Pgn129540ClassPb = _reflection.GeneratedProtocolMessageType('Pgn129540ClassPb', (_message.Message,), {

  'Satellites_DataClassPb' : _reflection.GeneratedProtocolMessageType('Satellites_DataClassPb', (_message.Message,), {
    'DESCRIPTOR' : _PGN129540CLASSPB_SATELLITES_DATACLASSPB,
    '__module__' : 'nmea2000_classes_gen_pb2'
    # @@protoc_insertion_point(class_scope:Pgn129540ClassPb.Satellites_DataClassPb)
    })
  ,
  'DESCRIPTOR' : _PGN129540CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn129540ClassPb)
  })
_sym_db.RegisterMessage(Pgn129540ClassPb)
_sym_db.RegisterMessage(Pgn129540ClassPb.Satellites_DataClassPb)

Pgn129794ClassPb = _reflection.GeneratedProtocolMessageType('Pgn129794ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN129794CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn129794ClassPb)
  })
_sym_db.RegisterMessage(Pgn129794ClassPb)

Pgn129809ClassPb = _reflection.GeneratedProtocolMessageType('Pgn129809ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN129809CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn129809ClassPb)
  })
_sym_db.RegisterMessage(Pgn129809ClassPb)

Pgn129810ClassPb = _reflection.GeneratedProtocolMessageType('Pgn129810ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN129810CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn129810ClassPb)
  })
_sym_db.RegisterMessage(Pgn129810ClassPb)

Pgn130306ClassPb = _reflection.GeneratedProtocolMessageType('Pgn130306ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN130306CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn130306ClassPb)
  })
_sym_db.RegisterMessage(Pgn130306ClassPb)

Pgn130310ClassPb = _reflection.GeneratedProtocolMessageType('Pgn130310ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN130310CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn130310ClassPb)
  })
_sym_db.RegisterMessage(Pgn130310ClassPb)

Pgn130311ClassPb = _reflection.GeneratedProtocolMessageType('Pgn130311ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN130311CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn130311ClassPb)
  })
_sym_db.RegisterMessage(Pgn130311ClassPb)

Pgn130312ClassPb = _reflection.GeneratedProtocolMessageType('Pgn130312ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN130312CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn130312ClassPb)
  })
_sym_db.RegisterMessage(Pgn130312ClassPb)

Pgn130314ClassPb = _reflection.GeneratedProtocolMessageType('Pgn130314ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN130314CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn130314ClassPb)
  })
_sym_db.RegisterMessage(Pgn130314ClassPb)

Pgn130316ClassPb = _reflection.GeneratedProtocolMessageType('Pgn130316ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN130316CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn130316ClassPb)
  })
_sym_db.RegisterMessage(Pgn130316ClassPb)

Pgn130578ClassPb = _reflection.GeneratedProtocolMessageType('Pgn130578ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN130578CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn130578ClassPb)
  })
_sym_db.RegisterMessage(Pgn130578ClassPb)

Pgn130842Mfg1857ClassPb = _reflection.GeneratedProtocolMessageType('Pgn130842Mfg1857ClassPb', (_message.Message,), {
  'DESCRIPTOR' : _PGN130842MFG1857CLASSPB,
  '__module__' : 'nmea2000_classes_gen_pb2'
  # @@protoc_insertion_point(class_scope:Pgn130842Mfg1857ClassPb)
  })
_sym_db.RegisterMessage(Pgn130842Mfg1857ClassPb)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PGN65359MFG1851CLASSPB._serialized_start=30
  _PGN65359MFG1851CLASSPB._serialized_end=121
  _PGN65379MFG1851CLASSPB._serialized_start=123
  _PGN65379MFG1851CLASSPB._serialized_end=229
  _PGN126992CLASSPB._serialized_start=231
  _PGN126992CLASSPB._serialized_end=312
  _PGN126993CLASSPB._serialized_start=314
  _PGN126993CLASSPB._serialized_end=366
  _PGN126996CLASSPB._serialized_start=369
  _PGN126996CLASSPB._serialized_end=584
  _PGN126998CLASSPB._serialized_start=586
  _PGN126998CLASSPB._serialized_end=679
  _PGN127245CLASSPB._serialized_start=681
  _PGN127245CLASSPB._serialized_end=769
  _PGN127250CLASSPB._serialized_start=771
  _PGN127250CLASSPB._serialized_end=882
  _PGN127258CLASSPB._serialized_start=884
  _PGN127258CLASSPB._serialized_end=980
  _PGN127488CLASSPB._serialized_start=982
  _PGN127488CLASSPB._serialized_end=1047
  _PGN127489CLASSPB._serialized_start=1050
  _PGN127489CLASSPB._serialized_end=1236
  _PGN127508CLASSPB._serialized_start=1238
  _PGN127508CLASSPB._serialized_end=1356
  _PGN128259CLASSPB._serialized_start=1359
  _PGN128259CLASSPB._serialized_end=1495
  _PGN128267CLASSPB._serialized_start=1497
  _PGN128267CLASSPB._serialized_end=1580
  _PGN129025CLASSPB._serialized_start=1582
  _PGN129025CLASSPB._serialized_end=1637
  _PGN129026CLASSPB._serialized_start=1639
  _PGN129026CLASSPB._serialized_end=1725
  _PGN129029CLASSPB._serialized_start=1728
  _PGN129029CLASSPB._serialized_end=2158
  _PGN129029CLASSPB_REF_STATIONSCLASSPB._serialized_start=2068
  _PGN129029CLASSPB_REF_STATIONSCLASSPB._serialized_end=2158
  _PGN129038CLASSPB._serialized_start=2161
  _PGN129038CLASSPB._serialized_end=2490
  _PGN129039CLASSPB._serialized_start=2493
  _PGN129039CLASSPB._serialized_end=2872
  _PGN129283CLASSPB._serialized_start=2874
  _PGN129283CLASSPB._serialized_end=2973
  _PGN129284CLASSPB._serialized_start=2976
  _PGN129284CLASSPB._serialized_end=3404
  _PGN129285CLASSPB._serialized_start=3407
  _PGN129285CLASSPB._serialized_end=3771
  _PGN129285CLASSPB_WP_DEFINITIONSCLASSPB._serialized_start=3649
  _PGN129285CLASSPB_WP_DEFINITIONSCLASSPB._serialized_end=3771
  _PGN129539CLASSPB._serialized_start=3773
  _PGN129539CLASSPB._serialized_end=3895
  _PGN129540CLASSPB._serialized_start=3898
  _PGN129540CLASSPB._serialized_end=4196
  _PGN129540CLASSPB_SATELLITES_DATACLASSPB._serialized_start=4041
  _PGN129540CLASSPB_SATELLITES_DATACLASSPB._serialized_end=4196
  _PGN129794CLASSPB._serialized_start=4199
  _PGN129794CLASSPB._serialized_end=4601
  _PGN129809CLASSPB._serialized_start=4603
  _PGN129809CLASSPB._serialized_end=4700
  _PGN129810CLASSPB._serialized_start=4703
  _PGN129810CLASSPB._serialized_end=4956
  _PGN130306CLASSPB._serialized_start=4958
  _PGN130306CLASSPB._serialized_end=5054
  _PGN130310CLASSPB._serialized_start=5056
  _PGN130310CLASSPB._serialized_end=5183
  _PGN130311CLASSPB._serialized_start=5186
  _PGN130311CLASSPB._serialized_end=5349
  _PGN130312CLASSPB._serialized_start=5352
  _PGN130312CLASSPB._serialized_end=5500
  _PGN130314CLASSPB._serialized_start=5502
  _PGN130314CLASSPB._serialized_end=5609
  _PGN130316CLASSPB._serialized_start=5612
  _PGN130316CLASSPB._serialized_end=5760
  _PGN130578CLASSPB._serialized_start=5763
  _PGN130578CLASSPB._serialized_end=5970
  _PGN130842MFG1857CLASSPB._serialized_start=5973
  _PGN130842MFG1857CLASSPB._serialized_end=6181
# @@protoc_insertion_point(module_scope)
