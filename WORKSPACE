load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

rules_python_version = "740825b7f74930c62f44af95c9a4c1bd428d2c53"

http_archive(
  name = "rules_python",
  sha256 = "09a3c4791c61b62c2cbc5b2cbea4ccc32487b38c7a2cc8f87a794d7a659cc742",
  strip_prefix = "rules_python-{}".format(rules_python_version),
  url = "https://github.com/bazelbuild/rules_python/archive/{}.zip".format(rules_python_version),
)

http_archive(
  name = "openflight_libraries",
  sha256 = "592565f41c879330f8193ae9e5c3f855e4d6de6c",
  urls = [
    "https://github.com/bradleycm/openflight/blob/main/openflight_libraries.zip",
  ],
  build_file_content = """
package(default_visibility = ["//visibility:public"])

load("@openflight_libraries//:openflight_video", "openflight_video")

# Declare additional libraries here.
"""
)