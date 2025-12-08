OPEN_AI_API_KEY = "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"
import os
if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = OPEN_AI_API_KEY