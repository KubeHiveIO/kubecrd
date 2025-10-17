import json
from dataclasses import dataclass, field
from apischema import schema
from kubecrd import KubeResourceBase


@dataclass
class Resource(KubeResourceBase):
    __group__ = "example.com"
    __version__ = "v1alpha1"

    name: str
    tags: list[str] = field(default_factory=list, metadata=schema(description="tags"))


def test_resource_serialization_structure():
    """Ensure Resource serializes correctly to Kubernetes CRD format."""
    example = Resource(name="myResource", tags=["tag1", "tag2"])
    serialized = example.serialize()

    assert serialized["apiVersion"] == "example.com/v1alpha1"
    assert serialized["kind"] == "Resource"
    assert serialized["spec"]["name"] == "myResource"
    assert serialized["spec"]["tags"] == ["tag1", "tag2"]

    # ensure it's valid JSON
    json.dumps(serialized)
