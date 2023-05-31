# Copyright 2022 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from dataclasses import dataclass, field
from typing import Optional

from .my_ppo_trainer import flatten_dict


@dataclass
class PPOConfig(object):
    """
    Configuration class for PPOTrainer
    """

    model_name: Optional[str] = field(
        default=None,
        metadata={"help": "Name of model to use - used only for tracking purposes"},
    )
    steps: Optional[int] = field(
        default=20000, metadata={"help": "Number of training steps"}
    )
    learning_rate: Optional[float] = field(
        default=1e-5, metadata={"help": "Adam learning rate"}
    )
    adap_kl_ctrl: Optional[bool] = field(
        default=True, metadata={"help": "Use adaptive KL control, otherwise linear"}
    )
    init_kl_coef: Optional[float] = field(
        default=0.2,
        metadata={
            "help": "Initial KL penalty coefficient (used for adaptive and linear control)"
        },
    )
    target: Optional[float] = field(
        default=6, metadata={"help": "Target KL value for adaptive KL control"}
    )
    horizon: Optional[float] = field(
        default=10000, metadata={"help": "Horizon for adaptive KL control"}
    )
    gamma: Optional[float] = field(
        default=1, metadata={"help": "Gamma parameter for advantage calculation"}
    )
    lam: Optional[float] = field(
        default=0.95, metadata={"help": "Lambda parameter for advantage calculation"}
    )
    cliprange: Optional[float] = field(
        default=0.2, metadata={"help": "Range for clipping in PPO policy gradient loss"}
    )
    cliprange_value: Optional[float] = field(
        default=0.2, metadata={"help": "Range for clipping values in loss calculation"}
    )
    vf_coef: Optional[float] = field(
        default=0.1, metadata={"help": "Scaling factor for value loss"}
    )
    batch_size: Optional[int] = field(
        default=256, metadata={"help": "Number of samples per optimisation step"}
    )
    mini_batch_size: Optional[int] = field(
        default=1, metadata={"help": "Number of samples optimized inside PPO together"}
    )
    ppo_epochs: Optional[int] = field(
        default=1,
        metadata={"help": "Number of optimisation epochs per batch of samples"},
    )

    def to_dict(self):
        output_dict = {}
        for key, value in self.__dict__.items():
            output_dict[key] = value
        return flatten_dict(output_dict)