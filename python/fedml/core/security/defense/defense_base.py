from abc import ABC, abstractmethod
from typing import List, Tuple, Dict, Any, Callable


class BaseDefenseMethod(ABC):
    @abstractmethod
    def __init__(self, config):
        pass

    @abstractmethod
    def run(
        self,
        raw_client_grad_list: List[Tuple[float, Dict]],
        base_aggregation_func: Callable = None,
        extra_auxiliary_info: Any = None,
    ) -> Dict:
        """
        args:
            base_aggregation_func: this can be aggregation function in FedAvg, FedOPT, or any other machine learning optimizer.
            client_grad_list: client_grad_list is a list, each item is (sample_num, gradients)
            extra_auxiliary_info: for methods which need extra info (e.g., data, previous model/gradient),
                                please use this variable.
        return:
            Note: the data type of the return variable should be the same as the input
        """
        pass

    def defend_before_aggregation(
            self,
            raw_client_grad_list: List[Tuple[float, Dict]],
            extra_auxiliary_info: Any = None,
    ) -> List[Tuple[float, Dict]]:
        """
        args:
            client_grad_list: client_grad_list is a list, each item is (sample_num, gradients)
            extra_auxiliary_info: for methods which need extra info (e.g., data, previous model/gradient),
                                please use this variable.
        return:
            Note: the data type of the return variable should be the same as the input
        """
        pass

    def defend_on_aggregation(
            self,
            raw_client_grad_list: List[Tuple[float, Dict]],
            base_aggregation_func: Callable = None,
            extra_auxiliary_info: Any = None,
    ) -> Dict:
        """
        args:
            base_aggregation_func: this can be aggregation function in FedAvg, FedOPT, or any other machine learning optimizer.
            client_grad_list: client_grad_list is a list, each item is (sample_num, gradients)
            extra_auxiliary_info: for methods which need extra info (e.g., data, previous model/gradient),
                                please use this variable.
        return:
            Note: the data type of the return variable should be the same as the input
        """
        pass

    def get_malicious_client_idxs(self):
        return []