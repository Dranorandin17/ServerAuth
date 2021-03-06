import csv
import os.path
def _load():
    default_protocol_version = 0
    minecraft_versions = {}
    packet_names = {}
    packet_idents = {}
    packet_ident = 0
    last_section = None
    csvpath = os.path.abspath(os.path.join(os.path.dirname(__file__), "packets.csv"))
    with open(csvpath) as csvfile:
        reader = csv.reader(csvfile)
        for i, record in enumerate(reader):
            if i == 0: continue
            minecraft_version = record[0]
            protocol_version = int(record[1])
            protocol_mode = record[2]
            packet_direction = record[3]
            packet_name = record[4]
            section = (protocol_version, protocol_mode, packet_direction)
            if section != last_section: packet_ident = 0
            last_section = section
            default_protocol_version = max(default_protocol_version, protocol_version)
            minecraft_versions[protocol_version] = minecraft_version
            key = [protocol_version, protocol_mode, packet_direction]
            packet_names [tuple(key + [packet_ident])] = packet_name
            packet_idents[tuple(key + [packet_name ])] = packet_ident
            packet_ident += 1
    return default_protocol_version, minecraft_versions, packet_names, packet_idents
default_protocol_version, minecraft_versions, packet_names, packet_idents = _load()