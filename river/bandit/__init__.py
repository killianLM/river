"""Multi-armed bandit (MAB) policies.

The bandit policies in River have a generic API. This allows them to be used in a variety of
situations. For instance, they can be used for model selection
(see `model_selection.BanditRegressor`).

"""
from __future__ import annotations

from . import base, envs
from .bayes_ucb import BayesUCB
from .epsilon_greedy import EpsilonGreedy
from .evaluate import evaluate, evaluate_offline
from .exp3 import Exp3
from .thompson import ThompsonSampling
from .ucb import UCB

__all__ = [
    "base",
    "envs",
    "evaluate",
    "evaluate_offline",
    "BayesUCB",
    "EpsilonGreedy",
    "Exp3",
    "ThompsonSampling",
    "UCB",
]
