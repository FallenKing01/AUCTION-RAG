

def validate_ai_input(body: dict):
    
    if not isinstance(body, dict):
        raise Exception("Invalid input: body should be a dictionary")

    if "history" not in body or not isinstance(body["history"], list):
        raise Exception("Invalid input: 'history' should be a list")

    for item in body["history"]:
        if "role" not in item or item["role"] not in ["user", "assistant"]:
            raise Exception("Invalid role")

        if "content" not in item or item["content"].strip() == "":
            raise Exception("Invalid content")

    if "question" not in body or body["question"].strip() == "":
        raise Exception("Invalid question")