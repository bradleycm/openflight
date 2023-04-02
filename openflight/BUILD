package(default_visibility = ["//visibility:public"])

load("@openflight_components//openflight_video:deps.bzl", "openflight_video")

py_library(
  name = "openflight",
  srcs = glob(["src/**/*.py"]),
  deps = [
    openflight_video,
  ],
)
