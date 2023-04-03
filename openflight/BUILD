load("@rules_python//python:defs.bzl", "py_binary", "py_library")

py_library(
  name = "openflight",
  srcs = glob([
    "src/**/*.py",
    "openflight_audio/src/**/*.py",
    "openflight_video/src/**/*.py",
  ]),
  deps = [],
  visibility = ["//visibility:public"],
)

py_binary(
  name = "openflight_executable",
  srcs = ["openflight_executable.py"],
  deps = [
    ":openflight",
  ],
)
