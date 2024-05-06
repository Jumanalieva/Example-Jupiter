import re

names = [
    "Abraham Lincoln",
    "Andrew P Garfield",
    "Connor Milliken",
    "Jordan Alexander Williams",
    "Madonna",
    "programming is cool"
]

pattern = re.compile(r"^[A-Z][a-z]*\s([A-Z][a-z]*\s?)*[A-Z][a-z]*$")


results = []
for name in names:
    match = pattern.match(name)
    if match:
        results.append(match.group(0))
    else:
        results.append(None)

print(results)

