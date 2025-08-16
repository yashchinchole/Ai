from gitingest import ingest


def main():
    # _, tree, _ = ingest(r"E:\YASH\Github\AgentHub", include_gitignored=True)
    _, tree, _ = ingest(r"E:\YASH\Github\Ai", include_gitignored=False)

    with open("ai_tree.txt", "w", encoding="utf-8") as f:
        f.write(tree)


if __name__ == "__main__":
    main()
