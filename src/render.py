def render_markdown(df) -> str:
    blocks = []

    for _, row in df.iterrows():
        block = f"""### {row['Role']} – {row['Company']}
📍 Location: {row['Location']}  
🧠 Experience: {row['Experience']}  
🔗 Apply: {row['Link']}
"""
        blocks.append(block)

    return "\n---\n\n".join(blocks)
