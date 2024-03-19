from aea.protocols.base import Message

class SummarizationRequest(Message):
    protocol_id = "summarization_request"

    def __init__(self, content: str):
        super().__init__(content=content)
