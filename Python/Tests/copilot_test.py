# Copyright (C) 2018  Copilot Core Team
# copilot is open-source software, licensed under the Apache License, Version 2.0,
# and you are kindly asked to keep the full copyright notice intact.
# You may use the software for any purpose, but you are asked only to
# inform us about your use of the software.  You are not allowed to
# distribute the software in any other way than to the official website
# http://copilot.de/
# You may only use the software in accordance with the terms of the
# Apache License version 2.0.
# You may obtain a copy of the Apache License at:
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the Apache License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the Apache License for the specific language governing permissions and
# limitations under the License.
# This program is part of the Copilot project, which is developed by the
# "Eine Universität" (University one) in cooperation with the
# "Technische Universität München" (TUM), and the
# "Deutsches Zentrum für Luft- und Raumfahrt e.V." (DLR).
# See http://www.copilot.de/ for details.


import sys
import os
import time
import json
import logging
import argparse
import subprocess
import signal
import threading
import queue
import socket
import select
import re
import shlex
import shutil
import tempfile
import zipfile
import tarfile
import hashlib
import base64
import urllib.request
import urllib.error
import urllib.parse
