# CRD Schema

This is a nested example that simply prints the CRD schema for a given Python
dataclass with nested dataclass. You can run it using:

``` sh
poetry run python examples/04-nested-crd/nested_crd.py
```


``` yaml
  apiVersion: apiextensions.k8s.io/v1
  kind: CustomResourceDefinition
  metadata:
    name: examplenesteds.nested-example.com
  spec:
    group: nested-example.com
    names:
      kind: ExampleNested
      plural: examplenesteds
      singular: examplenested
    scope: Cluster
    versions:
    - name: v1alpha1
      schema:
        openAPIV3Schema:
          properties:
            spec:
              properties:
                name:
                  type: string
                sourceRef:
                  properties:
                    kind:
                      type: string
                    name:
                      type: string
                    namespace:
                      description: The namespace of the source resource.
                      type: string
                  type: object
                targetNamespaces:
                  description: List of namespaces to replicate the resource into.
                  items:
                    type: string
                  type: array
              type: object
          type: object
      served: true
      storage: true
```