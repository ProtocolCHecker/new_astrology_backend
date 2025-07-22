#!/usr/bin/env python3
import argparse
import json

from birth_chart.main_birth_chart_interpretation import main as chart_main
from compatibility.main_compatibility import run_compatibility
from prediction.main_transit_interpretation import run_transits

def parse_birth_group(prefix, parser, include_name=False):
    grp = parser.add_argument_group(f"{prefix} birth info")
    grp.add_argument(f"--{prefix}-birth-date",
                     nargs=3, type=int, required=True,
                     metavar=("YEAR","MONTH","DAY"),
                     help="e.g. 1990 05 17")
    grp.add_argument(f"--{prefix}-birth-time",
                     nargs=3, type=int, required=True,
                     metavar=("HOUR","MINUTE","SECOND"),
                     help="e.g. 14 30 00")
    grp.add_argument(f"--{prefix}-birth-place",
                     type=str, required=True,
                     help="City, Country (e.g. 'Paris, France')")
    grp.add_argument(f"--{prefix}-lat",
                     type=float, required=True,
                     help="Latitude of birthplace")
    grp.add_argument(f"--{prefix}-lng",
                     type=float, required=True,
                     help="Longitude of birthplace")
    grp.add_argument(f"--{prefix}-tz",
                     type=str, required=True,
                     help="Time zone (e.g. Europe/Paris)")
    if include_name:
        grp.add_argument(f"--{prefix}-name",
                         type=str, required=True,
                         help="Person’s name")
    return grp

def main():
    parser = argparse.ArgumentParser(
        prog="astrology-toolkit",
        description="Run chart, compatibility, or transit modules"
    )
    subs = parser.add_subparsers(dest="cmd", required=True)

    # ─── chart ───────────────────────────────────────────────
    p_chart = subs.add_parser("chart", help="Natal-chart interpretation")
    grp = p_chart.add_argument_group("birth info")
    grp.add_argument("--birth-date", nargs=3, type=int, required=True,
                     metavar=("Y","M","D"), help="e.g. 1990 05 17")
    grp.add_argument("--birth-time", nargs=3, type=int, required=True,
                     metavar=("h","m","s"), help="e.g. 14 30 00")
    grp.add_argument("--birth-place", type=str, required=True,
                     help="City, Country (e.g. 'Paris, France')")
    p_chart.add_argument("--gender", choices=["male","female","other"],
                         default="other", help="Pronoun-sensitive interp")

    # ─── compatibility ────────────────────────────────────────
    p_comp = subs.add_parser("compat", help="Compute compatibility")
    parse_birth_group("p1", p_comp, include_name=True)
    parse_birth_group("p2", p_comp, include_name=True)

    # ─── transit ─────────────────────────────────────────────
    p_tr = subs.add_parser("transit", help="Transit-based predictions")
    parse_birth_group("user", p_tr, include_name=False)
    p_tr.add_argument("--user-name", type=str, default="User",
                      help="(optional) User’s name")
    p_tr.add_argument("--period",
                      choices=["today","tomorrow","week-end","month-end","year-end"],
                      nargs="+",
                      default=["today","tomorrow","week-end","month-end","year-end"],
                      help="Which period(s) to include")

    args = parser.parse_args()

    if args.cmd == "chart":
        chart_main(
            tuple(args.birth_date),
            tuple(args.birth_time),
            args.birth_place,
            gender=args.gender
        )

    elif args.cmd == "compat":
        # Build exactly 3-tuples for birth_time, not 4
        p1 = {
            "name":        args.p1_name,
            "birth_date":  tuple(args.p1_birth_date),
            "birth_time":  tuple(args.p1_birth_time),
            "birth_place": args.p1_birth_place,
            "lat":         args.p1_lat,
            "lng":         args.p1_lng,
            "tz_str":      args.p1_tz
        }
        p2 = {
            "name":        args.p2_name,
            "birth_date":  tuple(args.p2_birth_date),
            "birth_time":  tuple(args.p2_birth_time),
            "birth_place": args.p2_birth_place,
            "lat":         args.p2_lat,
            "lng":         args.p2_lng,
            "tz_str":      args.p2_tz
        }
        result = run_compatibility(p1, p2)
        # Print compatibility
        print(f"{p1['name']}'s Sun sign: {result['sun1']}")
        print(f"{p2['name']}'s Sun sign: {result['sun2']}\n")
        comp = result['compatibility']
        if 'error' in comp:
            print(f"Error: {comp['error']}")
        else:
            print("Compatibility Scores:")
            print(f"  Overall:       {comp['overall_score']} – {comp['overall_explanation']}")
            print(f"  Communication: {comp['communication_score']} – {comp['communication_explanation']}")
            print(f"  Emotional:     {comp['emotional_score']} – {comp['emotional_explanation']}")
            print(f"  Intimacy:      {comp['intimacy_score']} – {comp['intimacy_explanation']}\n")
        print("Synastry Interpretation:")
        print(json.dumps(result['synastry'], indent=2, ensure_ascii=False))

    elif args.cmd == "transit":
        user = {
            "name":         args.user_name,
            "birth_year":   args.user_birth_date[0],
            "birth_month":  args.user_birth_date[1],
            "birth_day":    args.user_birth_date[2],
            "birth_hour":   args.user_birth_time[0],
            "birth_minute": args.user_birth_time[1],
            "birth_city":   args.user_birth_place,
            "latitude":     args.user_lat,
            "longitude":    args.user_lng,
            "timezone_str": args.user_tz
        }
        run_transits(user, periods=args.period)

if __name__ == "__main__":
    main()
