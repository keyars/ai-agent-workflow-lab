import argparse
from agents.catalog import AGENTS

def main() -> None:
    parser = argparse.ArgumentParser(description="AI Agent Workflow Lab")
    sub = parser.add_subparsers(dest="command", required=True)
    cmd = sub.add_parser("agents", help="List available agents")
    cmd.set_defaults(handler=_list_agents)
    args = parser.parse_args()
    args.handler()

def _list_agents() -> None:
    for number, slug, description in AGENTS:
        print(f"{number}. {slug} — {description}")

if __name__ == "__main__":
    main()
