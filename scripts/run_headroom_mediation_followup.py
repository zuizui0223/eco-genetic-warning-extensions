from __future__ import annotations

import argparse

from eco_genetic_warning_extensions.headroom_mediation_followup import write


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", required=True)
    parser.add_argument("--records", required=True)
    parser.add_argument("--protocol", default="experiments/headroom_mediation_followup_protocol.json")
    args = parser.parse_args()
    write(args.summary, args.records, args.protocol)


if __name__ == "__main__":
    main()
