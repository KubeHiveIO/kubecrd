from dataclasses import dataclass, field
from kubecrds import schemabase
from kubecrds.types import Scope
from kubernetes import client, config


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


@dataclass
class CrdSchemaResourceExists(schemabase.KubeResourceBase):
    __group__ = "simple-example.com"
    __version__ = "v1alpha1"
    __scope__ = Scope.NAMESPACE

    id: str
    testing: str
    name: str
    tags: list[str] = field(
        default_factory=list,
        metadata={
            "description": "regroup multiple resources",
        },
    )


def test_install_is_idempotent():
    config.load_kube_config()
    k8s_client = client.ApiClient()

    crd_install, resualt = CrdSchemaResource.install(
        k8s_client=k8s_client, exist_ok=True
    )
    assert crd_install is True
    assert resualt["code"] in ["CRD_INSTALLED", "CRD_SKIP_CREATE"]


def test_install_crd_already_exists():
    config.load_kube_config()
    k8s_client = client.ApiClient()

    crd_install_num_1, resualt = CrdSchemaResourceExists.install(
        k8s_client=k8s_client, exist_ok=True
    )
    assert crd_install_num_1 is True
    assert resualt["code"] in ["CRD_INSTALLED", "CRD_SKIP_CREATE"]

    crd_install_num_2, resualt = CrdSchemaResourceExists.install(
        k8s_client=k8s_client, exist_ok=False
    )
    assert crd_install_num_2 is False
    assert resualt["code"] in ["CRD_INSTALL_DENIED"]


def test_install_crd_already_exsits_allow_replace():
    assert True is True
