from dataclasses import dataclass, field
from enum import Enum
from kubecrds import schemabase
from kubecrds.types import Scope


class Color(Enum):
    RED = "Red"
    BLUE = "Blue"
    GREEN = "Green"


@dataclass
class ExampleResource(schemabase.KubeResourceBase):
    __group__ = "example.com"
    __version__ = "v1alpha1"
    __scope__ = Scope.CLUSTER

    id: str
    name: str
    mode: Color = field(
        metadata={
            "description": "Picking a Color",
            "default": Color.RED.value,
        },
    )


print([value.value for value in Color])


def main():
    print(ExampleResource.crd_schema())


if __name__ == "__main__":
    main()
