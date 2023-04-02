load("@rules_python//python:defs.bzl", "py_binary", "py_library")

py_library(
  name = "openflight_video",
  srcs = glob(["src/**/*.py"]),
  visibility = ["//visibility:public"],
)

py_binary(
  name = "openflight_video_executable",
  srcs = ["openflight_video_executable.py"],
  deps = [
    ":openflight_video",
  ],
)