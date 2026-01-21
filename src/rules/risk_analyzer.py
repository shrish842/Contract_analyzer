"""
Rule-based contract risk analyzer.
Phase 1: High-precision rules for critical risk detection.
"""

import re
from typing import Dict, List, Tuple
from dataclasses import dataclass


@dataclass
class RiskFinding:
    """Represents a detected risk in a contract"""
    risk_type: str
    risk_level: str  # HIGH, MEDIUM, LOW
    explanation: str
    matched_text: str = ""
    confidence: float = 1.0


class ContractRiskRules:
    """Rule-based risk detection for contracts"""
    
    @staticmethod
    def check_unlimited_liability(text: str) -> RiskFinding:
        """Detect unlimited liability clauses"""
        text_lower = text.lower()
        
        # Risk indicators
        unlimited_indicators = [
            'unlimited liability',
            'unlimited indemnification',
            'no limit on liability',
            'without limitation'
        ]
        
        # Protective clauses
        cap_indicators = [
            'liability cap',
            'cap on damages',
            'maximum liability',
            'limited to'
        ]
        
        has_unlimited = any(ind in text_lower for ind in unlimited_indicators)
        has_cap = any(ind in text_lower for ind in cap_indicators)
        
        if has_unlimited and not has_cap:
            return RiskFinding(
                risk_type='unlimited_liability',
                risk_level='HIGH',
                explanation='Contract contains unlimited liability without damage cap',
                confidence=0.95
            )
        
        return None
    
    @staticmethod
    def check_auto_renewal(text: str) -> RiskFinding:
        """Detect problematic auto-renewal clauses"""
        text_lower = text.lower()
        
        has_auto_renewal = any([
            'automatically renew' in text_lower,
            'auto-renew' in text_lower,
            'evergreen' in text_lower
        ])
        
        # Check notice period
        notice_match = re.search(r'(\d+)\s*days?\s*(?:prior\s+)?notice', text_lower)
        long_notice = False
        if notice_match:
            days = int(notice_match.group(1))
            if days > 90:
                long_notice = True
        
        if has_auto_renewal and long_notice:
            return RiskFinding(
                risk_type='auto_renewal',
                risk_level='MEDIUM',
                explanation=f'Auto-renewal with {days}-day notice period (>90 days)',
                confidence=0.90
            )
        
        return None
    
    @classmethod
    def analyze(cls, contract_text: str) -> Dict:
        """Run all risk checks on a contract"""
        
        # Run all rule checks
        checks = [
            cls.check_unlimited_liability,
            cls.check_auto_renewal,
            # Add more checks here
        ]
        
        findings = []
        for check in checks:
            result = check(contract_text)
            if result:
                findings.append(result)
        
        # Determine overall risk
        risk_levels = [f.risk_level for f in findings]
        if 'HIGH' in risk_levels:
            overall_risk = 'HIGH'
        elif 'MEDIUM' in risk_levels:
            overall_risk = 'MEDIUM'
        else:
            overall_risk = 'LOW'
        
        return {
            'overall_risk': overall_risk,
            'findings': findings,
            'total_risks': len(findings)
        }


if __name__ == "__main__":
    # Example usage
    sample_contract = """
    This agreement contains unlimited liability provisions.
    The contract will automatically renew unless 120 days notice is provided.
    """
    
    analyzer = ContractRiskRules()
    results = analyzer.analyze(sample_contract)
    
    print(f"Overall Risk: {results['overall_risk']}")
    print(f"Total Risks Found: {results['total_risks']}")
    for finding in results['findings']:
        print(f"  - {finding.risk_type}: {finding.explanation}")
