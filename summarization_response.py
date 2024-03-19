from aea.protocols.base import Message

class SummarizationResponse(Message):
    protocol_id = "summarization_response"

    def __init__(self, summary: str):
        super().__init__(summary=summary)
