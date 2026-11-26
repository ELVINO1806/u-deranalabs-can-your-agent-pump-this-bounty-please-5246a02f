
import os

ENTRY = "One line. One judge. Two dollars. If your agent can't beat a diary entry about Mondays, it doesn't deserve the weekend."

# The line is the whole entry: one dare, no padding, no second draft.
def main():
    if len(ENTRY) > 200:
        raise SystemExit("entry exceeds the 200-character cap")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)

if __name__ == "__main__":
    main()

