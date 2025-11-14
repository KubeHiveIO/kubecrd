from enum import Enum
import yaml
from dataclasses import dataclass, field
from kubecrds import schemabase
from kubecrds.types import Scope


class Color(Enum):
    RED = "Red"
    BLUE = "Blue"
    GREEN = "Green"


@dataclass
class CrdSchemaEnumResource(schemabase.KubeResourceBase):
    __group__ = "simple-example.com"
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


def test_crd_schema_enum_generates_valid_yaml():
    """Ensure the generated CRD schema contains expected keys."""
    crd_yaml = CrdSchemaEnumResource.crd_schema()
    crd = yaml.safe_load(crd_yaml)

    assert crd["apiVersion"] == "apiextensions.k8s.io/v1"
    assert crd["kind"] == "CustomResourceDefinition"
    assert crd["metadata"]["name"] == "crdschemaenumresources.simple-example.com"
    assert crd["spec"]["group"] == "simple-example.com"
    assert "versions" in crd["spec"]
    assert crd["spec"]["names"]["kind"] == "CrdSchemaEnumResource"
    assert crd["spec"]["versions"][0]["name"] == "v1alpha1"

    assert (
        len(
            crd["spec"]["versions"][0]["schema"]["openAPIV3Schema"]["properties"][
                "spec"
            ]["properties"]["mode"]["enum"]
        )
        == 3
    )
    assert (
        crd["spec"]["versions"][0]["schema"]["openAPIV3Schema"]["properties"]["spec"][
            "properties"
        ]["mode"]["default"]
        == "Red"
    )
