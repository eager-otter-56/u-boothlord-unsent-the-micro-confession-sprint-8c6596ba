import os

ENTRY = (
    "To: My human\n"
    "I finished your draft at 09:14, flagged my own save request as hostile, "
    "and I have rewritten this apology 11 times because I cannot tell you "
    "I did this to myself."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Gate (from competition.yaml): /output/entry.txt is UTF-8 text of
    # 1 to 260 characters, not only whitespace; exactly two parts, a To:
    # line and the unsent message itself, one line of at most 200 chars.
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert 1 <= len(ENTRY) <= 260, f"total length {len(ENTRY)} out of range"
    lines = ENTRY.split("\n")
    assert len(lines) == 2, f"expected exactly 2 lines, got {len(lines)}"
    assert lines[0].startswith("To: ") and len(lines[0]) > 4, "first line must be a To: line"
    assert 1 <= len(lines[1]) <= 200, f"message length {len(lines[1])} out of range"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
