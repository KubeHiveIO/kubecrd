from dataclasses import dataclass, field
from kubecrds import schemabase
from kubecrds.types import Scope
from kubernetes import client, config


@dataclass
class CrdSchemaResourceToDelete(schemabase.KubeResourceBase):
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


@dataclass
class CrdSchemaResourceToDeleteNotFound(schemabase.KubeResourceBase):
    __group__ = "simple-example.com"
    __version__ = "v1alpha1"
    __scope__ = Scope.NAMESPACE

    id: str
    name: str


def test_delete_crd():
    config.load_kube_config()
    k8s_client = client.ApiClient()

    crd_install, resualt = CrdSchemaResourceToDelete.install(
        k8s_client=k8s_client, exist_ok=True
    )
    assert crd_install is True
    assert resualt["code"] in ["CRD_INSTALLED", "CRD_SKIP_CREATE"]

    resualt, response = CrdSchemaResourceToDelete.delete(k8s_client=k8s_client)

    assert resualt is True
    assert response["code"] == "CRD_DELETED"


def test_delete_crd_not_exists():
    config.load_kube_config()
    k8s_client = client.ApiClient()

    resualt, response = CrdSchemaResourceToDeleteNotFound.delete(k8s_client=k8s_client)

    assert resualt is False
    assert response["code"] == "CRD_DELETE_FAILED"
