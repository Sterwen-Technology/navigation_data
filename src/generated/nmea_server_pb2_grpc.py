# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import nmea_messages_pb2 as nmea__messages__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in nmea_server_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class NMEAServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.status = channel.unary_unary(
                '/NMEAServer/status',
                request_serializer=nmea__messages__pb2.server_cmd.SerializeToString,
                response_deserializer=nmea__messages__pb2.server_resp.FromString,
                _registered_method=True)
        self.sendNMEA = channel.unary_unary(
                '/NMEAServer/sendNMEA',
                request_serializer=nmea__messages__pb2.nmea_msg.SerializeToString,
                response_deserializer=nmea__messages__pb2.server_resp.FromString,
                _registered_method=True)
        self.getNMEA = channel.unary_stream(
                '/NMEAServer/getNMEA',
                request_serializer=nmea__messages__pb2.server_cmd.SerializeToString,
                response_deserializer=nmea__messages__pb2.nmea_msg.FromString,
                _registered_method=True)


class NMEAServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def status(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendNMEA(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getNMEA(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NMEAServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'status': grpc.unary_unary_rpc_method_handler(
                    servicer.status,
                    request_deserializer=nmea__messages__pb2.server_cmd.FromString,
                    response_serializer=nmea__messages__pb2.server_resp.SerializeToString,
            ),
            'sendNMEA': grpc.unary_unary_rpc_method_handler(
                    servicer.sendNMEA,
                    request_deserializer=nmea__messages__pb2.nmea_msg.FromString,
                    response_serializer=nmea__messages__pb2.server_resp.SerializeToString,
            ),
            'getNMEA': grpc.unary_stream_rpc_method_handler(
                    servicer.getNMEA,
                    request_deserializer=nmea__messages__pb2.server_cmd.FromString,
                    response_serializer=nmea__messages__pb2.nmea_msg.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'NMEAServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('NMEAServer', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class NMEAServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def status(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/NMEAServer/status',
            nmea__messages__pb2.server_cmd.SerializeToString,
            nmea__messages__pb2.server_resp.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def sendNMEA(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/NMEAServer/sendNMEA',
            nmea__messages__pb2.nmea_msg.SerializeToString,
            nmea__messages__pb2.server_resp.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def getNMEA(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/NMEAServer/getNMEA',
            nmea__messages__pb2.server_cmd.SerializeToString,
            nmea__messages__pb2.nmea_msg.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
