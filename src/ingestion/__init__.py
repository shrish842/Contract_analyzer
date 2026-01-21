"""
Data ingestion module for collecting contracts from various sources.
"""

from .sec_downloader import SECDownloader
from .contract_parser import ContractParser

__all__ = ['SECDownloader', 'ContractParser']
