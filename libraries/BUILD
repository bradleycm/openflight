load("@rules_python//python:defs.bzl", "py_library")

py_library(
  name = "deps",
  srcs = ["requirements.txt"],
)

py_library(
  name = "openflight_video",
  srcs = glob(["openflight_video/**/*.py"]),
  deps = [
    "@opencv//python:opencv",
    "@numpy",
    "@pyyaml",
    "@protobuf//:python",
    "@grpcio//:grpcio",
    "@grpcio//grpc_tools:grpc_tools",
    "@openflight_components//:deps",
  ],
  visibility = ["//visibility:public"],
)
