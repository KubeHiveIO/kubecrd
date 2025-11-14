# CRD Schema Minimal <img referrerpolicy="no-referrer-when-downgrade" src="https://static.scarf.sh/a.png?x-pxid=e8da2de2-769b-48e2-a194-a1efb25883f6&page=example-01&title=CRD Schema Minimal" />

This is a simple example that simply prints the CRD schema for a given Python
dataclass. You can run it using::

## Example 1

``` sh
poetry run python3 examples/01-minimal/example_01.py
```

**OUTPUT**
``` yaml
  apiVersion: apiextensions.k8s.io/v1
  kind: CustomResourceDefinition
  metadata:
    name: resources.example.com
  spec:
    group: example.com
    names:
      kind: Resource
      plural: resources
      singular: resource
    scope: Namespaced
    versions:
    - name: v1alpha1
      schema:
        openAPIV3Schema:
          properties:
            spec:
              properties:
                id:
                  type: string
                name:
                  type: string
                tags:
                  default: []
                  description: regroup multiple resources
                  items:
                    type: string
                  type: array
                  uniqueItems: false
              required:
              - id
              - name
              type: object
          type: object
      served: true
      storage: true
```

## Example 2
``` sh
poetry run python3 examples/01-minimal/example_02-enum.py
```

**OUTPUT**

``` yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: exampleresources.example.com
spec:
  group: example.com
  names:
    kind: ExampleResource
    plural: exampleresources
    singular: exampleresource
  scope: Cluster
  versions:
  - additionalPrinterColumns: []
    name: v1alpha1
    schema:
      openAPIV3Schema:
        properties:
          spec:
            properties:
              id:
                type: string
              mode:
                default: Red
                description: Picking a Color
                enum:
                - Red
                - Blue
                - Green
                type: string
              name:
                type: string
            type: object
        type: object
    served: true
    storage: true
```