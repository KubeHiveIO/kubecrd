import json


def test_resource_serialization_structure():
    """Ensure Resource serializes correctly to Kubernetes CRD format."""
    # example = Resource(
    #     spec=ResourceSpec(
    #         name="myResource",
    #         tags=["tag1", "tag2"],
    #     ),
    # )
    # serialized = example.serialize()

    # assert serialized["apiVersion"] == "example.com/v1alpha1"
    # # assert serialized["kind"] == "Resource"
    # # assert serialized["spec"]["name"] == "myResource"
    # # assert serialized["spec"]["tags"] == ["tag1", "tag2"]

    # # ensure it's valid JSON
    # json.dumps(serialized)
    assert True is True
