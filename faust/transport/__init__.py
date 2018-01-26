"""Transport registry."""
from typing import Type
from ..types import TransportT
from ..utils.imports import FactoryMapping

__all__ = ['by_name', 'by_url']

TRANSPORTS: FactoryMapping[Type[TransportT]] = FactoryMapping(
    aiokafka='faust.transport.librdkafka:Transport',
    confluent='faust.transport.confluent:Transport',
    kafka='faust.transport.librdkafka:Transport',
    memory='faust.transport.memory:Transport',
)
TRANSPORTS.include_setuptools_namespace('faust.transports')
by_name = TRANSPORTS.by_name
by_url = TRANSPORTS.by_url
