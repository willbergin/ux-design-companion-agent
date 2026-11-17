#!/usr/bin/env python3
"""Optional deterministic implementation of the five-dimension UX review rubric."""
import argparse
from decimal import Decimal, ROUND_HALF_UP


def score(values):
    """Return (rating, label, coverage) or (None, 'Not scored', coverage).

    Values must have five items, each 0, 1, 2 or None.
    """
    if len(values) != 5 or any(v not in (0, 1, 2, None) for v in values):
        raise ValueError('Provide exactly five dimensions, each 0/1/2 or N/A')
    assessed = [v for v in values if v is not None]
    if len(assessed) < 3:
        return None, 'Not scored — insufficient evidence', len(assessed)
    raw = Decimal(10 * sum(assessed)) / Decimal(2 * len(assessed))
    rating = max(1, int(raw.quantize(Decimal(1), rounding=ROUND_HALF_UP)))
    label = 'Evidence-based' if len(assessed) == 5 else 'Provisional'
    return rating, label, len(assessed)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('dimensions', nargs=5, help='Each dimension: 0, 1, 2 or N/A')
    args = parser.parse_args()
    values = [None if x.lower() in ('n/a', 'na', '-') else int(x) for x in args.dimensions]
    rating, label, coverage = score(values)
    print(f'{label}: {rating}/10 ({coverage}/5 assessable)' if rating else f'{label} ({coverage}/5 assessable)')


if __name__ == '__main__':
    main()
