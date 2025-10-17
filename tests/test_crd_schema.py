import yaml
from dataclasses import dataclass, field
from apischema import schema
from kubecrd import KubeResourceBase


@dataclass
class Resource(KubeResourceBase):
    __group__ = "example.com"
    __version__ = "v1alpha1"

    name: str
    tags: list[str] = field(
        default_factory=list,
        metadata=schema(
            description="regroup multiple resources",
            unique=False,
        ),
    )


def test_crd_schema_generates_valid_yaml():
    """Ensure the generated CRD schema contains expected keys."""
    crd_yaml = Resource.crd_schema()
    crd = yaml.safe_load(crd_yaml)

    assert crd["apiVersion"] == "apiextensions.k8s.io/v1"
    assert crd["kind"] == "CustomResourceDefinition"
    assert crd["metadata"]["name"] == "resources.example.com"
    assert crd["spec"]["group"] == "example.com"
    assert "versions" in crd["spec"]
    assert crd["spec"]["names"]["kind"] == "Resource"
    assert crd["spec"]["versions"][0]["name"] == "v1alpha1"
