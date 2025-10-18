import yaml
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


def test_crd_schema_nested_properties_generates_valid_yaml():
    """Ensure the generated CRD schema contains expected keys."""
    crd_yaml = ExampleNested.crd_schema()
    crd = yaml.safe_load(crd_yaml)

    assert crd["apiVersion"] == "apiextensions.k8s.io/v1"
    assert crd["kind"] == "CustomResourceDefinition"
    assert crd["metadata"]["name"] == "examplenesteds.nested-example.com"
    assert crd["spec"]["group"] == "nested-example.com"
    assert "versions" in crd["spec"]
    assert crd["spec"]["names"]["kind"] == "ExampleNested"
    assert crd["spec"]["versions"][0]["name"] == "v1alpha1"
