
import os
import html
import urllib.request
import json

token = os.environ["GH_STATS_TOKEN"]

request = urllib.request.Request(
    "https://api.github.com/user",
    headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2026-03-10"
    }
)

with urllib.request.urlopen(request) as response:
    user = json.loads(response.read())

username = html.escape(user["login"])
public_repos = user["public_repos"]
private_repos = user["owned_private_repos"]

svg = f"""<svg xmlns="http://www.w3.org/2000/svg"
width="850" height="190" viewBox="0 0 850 190">
<rect width="850" height="190" rx="12" fill="#191a23"/>

<text x="35" y="48" fill="#7aa2f7"
font-size="25" font-family="Arial">
{username} — Repository Statistics
</text>

<line x1="425" y1="75" x2="425" y2="155"
stroke="#414354" stroke-width="1"/>

<text x="220" y="112" text-anchor="middle"
fill="#7aa2f7" font-size="36" font-weight="bold">
{public_repos}
</text>
<text x="220" y="143" text-anchor="middle"
fill="#70d6c2" font-size="17">
Public Repositories
</text>

<text x="630" y="112" text-anchor="middle"
fill="#bb9af7" font-size="36" font-weight="bold">
{private_repos}
</text>
<text x="630" y="143" text-anchor="middle"
fill="#70d6c2" font-size="17">
Private Repositories
</text>
</svg>
"""

os.makedirs("assets", exist_ok=True)

with open("assets/repository-stats.svg", "w") as file:
    file.write(svg)

print("Repository statistics generated successfully.")
