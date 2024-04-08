# Data Processing Library

The Data Processing Framework is a python-based library and a set of transforms that enable the 
transformation, annotation and filtering of data (typically LLM training data contained in 
[parquet](https://arrow.apache.org/docs/python/parquet.html) files).
The distributed infrastructure, based on 
[Ray](https://docs.ray.io/en/latest/index.html), is used to scale out the transformation process.

It also includes transform execution automation based on 
[Kubeflow pipelines](https://www.kubeflow.org/docs/components/pipelines/v1/introduction/)(KFP) and
tested on [Kind cluster](https://kind.sigs.k8s.io/)

KFP implementation is based on [KubeRay Operator](https://docs.ray.io/en/master/cluster/kubernetes/getting-started.html)
for creating and managing Ray cluster and [KubeRay API server](https://github.com/ray-project/kuberay/tree/master/apiserver)
to interact with the KubeRay operator. An additional [framework](kfp/kfp_support_lib) along with the several
[kfp components](kfp/kfp_ray_components) to simplify pipelines implementation.

The framework allows simple 1:1 transformation of parquet files, but also enables
more complex transformations requiring coordination among transforming nodes.
This might include operations such as de-duplication, merging, and splitting.

Topics to explore:
   * [Data schema and processing](doc/data-processing.md)
   * [Available Transforms](transforms/README.md)
   * [Core library](data-processing-lib/README.md) and [its documentation](data-processing-lib/doc/overview.md)
   * [Kind cluster support](kind/README.md)
   * [KFP support library](kfp/kfp_support_lib/README.md) and [its implementation](kfp/kfp_support_lib/doc/kfp_support_library.md)

# Setup
After cloning the repo, enable the pre-commit hooks.
* Install [pre-commit](https://pre-commit.com/)
* `cd fm-data-engineering`
* `pre-commit install`

# Repository structure
* data_processing_lib - provides a library and framework supporting data transformations in a Ray cluster
* kfp - Kubeflow pipeline support
* kind - kind
* transform
    * universal
        * ededup 
        * fdedup 
        * ...
    * code
        * select_language
        * ...
    * language
        * language_id
        * ...

# Build and Makefiles
Makefiles are used for operations performed across all projects in the directory tree.
Using specific rules from the top of the repository tree will recurse their execution
into subdirectories  until subdirectories provide a Makefile that implements the action
and/or recurses further.  For example,
```shell
make build
```
will apply the `make build` rule into all sub-directories supporting such recursion.

Standard rules include the following:

* clean
* setup
* build
* test
* publish
* ... 
