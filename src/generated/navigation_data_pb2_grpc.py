# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

<<<<<<<< HEAD:src/generated/navigation_data_pb2_grpc.py
import generated.navigation_data_pb2 as navigation__data__pb2
========
import generated.energy_pb2 as energy__pb2
>>>>>>>> refs/heads/main_publish:src/generated/energy_pb2_grpc.py



class EngineDataStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
<<<<<<<< HEAD:src/generated/navigation_data_pb2_grpc.py
        self.GetEngineData = channel.unary_unary(
                '/EngineData/GetEngineData',
                request_serializer=navigation__data__pb2.engine_request.SerializeToString,
                response_deserializer=navigation__data__pb2.engine_response.FromString,
                )
        self.GetEngineEvents = channel.unary_unary(
                '/EngineData/GetEngineEvents',
                request_serializer=navigation__data__pb2.engine_request.SerializeToString,
                response_deserializer=navigation__data__pb2.engine_response.FromString,
========
        self.GetDeviceInfo = channel.unary_unary(
                '/solar_mppt/GetDeviceInfo',
                request_serializer=energy__pb2.request.SerializeToString,
                response_deserializer=energy__pb2.MPPT_device.FromString,
                )
        self.GetOutput = channel.unary_unary(
                '/solar_mppt/GetOutput',
                request_serializer=energy__pb2.request.SerializeToString,
                response_deserializer=energy__pb2.solar_output.FromString,
>>>>>>>> refs/heads/main_publish:src/generated/energy_pb2_grpc.py
                )


class EngineDataServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetEngineData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEngineEvents(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EngineDataServicer_to_server(servicer, server):
    rpc_method_handlers = {
<<<<<<<< HEAD:src/generated/navigation_data_pb2_grpc.py
            'GetEngineData': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEngineData,
                    request_deserializer=navigation__data__pb2.engine_request.FromString,
                    response_serializer=navigation__data__pb2.engine_response.SerializeToString,
            ),
            'GetEngineEvents': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEngineEvents,
                    request_deserializer=navigation__data__pb2.engine_request.FromString,
                    response_serializer=navigation__data__pb2.engine_response.SerializeToString,
========
            'GetDeviceInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDeviceInfo,
                    request_deserializer=energy__pb2.request.FromString,
                    response_serializer=energy__pb2.MPPT_device.SerializeToString,
            ),
            'GetOutput': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOutput,
                    request_deserializer=energy__pb2.request.FromString,
                    response_serializer=energy__pb2.solar_output.SerializeToString,
>>>>>>>> refs/heads/main_publish:src/generated/energy_pb2_grpc.py
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'EngineData', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EngineData(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetEngineData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
<<<<<<<< HEAD:src/generated/navigation_data_pb2_grpc.py
        return grpc.experimental.unary_unary(request, target, '/EngineData/GetEngineData',
            navigation__data__pb2.engine_request.SerializeToString,
            navigation__data__pb2.engine_response.FromString,
========
        return grpc.experimental.unary_unary(request, target, '/solar_mppt/GetDeviceInfo',
            energy__pb2.request.SerializeToString,
            energy__pb2.MPPT_device.FromString,
>>>>>>>> refs/heads/main_publish:src/generated/energy_pb2_grpc.py
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEngineEvents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
<<<<<<<< HEAD:src/generated/navigation_data_pb2_grpc.py
        return grpc.experimental.unary_unary(request, target, '/EngineData/GetEngineEvents',
            navigation__data__pb2.engine_request.SerializeToString,
            navigation__data__pb2.engine_response.FromString,
========
        return grpc.experimental.unary_unary(request, target, '/solar_mppt/GetOutput',
            energy__pb2.request.SerializeToString,
            energy__pb2.solar_output.FromString,
>>>>>>>> refs/heads/main_publish:src/generated/energy_pb2_grpc.py
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
