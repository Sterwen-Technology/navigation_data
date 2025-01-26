# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import generated.ecu_pb2 as ecu__pb2

import nmea2000_pb2 as nmea2000__pb2

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
        + f' but the generated code in ecu_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ECU_NMEA2000Stub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.open_ca = channel.unary_unary(
                '/ECU_NMEA2000/open_ca',
                request_serializer=ecu__pb2.OpenControllerApplicationRequest.SerializeToString,
                response_deserializer=ecu__pb2.ControllerApplication.FromString,
                _registered_method=True)
        self.getMessages = channel.unary_stream(
                '/ECU_NMEA2000/getMessages',
                request_serializer=ecu__pb2.ControllerApplicationRequest.SerializeToString,
                response_deserializer=nmea2000__pb2.nmea2000pb.FromString,
                _registered_method=True)
        self.sendMessage = channel.unary_unary(
                '/ECU_NMEA2000/sendMessage',
                request_serializer=ecu__pb2.ControllerApplicationSendMsg.SerializeToString,
                response_deserializer=ecu__pb2.ControllerApplicationStatus.FromString,
                _registered_method=True)


class ECU_NMEA2000Servicer(object):
    """Missing associated documentation comment in .proto file."""

    def open_ca(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getMessages(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ECU_NMEA2000Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'open_ca': grpc.unary_unary_rpc_method_handler(
                    servicer.open_ca,
                    request_deserializer=ecu__pb2.OpenControllerApplicationRequest.FromString,
                    response_serializer=ecu__pb2.ControllerApplication.SerializeToString,
            ),
            'getMessages': grpc.unary_stream_rpc_method_handler(
                    servicer.getMessages,
                    request_deserializer=ecu__pb2.ControllerApplicationRequest.FromString,
                    response_serializer=nmea2000__pb2.nmea2000pb.SerializeToString,
            ),
            'sendMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.sendMessage,
                    request_deserializer=ecu__pb2.ControllerApplicationSendMsg.FromString,
                    response_serializer=ecu__pb2.ControllerApplicationStatus.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ECU_NMEA2000', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ECU_NMEA2000', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ECU_NMEA2000(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def open_ca(request,
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
            '/ECU_NMEA2000/open_ca',
            ecu__pb2.OpenControllerApplicationRequest.SerializeToString,
            ecu__pb2.ControllerApplication.FromString,
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
    def getMessages(request,
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
            '/ECU_NMEA2000/getMessages',
            ecu__pb2.ControllerApplicationRequest.SerializeToString,
            nmea2000__pb2.nmea2000pb.FromString,
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
    def sendMessage(request,
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
            '/ECU_NMEA2000/sendMessage',
            ecu__pb2.ControllerApplicationSendMsg.SerializeToString,
            ecu__pb2.ControllerApplicationStatus.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
