from abc import ABC, abstractmethod
from typing import List

import spacy

import pandas as pd


class BaseTextProcessor(ABC):
    def __init__(self, pipeline: str = None):
        super().__init__()
        self.nlp = None
        if pipeline:
            self.nlp = spacy.load(pipeline)
        self.text = ''
        self.doc = None
        self.sequences = []
        self.chunks = []
        self.n_tokens = []
        self.segments = []
        self.dataframe = pd.DataFrame([])

    @abstractmethod
    def split(self, text: str) -> List[str]:
        pass

    @abstractmethod
    def to_chunks(self, text: str, model: str) -> List[str]:
        pass

    @abstractmethod
    def group_by_semantics(self, text: str, model: str) -> pd.DataFrame:
        pass
