import yaml
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


def test_crd_schema_additional_printer_columns_generates_valid_yaml():
    """Ensure the generated CRD schema contains expected keys."""
    crd_yaml = CrdSchemaAdditionalPrinterColumnsResource.crd_schema()
    crd = yaml.safe_load(crd_yaml)

    assert crd["apiVersion"] == "apiextensions.k8s.io/v1"
    assert crd["kind"] == "CustomResourceDefinition"
    assert (
        crd["metadata"]["name"]
        == "crdschemaadditionalprintercolumnsresources.simple-example.com"
    )
    assert crd["spec"]["group"] == "simple-example.com"
    assert "versions" in crd["spec"]
    assert crd["spec"]["names"]["kind"] == "CrdSchemaAdditionalPrinterColumnsResource"
    assert crd["spec"]["versions"][0]["name"] == "v1alpha1"

    assert (
        crd["spec"]["versions"][0]["additionalPrinterColumns"][0]["name"] == "replicas"
    )
    assert (
        crd["spec"]["versions"][0]["additionalPrinterColumns"][0]["jsonPath"]
        == ".spec.replicas"
    )
    assert (
        crd["spec"]["versions"][0]["additionalPrinterColumns"][0]["type"] == "integer"
    )
