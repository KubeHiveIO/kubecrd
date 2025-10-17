from dataclasses import dataclass, field
from kubecrds import schemabase
from kubecrds.types import Scope


@dataclass
class ExampleResource(schemabase.KubeResourceBase):
    __group__ = "example.com"
    __version__ = "v1alpha1"
    __scope__ = Scope.CLUSTER

    id: str
    name: str
    tags: list[str] = field(
        default_factory=list,
        metadata={
            "description": "regroup multiple resources",
        },
    )


def main():
    print(ExampleResource.crd_schema())


if __name__ == "__main__":
    main()
