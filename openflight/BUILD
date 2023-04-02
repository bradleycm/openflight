package(default_visibility = ["//visibility:public"])

load("@openflight_libraries//openflight_video:openflight_video.bzl", "openflight_video")

py_library(
  name = "openflight",
  srcs = glob(["src/**/*.py"]),
  deps = [
    openflight_video,
  ],
)
