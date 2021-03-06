import os
import logging

api_version = os.getenv("MENDER_API_VERSION", "0.1")

logger = logging.getLogger()

logger.setLevel(logging.DEBUG)
#logging.getLogger("paramiko").setLevel(logging.DEBUG)

logging.info("Setting api_version as: " + api_version)

import authentication
import admission
import deployments
import artifacts
import inventory

auth = authentication.Authentication()
adm = admission.Admission(auth)
deploy = deployments.Deployments(auth)
image = artifacts.Artifacts()
inv = inventory.Inventory(auth)
