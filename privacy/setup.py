# Copyright 2018, The TensorFlow Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""TensorFlow Privacy library setup file for pip."""
from setuptools import find_packages
from setuptools import setup

setup(
    name='tensorflow_privacy',
    version='0.7.3',
    url='https://github.com/tensorflow/privacy',
    license='Apache-2.0',
    install_requires=[
        'scipy>=0.17',
        'tensorflow-estimator>=2.3.0',  # for DP versions of estimator.
        'attrs>=21.2.0',  # for tree_aggregation_query.py.
        'mpmath',  # used in tests only
        'dm-tree~=0.1.1',  # used in tests only
        'tensorflow-probability>=0.13.0',  # For discrete Gaussian.
        'tensorflow-datasets>=4.4.0'
    ],
    # Explicit dependence on TensorFlow is not supported.
    # See https://github.com/tensorflow/tensorflow/issues/7166
    extras_require={
        'tf': ['tensorflow>=1.0.0'],
        'tf_gpu': ['tensorflow-gpu>=1.0.0'],
    },
    packages=find_packages())