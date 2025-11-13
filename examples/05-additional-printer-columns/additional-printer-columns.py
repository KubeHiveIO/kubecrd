from dataclasses import dataclass, field
from kubecrds import schemabase
from kubecrds.types import Scope


@dataclass
class CrdSchemaAdditionalPrinterColumnsResource(schemabase.KubeResourceBase):
    __group__ = "simple-example.com"
    __version__ = "v1alpha1"
    __scope__ = Scope.NAMESPACE
    __additionalPrinterColumns__ = [
        schemabase.KubeResourceAdditionalPrinterColumns(
            name="replicas",
            type=schemabase.AdditionalPrinterColumnsType.Integer,
            jsonPath=".spec.replicas",
        ),
    ]

    id: str
    name: str
    replicas: int


print(CrdSchemaAdditionalPrinterColumnsResource.crd_schema())
