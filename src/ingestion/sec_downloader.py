"""
SEC EDGAR contract downloader.
Downloads material contracts (EX-10.*) from public companies.
"""

from sec_edgar_downloader import Downloader
from pathlib import Path
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SECDownloader:
    """Download contracts from SEC EDGAR filings"""
    
    def __init__(self, company_name: str, email: str, output_dir: str = "data/raw/real_contracts"):
        """
        Initialize SEC downloader
        
        Args:
            company_name: Your company/project name for SEC requests
            email: Your email for SEC requests (required)
            output_dir: Directory to save downloaded contracts
        """
        self.downloader = Downloader(company_name, email)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def download_contracts(self, ticker: str, filing_types: list = ['10-K', '8-K'], 
                          after_date: str = "2020-01-01", before_date: str = "2024-12-31"):
        """
        Download contracts for a specific company
        
        Args:
            ticker: Stock ticker symbol (e.g., 'AAPL')
            filing_types: List of filing types to download
            after_date: Start date (YYYY-MM-DD)
            before_date: End date (YYYY-MM-DD)
        """
        logger.info(f"Downloading contracts for {ticker}...")
        
        for filing_type in filing_types:
            try:
                self.downloader.get(
                    filing_type, 
                    ticker, 
                    after=after_date, 
                    before=before_date
                )
                logger.info(f"Downloaded {filing_type} filings for {ticker}")
                time.sleep(2)  # Be respectful to SEC servers
                
            except Exception as e:
                logger.error(f"Error downloading {filing_type} for {ticker}: {e}")
    
    def download_multiple(self, tickers: list):
        """Download contracts for multiple companies"""
        for ticker in tickers:
            self.download_contracts(ticker)


if __name__ == "__main__":
    # Example usage
    downloader = SECDownloader(
        company_name="ContractAnalyzerProject",
        email="your.email@example.com"
    )
    
    # Download from major companies
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'TSLA', 'JPM']
    downloader.download_multiple(tickers)
