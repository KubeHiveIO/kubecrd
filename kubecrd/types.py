from enum import Enum


class Scope(str, Enum):
    CLUSTER = "Cluster"
    NAMESPACE = "Namespaced"
