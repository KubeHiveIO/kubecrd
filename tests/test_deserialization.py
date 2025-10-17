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


def test_from_json_loads_metadata(tmp_path):
    """Ensure Resource.from_json restores data and metadata."""
    cr_data = {
        "apiVersion": "example.com/v1alpha1",
        "kind": "Resource",
        "metadata": {
            "generation": 1,
            "name": "myresource1",
            "namespace": "default",
            "resourceVersion": "105572812",
            "uid": "02102eb3-968b-418a-8023-75df383daa3c",
        },
        "spec": {"name": "bestID", "tags": ["tag1", "tag2"]},
    }

    datafile = tmp_path / "cr.json"
    datafile.write_text(json.dumps(cr_data))

    with open(datafile) as fd:
        json_schema = json.load(fd)

    res = Resource.from_json(json_schema)

    assert res.name == "bestID"
    assert res.tags == ["tag1", "tag2"]
    assert res.metadata.name == "myresource1"
    assert res.metadata.namespace == "default"
    assert res.metadata.resource_version == "105572812"
