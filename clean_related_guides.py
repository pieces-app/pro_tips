import re, os

base = "/Users/tsavoknott/Development/GitHub/open-runtime/pro_tips/guides/MCP/Agent Setups & Integrations"
files = [
    f"{base}/Zed.md",
    f"{base}/GitHub Copilot.md",
    f"{base}/OpenAI Codex CLI.md",
    f"{base}/Google Gemini CLI.md",
    f"{base}/Amazon Q Developer.md",
    f"{base}/ChatGPT Developer Mode.md",
    f"{base}/Raycast.md",
    f"{base}/Rovo Dev CLI.md",
    f"{base}/OpenClaw.md",
]

for path in files:
    with open(path) as f:
        content = f.read()

    nav_hrefs = set(re.findall(r'<a href="([^"]+)">', content))

    rg_match = re.search(r'(## Related Guides\n)((?:.*\n)*?)(\n---)', content)
    if not rg_match:
        print(f"SKIP (no Related Guides): {os.path.basename(path)}")
        continue

    section_prefix = rg_match.group(1)
    section_body = rg_match.group(2)
    section_suffix = rg_match.group(3)

    original_body = section_body
    new_lines = []
    removed = []

    for line in section_body.split('\n'):
        href_match = re.search(r'\(([^)]+\.md[^)]*)\)', line)
        if href_match and line.strip().startswith('-'):
            href = href_match.group(1)
            href_norm = href.lstrip('./')
            is_redundant = any(
                nav.lstrip('./') == href_norm or
                nav.lstrip('./').endswith(href_norm) or
                href_norm.endswith(nav.lstrip('./'))
                for nav in nav_hrefs
            )
            if is_redundant:
                removed.append(line.strip())
                continue
        new_lines.append(line)

    new_body = '\n'.join(new_lines)
    new_body = re.sub(r'\n{3,}', '\n\n', new_body)

    if new_body != original_body:
        new_content = content.replace(
            section_prefix + original_body + section_suffix,
            section_prefix + new_body + section_suffix
        )
        rg_new = re.search(r'## Related Guides\n((?:\s*\n)*)\n---', new_content)
        if rg_new and not rg_new.group(1).strip():
            new_content = new_content.replace('## Related Guides\n' + rg_new.group(1) + '\n---', '---')

        with open(path, 'w') as f:
            f.write(new_content)
        print(f"FIXED {os.path.basename(path)}: removed {len(removed)} bullet(s)")
        for r in removed:
            print(f"  - {r[:80]}")
    else:
        print(f"OK (no redundancy): {os.path.basename(path)}")
