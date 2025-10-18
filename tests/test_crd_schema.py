import yaml
from dataclasses import dataclass, field
from kubecrds import schemabase
from kubecrds.types import Scope


@dataclass
class CrdSchemaResource(schemabase.KubeResourceBase):
    __group__ = "simple-example.com"
    __version__ = "v1alpha1"
    __scope__ = Scope.NAMESPACE

    id: str
    name: str
    tags: list[str] = field(
        default_factory=list,
        metadata={
            "description": "regroup multiple resources",
        },
    )


def test_crd_schema_generates_valid_yaml():
    """Ensure the generated CRD schema contains expected keys."""
    crd_yaml = CrdSchemaResource.crd_schema()
    crd = yaml.safe_load(crd_yaml)

    assert crd["apiVersion"] == "apiextensions.k8s.io/v1"
    assert crd["kind"] == "CustomResourceDefinition"
    assert crd["metadata"]["name"] == "crdschemaresources.simple-example.com"
    assert crd["spec"]["group"] == "simple-example.com"
    assert "versions" in crd["spec"]
    assert crd["spec"]["names"]["kind"] == "CrdSchemaResource"
    assert crd["spec"]["versions"][0]["name"] == "v1alpha1"
