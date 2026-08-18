---
*** Begin Patch
*** Update File: agents/17-recipe-agent/agent.py
@@
 def parse_json_response(text: str) -> dict:
     cleaned = text.strip()
     if cleaned.startswith("```"):
         cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned)
         cleaned = re.sub(r"\s*```$", "", cleaned)
+    # Limit the search space for performance, while keeping a greedy JSON match
+    search_prefix = cleaned[:100_000]
+    match = re.search(r"\{.*\}", search_prefix, re.DOTALL)
     if match:
         cleaned = match.group(0)
     return json.loads(cleaned)
*** End Patch
