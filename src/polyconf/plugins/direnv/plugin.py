"""
Expects "K8SCFG_" prefix.

Example content of ".envrc":

    export K8SCFG_AWS_PROFILE="CRM-Devops"
    export K8SCFG_NATIVE_ACCOUNT="devops"
    export K8SCFG_DEFAULT_ACCOUNT="dev"
    export K8SCFG_DEFAULT_REGION="us-west-2"
    export K8SCFG_DEFAULT_NAMESPACE="default"

"""
from pathlib import Path
import logging

# from k8scfg.config import base
#
#
# SOURCE_NAME = "direnv"
# COMMON_PREFIX = "K8SCFG_"
# log = logging.getLogger(__name__)
#
#
# def hydrate(data: base.Data) -> base.Data:
#     local_direnv_file = Path.cwd() / ".envrc"
#     if not local_direnv_file.is_file():
#         return data
#     env_data = local_direnv_file.read_text()
#
#     env_lines = [
#         x.removeprefix(f"export {COMMON_PREFIX}")
#         for x in env_data.splitlines()
#         if x.startswith(f"export {COMMON_PREFIX}")
#     ]
#
#     # # Method 1 -- iterate lines, set attrs if keys look valid
#     # for line in env_lines:
#     #     key_, value_ = line.split("=", maxsplit=1)
#     #     key = key_.lower()
#     #     value = value_.strip("\"'")
#     #     log.info(f"FOUND: {key=} {value=}")
#     #
#     #     if key in dir(data):
#     #         setattr(data, key, value)
#     #     else:
#     #         log.warning(f"{key=} not found in {data=}")
#     #
#     #     # if "_" in key:
#     #     #     section, key = key.split("_", maxsplit=1)
#     #     #     if section in base.section_names:
#     #     #         ...
#
#     # Method 2 -- iterate known keys, attempt lookup in lines
#     found = {}
#     for line in env_lines:
#         key_, value = line.split("=", maxsplit=1)
#         key = key_.lower()
#         # value = value_.strip("\"'")
#         found[key] = value
#     for key in [attr for attr in dir(data) if not attr.startswith("_")]:
#         if value := found.get(key):
#             log.info(f"{SOURCE_NAME} FOUND: {key=} {value=}")
#             if key in dir(base.Raw):
#                 setattr(data.raw, key, value)
#                 data.raw.seen.add(key)
#             else:
#                 setattr(data, key, value)
#             data.sources[key] = SOURCE_NAME
#
#     return data
#
#
# def method_name(section: str, data: base.Data, env_lines: list[str]) -> base.Data:
#     # section = "default"
#     section_lines = [
#         x.removeprefix(f"{section.upper()}_")
#         for x in env_lines
#         if x.startswith(f"{section.upper()}_")
#     ]
#     for line in section_lines:
#         key_, value_ = line.split("=", maxsplit=1)
#         key = key_.lower()
#         value = value_.strip("\"'")
#         log.info(f"FOUND: {key=} {value=}")
#
#         qualified_key = f"{section}_{key}"
#         if qualified_key in dir(data):
#             setattr(data, qualified_key, value)
#         else:
#             log.warning(f"Unknown key found in.envrc: {key}")
#
#     return data
