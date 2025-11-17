from dataclasses import dataclass
from datetime import datetime, date
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
    last_synced: datetime
    create_date: date


def main():
    print(ExampleResource.crd_schema())


if __name__ == "__main__":
    main()
