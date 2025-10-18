from dataclasses import dataclass, field
from kubecrds import schemabase
from kubecrds.types import Scope


@dataclass
class SourceRef(schemabase.KubeResourceBase):
    kind: str
    name: str
    namespace: str = field(
        metadata={
            "description": "The namespace of the source resource.",
        }
    )


@dataclass
class ExampleNested(schemabase.KubeResourceBase):
    __group__ = "nested-example.com"
    __version__ = "v1alpha1"
    __scope__ = Scope.CLUSTER

    name: str
    sourceRef: SourceRef
    targetNamespaces: list[str] = field(
        default_factory=list,
        metadata={
            "description": "List of namespaces to replicate the resource into.",
        },
    )


def main():
    print(ExampleNested.crd_schema())


if __name__ == "__main__":
    main()
