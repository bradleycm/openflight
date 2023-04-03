load("@rules_python//python:defs.bzl", "py_binary", "py_library")

py_library(
  name = "openflight_audio",
  srcs = glob(["src/**/*.py"]),
  visibility = ["//visibility:public"],
)

py_binary(
  name = "openflight_audio_executable",
  srcs = ["openflight_audio_executable.py"],
  deps = [
    ":openflight_audio",
  ],
)
