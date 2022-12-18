from dataclasses import dataclass
from datetime import date


@dataclass
class InternalStatementLineRaw:
    operation_date: date
    amount: float
    client_account_raw: str
    client_tax_number: str
    client_name: str
    description_raw: str




class ParsingError(RuntimeError):
    """
    Raised when obligatory parts of the statement are missing or are incorrect
    """
    pass


class IParserPlugin:
    def parse_raw_statement(self, statement: bytes) -> list[InternalStatementLineRaw]:
        pass


class IEncodingDetector:

    def detect_encoding(self, sample: bytes) -> list[str]:
        """

        :param sample:
        :return: name of the encoding(s) detected; [0] is the most probable one
        """
        pass

class IExporterPlugin:
    def export_statement(statement: list[InternalStatementLineRaw]) -> bytes:
        """
        :return: bytes that can be saved to file, and fed to accounting program
        """
