import argparse
from colorama import Fore, init

from fetch_news import fetch_news
from database import create_table, insert_news, get_news
from exporter import export_csv, export_excel


init(autoreset=True)


create_table()


parser = argparse.ArgumentParser(description="News Aggregator CLI")

parser.add_argument("--fetch", action="store_true", help="Fetch latest news")
parser.add_argument("--source", type=str, help="Filter by source")
parser.add_argument("--keyword", type=str, help="Search by keyword")
parser.add_argument("--export", type=str, help="Export format csv/excel")

args = parser.parse_args()


if args.fetch:
    print(Fore.CYAN + "Fetching news...")

    news = fetch_news(args.source, args.keyword)

    insert_news(news)

    print(Fore.GREEN + f"{len(news)} news articles saved.")


records = get_news(args.keyword, args.source)


print(Fore.YELLOW + "\nSaved News:\n")

for row in records:
    print(Fore.WHITE + f"Title : {row[0]}")
    print(Fore.BLUE + f"Source: {row[1]}")
    print(Fore.MAGENTA + f"Date  : {row[2]}")
    print(Fore.CYAN + f"URL   : {row[3]}")
    print("-" * 70)


if args.export:
    if args.export.lower() == "csv":
        export_csv(records)

    elif args.export.lower() == "excel":
        export_excel(records)

    else:
        print("Invalid export format")