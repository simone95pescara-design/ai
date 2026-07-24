"""Minimal market-data model for the first vertical experiment."""

from dataclasses import dataclass
from datetime import UTC, datetime
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class Candle:
    """One OHLCV observation with explicit invariants."""

    timestamp: datetime
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: Decimal

    def __post_init__(self) -> None:
        if self.timestamp.tzinfo is None or self.timestamp.utcoffset() is None:
            raise ValueError("timestamp must be timezone-aware")
        if self.timestamp.tzinfo != UTC:
            raise ValueError("timestamp must use UTC")
        if self.low > min(self.open, self.close):
            raise ValueError("low cannot exceed open or close")
        if self.high < max(self.open, self.close):
            raise ValueError("high cannot be below open or close")
        if self.low > self.high:
            raise ValueError("low cannot exceed high")
        if self.volume < 0:
            raise ValueError("volume cannot be negative")
