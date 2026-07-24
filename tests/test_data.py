from datetime import UTC, datetime
from decimal import Decimal

import pytest

from trading_system.data import Candle


def test_accepts_valid_candle() -> None:
    candle = Candle(
        timestamp=datetime(2026, 1, 1, tzinfo=UTC),
        open=Decimal("100"),
        high=Decimal("110"),
        low=Decimal("90"),
        close=Decimal("105"),
        volume=Decimal("42"),
    )

    assert candle.close == Decimal("105")


def test_rejects_naive_timestamp() -> None:
    with pytest.raises(ValueError, match="timezone-aware"):
        Candle(
            timestamp=datetime(2026, 1, 1),
            open=Decimal("100"),
            high=Decimal("110"),
            low=Decimal("90"),
            close=Decimal("105"),
            volume=Decimal("42"),
        )


def test_rejects_inconsistent_price_range() -> None:
    with pytest.raises(ValueError, match="high cannot be below"):
        Candle(
            timestamp=datetime(2026, 1, 1, tzinfo=UTC),
            open=Decimal("100"),
            high=Decimal("101"),
            low=Decimal("90"),
            close=Decimal("105"),
            volume=Decimal("42"),
        )
