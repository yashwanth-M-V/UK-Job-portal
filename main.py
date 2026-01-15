from src.ingest import load_jobs
from src.transform import filter_active_jobs
from src.render import render_markdown

DATA_PATH = "data/jobs.xlsx"
README_PATH = "README.md"

START_MARKER = "<!-- START:JOB_POSTINGS -->"
END_MARKER = "<!-- END:JOB_POSTINGS -->"

def update_readme(content: str):
    with open(README_PATH, "r", encoding="utf-8") as f:
        readme = f.read()

    if START_MARKER not in readme or END_MARKER not in readme:
        raise RuntimeError("README markers not found")

    before = readme.split(START_MARKER)[0]
    after = readme.split(END_MARKER)[1]

    new_readme = (
        before
        + START_MARKER
        + "\n\n"
        + content
        + "\n\n"
        + END_MARKER
        + after
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_readme)

def main():
    df = load_jobs(DATA_PATH)
    active_jobs = filter_active_jobs(df)
    markdown = render_markdown(active_jobs)
    update_readme(markdown)

if __name__ == "__main__":
    main()
