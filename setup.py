#  Copyright 2019 U.C. Berkeley RISE Lab
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from distutils.core import setup
import os
from setuptools.command.install import install


class InstallWrapper(install):
    def run(self):
        # compile the relevant protobufs
        self.compile_proto()

        # Run the standard PyPi copy
        install.run(self)

        # remove the compiled protobufs
        self.cleanup()

    def compile_proto(self):
        os.system('./scripts/clean.sh')
        os.system('./scripts/build.sh')

    def cleanup(self):
        os.system('./scripts/clean.sh')
        os.system('rm -rf Droplet.egg-info')


setup(
        name='Droplet',
        version='0.1.0',
        packages=['droplet', ],
        license='Apache v2',
        long_description='The Droplet Client and Server',
        install_requires=['zmq', 'protobuf', 'anna'],
        cmdclass={'install': InstallWrapper}
)
