from typing import List

import pandas as pd

from api.parsers._base import BaseParser


class AdcpParser(BaseParser):

    INDEX_COL = 0
    NAN_VALUES = [99.0, 999, 9999]

    @classmethod
    def df_from_responses(cls, responses: List[dict]) -> pd.DataFrame:
        return super(AdcpParser, cls).df_from_responses(responses)
